import { defineStore } from "pinia";

export const useAppStore = defineStore("app", {
  state: () => ({
    activeModal: "", // 'login' | 'register' | 'reset' | 'password' | 'otp'
  }),
  actions: {
    toggleModal(modal) {
      this.activeModal = this.activeModal === modal ? null : modal;
    },
    closeModal() {
      this.activeModal = null;
    },
  },
});