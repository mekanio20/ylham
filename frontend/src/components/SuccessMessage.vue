<template>
    <Transition enter-active-class="transition-all duration-200" enter-from-class="opacity-0 -translate-y-2"
        enter-to-class="opacity-100 translate-y-0">
        <div v-if="successMsg"
            class="mb-5 flex items-start gap-3 px-4 py-3 bg-[#F0FFF4] border border-[#A8D5B5] rounded-xl">
            <v-icon size="16" icon="mdi-check-circle-outline" class="text-[#27AE60] shrink-0 mt-0.5" />
            <p class="text-sm text-[#27AE60] font-dm">{{ successMsg }}</p>
        </div>
    </Transition>
</template>

<script setup>
defineProps({
    successMsg: String
})
</script>