import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
    meta: { layout: "base-layout" },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue"),
    meta: { guestOnly: true }
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("@/views/Register.vue"),
    meta: { guestOnly: true }
  },
  {
    path: "/forgot-password",
    name: "ForgotPassword",
    component: () => import("@/views/ForgotPassword.vue"),
    meta: { guestOnly: true }
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("@/views/Dashboard.vue"),
  },
  {
    path: "/poem/create",
    name: "PoemCreate",
    component: () => import("@/views/PoemCreate.vue"),
  },
  {
    path: "/poem/:id",
    name: "PoemDetail",
    component: () => import("@/views/PoemDetail.vue"),
  },
  {
    path: "/search",
    name: "SearchResults",
    component: () => import("@/views/SearchResults.vue"),
    meta: { layout: "base-layout" },
  },
  {
    path: "/terms",
    name: "Terms",
    component: () => import("@/views/Terms.vue"),
  },
  {
    path: "/privacy",
    name: "Privacy",
    component: () => import("@/views/Privacy.vue"),
  },
  {
    path: "/cookies",
    name: "Cookies",
    component: () => import("@/views/Cookies.vue"),
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: () => import("@/views/NotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.guestOnly && authStore.isAuthenticated) {
    next({ name: 'Home' })
  } else {
    next()
  }
})

export default router;
