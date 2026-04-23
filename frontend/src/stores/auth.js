import { defineStore } from "pinia";
import router from "@/router/index";
import api from "@/api/index";
import {
  setUser,
  setAccessToken,
  setRefreshToken,
  clearTokens,
} from "@/composables/useTokens";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: JSON.parse(localStorage.getItem('ylham_user')),
    access_token: localStorage.getItem("ylham_access"),
    refresh_token: localStorage.getItem("ylham_refresh"),
    error: null,
    loading: false,
  }),
  getters: {
    isAuthenticated: (state) => !!state.access_token,
    fullName: (state) => (state.user.first_name + state.user.last_name)
  },
  actions: {
    async login(data) {
      this.loading = true;
      try {
        const result = await api.post("auth/login/", data);
        const response = result.data
        setUser(response.data.user);
        setAccessToken(response.data.access);
        setRefreshToken(response.data.refresh);
        this.user = response.data.user;
        this.access_token = response.data.access;
        this.refresh_token = response.data.refresh;
        return response;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    async verifyOtp(data) {
      this.loading = true;
      try {
        const result = await api.post("auth/verify/", data);
        const response = result.data
        setUser(response.data.user);
        setAccessToken(response.data.access);
        setRefreshToken(response.data.refresh);
        this.user = response.data.user;
        this.access_token = response.data.access;
        this.refresh_token = response.data.refresh;
        return response;
      } catch (error) {
        this.error = error;
        return error
      } finally {
        this.loading = false;
      }
    },
    async register(payload) {
      this.loading = true;
      try {
        const data = await api.post("auth/register/", payload);
        return data;
      } catch (error) {
        this.error = error;
        return error
      } finally {
        this.loading = false;
      }
    },
    async resetPassword(data) {
      this.loading = true;
      try {
        const response = await api.post("auth/reset/", data);
        return response;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    logout() {
      clearTokens();
      this.user = {};
      this.access_token = null;
      this.refresh_token = null;
      router.push({ name: "Home" });
    },
  },
});