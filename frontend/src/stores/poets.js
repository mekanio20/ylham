import { defineStore } from "pinia";
import api from "@/api/index";

export const usePoetStore = defineStore("poets", {
  state: () => ({
    poets: [],
    poet_detail: {},
    poet_count: 0,
    error: null,
    loading: false,
  }),
  actions: {
    // GET
    async fetchPoets(filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get("auth/poets/", { params: filteredParams });
        this.poet_count = response.data.count;
        this.poets = response.data.results;
        return response.data.results;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    async fetchPoetDetail(id) {
      this.loading = true;
      try {
        const response = await api.get(`poets/${id}/`);
        this.poet_detail = response.data;
        return response.data;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
  },
});
