<template>
    <!-- Stepper -->
    <div class="flex items-center justify-center gap-2 mb-8">
        <div v-for="i in 4" :key="i" class="flex items-center gap-2">
            <div :class="[
                'w-7 h-7 rounded-full flex items-center justify-center text-xs font-semibold transition-all duration-300',
                currentStep > i
                    ? 'bg-[#A8896C] text-[#F5F0E8]'
                    : currentStep === i
                        ? 'bg-[#1C1C1E] text-[#F5F0E8]'
                        : 'bg-[#EDE8E0] text-[#9A9A8A]'
            ]">
                <v-icon v-if="currentStep > i" size="14" icon="mdi-check" />
                <span v-else class="font-dm">{{ i }}</span>
            </div>
            <div v-if="i < 4"
                :class="['flex-1 h-0.5 w-8 transition-all duration-300', currentStep > i ? 'bg-[#A8896C]' : 'bg-[#EDE8E0]']">
            </div>
        </div>
    </div>
</template>

<script setup>
</script>