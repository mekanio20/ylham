import { defineStore } from "pinia";
import api from "@/api/index";

export const useHighlightsStore = defineStore("highlights", {
  state: () => ({
    highlights: [],
    error: null,
    loading: false,
  }),
  getters: {
    dailyPoem: (state) => state.highlights.find((item) => item.rank === 1)?.poem
  },
  actions: {
    // GET
    async fetchHighlights(filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get("highlights/", { params: filteredParams });
        this.highlights = response.data;
        return response.data;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    }
  },
});