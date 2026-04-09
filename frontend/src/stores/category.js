import { defineStore } from "pinia";
import api from "@/api/index";

export const useCategoryStore = defineStore("categories", {
  state: () => ({
    categories: [],
    category_count: 0,
    error: null,
    loading: false,
  }),
  actions: {
    // GET
    async fetchCategories(filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get("categories/", { params: filteredParams });
        this.category_count = response.data.count;
        this.categories = response.data.results;
        return response.data.results;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
  },
});
