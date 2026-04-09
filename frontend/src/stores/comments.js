import { defineStore } from "pinia";
import api from "@/api/index";

export const useCommentStore = defineStore("commenst", {
  state: () => ({
    comments: [],
    comment_detail: {},
    comments_count: 0,
    error: null,
    loading: false,
  }),
  actions: {
    // GET
    async fetchComments(filteredParams = {}) {
      this.loading = true;
      try {
        const response = await api.get("comments/", { params: filteredParams });
        this.comments_count = response.data.count;
        this.comments = response.data.results;
        return response.data.results;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    async fetchCommentDetail(id) {
      this.loading = true;
      try {
        const response = await api.get(`comments/${id}/`);
        this.comment_detail = response.data;
        return response.data;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // POST
    async createComment(data) {
      this.loading = true;
      try {
        await api.post("comments/create/", data);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // PATCH
    async updateComment(id, data) {
      this.loading = true;
      try {
        await api.patch(`comments/${id}/update/`, data);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
    // DELETE
    async deleteComment(id) {
      this.loading = true;
      try {
        await api.delete(`comments/${id}/delete/`);
        return true;
      } catch (error) {
        this.error = error;
        return error;
      } finally {
        this.loading = false;
      }
    },
  },
});
