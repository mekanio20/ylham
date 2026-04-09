<template>
  <div>
    <LoginModal :is-open="appStore.activeModal === 'login'" @close="appStore.closeModal()" />
    <component :is="layout"></component>
  </div>
</template>

<script setup>
import baseLayout from '@/layouts/baseLayout.vue';
import emptyLayout from '@/layouts/emptyLayout.vue';
const route = useRoute()
const appStore = useAppStore()

const layouts = { 'base-layout': baseLayout, 'empty': emptyLayout }
const layout = computed(() => {
  return layouts[route.meta.layout] || layouts['empty']
})
</script>