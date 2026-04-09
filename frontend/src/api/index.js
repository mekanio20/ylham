import router from "@/router/index";
import axios from "axios";
import {
  getAccessToken,
  getRefreshToken,
  setAccessToken,
  setRefreshToken,
  clearTokens,
} from "@/composables/useTokens";

const api = axios.create({
  baseURL: `${import.meta.env.VITE_API_BASE_URL}`,
  crossdomain: true,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  headers: {
    "Content-Type": "application/json",
    "Accept-Language": localStorage.getItem("lang") || "tk",
  },
  withCredentials: true,
});

const plainAxios = axios.create({
  baseURL: `${import.meta.env.VITE_API_BASE_URL}`,
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});

api.interceptors.request.use(
  (config) => {
    config.headers["Accept-Language"] = localStorage.getItem("lang");
    if (getAccessToken()) {
      config.headers.Authorization = `Bearer ${getAccessToken()}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (token) {
      prom.resolve(token);
    } else {
      prom.reject(error);
    }
  });
  failedQueue = [];
};

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        }).then((token) => {
          originalRequest.headers.Authorization = `Bearer ${token}`;
          return api(originalRequest);
        });
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        const { data } = await plainAxios.post("auth/token/refresh/", {
          refresh: getRefreshToken() || "",
        });

        setAccessToken(data.access);
        setRefreshToken(data.refresh);
        processQueue(null, data.access);
        originalRequest.headers.Authorization = `Bearer ${data.access}`;
        return api(originalRequest);
      } catch (err) {
        processQueue(err, null);
        clearTokens();

        const appStore = useAppStore()
        appStore.toggleModal('login')

        return Promise.reject(err);
      } finally {
        isRefreshing = false;
      }
    }

    return Promise.reject(error.response);
  },
);

export default api;