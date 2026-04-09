import { defineStore } from "pinia";
import api from "@/api/index";

export const usePoemStore = defineStore("poems", {
  state: () => ({
    poems: [],
    poem_detail: {},
    poems_count: 0,
    poem_comments: [],
    poem_comments_count: 0,
    error: null,
    loading: false,
  }),
  actions: {
    // GET
    async fetchPoems(filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get("poems/", { params: filteredParams });
        this.poems_count = response.data.count;
        this.poems = response.data.results;
        return response.data.results;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    async fetchPoemDetail(id) {
      this.loading = true;
      try {
        const response = await api.get(`poems/${id}/`);
        this.poem_detail = response.data;
        return response.data;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // POST
    // create
    async createPoem(data) {
      this.loading = true;
      try {
        await api.post("poems/create/", data);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // publish
    async publishPoem(id) {
      this.loading = true;
      try {
        await api.post(`poems/${id}/publish/`);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // PATCH
    async updatePoem(id, data) {
      this.loading = true;
      try {
        await api.patch(`poems/${id}/update/`, data);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // DELETE
    async deletePoem(id) {
      this.loading = true;
      try {
        await api.delete(`poems/${id}/delete/`);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },

    // COMMENTS
    // GET
    async fetchPoemComments(id, filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get(`poems/${id}/comments/`, { params: filteredParams });
        this.poem_comments_count = response.data.count;
        this.poem_comments = response.data.results;
        return response.data.results;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // POST
    async createPoemComment(id, data) {
      this.loading = true;
      try {
        const response = await api.post(`poems/${id}/comments/`, data);
        this.poem_comments.push(response.data)
        this.poem_comments_count++;
        return true
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
  },
});