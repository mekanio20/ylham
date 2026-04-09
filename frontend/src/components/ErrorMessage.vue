<template>
    <Transition enter-active-class="transition-all duration-200" enter-from-class="opacity-0 -translate-y-2"
        enter-to-class="opacity-100 translate-y-0">
        <div v-if="errorMsg"
            class="mb-5 flex items-start gap-3 px-4 py-3 bg-[#FFF0F0] border border-[#F5C6C6] rounded-xl">
            <v-icon size="16" icon="mdi-alert-circle-outline" class="text-[#C0392B] shrink-0 mt-0.5" />
            <p class="text-sm text-[#C0392B] font-dm">{{ errorMsg }}</p>
        </div>
    </Transition>
</template>

<script setup>
defineProps({ errorMsg: String })
</script>