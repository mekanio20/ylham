import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  state: () => ({
    /**
     * @type {Array<{ id: number, type: 'success' | 'error' | 'info', title?: string, message: string }>}
     */
    items: [],
  }),
  actions: {
    /**
     * Show a new toast
     * @param {{ type?: 'success' | 'error' | 'info', title?: string, message: string, duration?: number }} payload
     */
    show(payload) {
      const { type = "error", title = "", message, duration = 6000 } = payload || {};
      if (!message) return;

      const id = Date.now() + Math.random();

      this.items.push({
        id,
        type,
        title,
        message,
      });

      if (duration && duration > 0) {
        setTimeout(() => {
          this.hide(id);
        }, duration);
      }
    },

    hide(id) {
      this.items = this.items.filter((item) => item.id !== id);
    },

    clear() {
      this.items = [];
    },
  },
});