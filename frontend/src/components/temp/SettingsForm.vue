<template>
    <!-- ══ STEP 4 — Settings ══ -->
    <div v-if="currentStep === 4" key="step4" class="space-y-5">
        <div class="space-y-3">
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] font-dm">Bildirişler</label>
            <div v-for="pref in notifPrefs" :key="pref.id"
                class="flex items-center justify-between py-3 px-4 bg-white rounded-xl border border-[#EDE8E0]">
                <div class="flex items-center gap-3">
                    <v-icon size="16" :icon="pref.icon" class="text-[#A8896C]" />
                    <div>
                        <p class="text-sm text-[#1C1C1E] font-dm font-medium">{{ pref.label }}</p>
                        <p class="text-xs text-[#9A9A8A] font-dm">{{ pref.desc }}</p>
                    </div>
                </div>
                <button @click="pref.value = !pref.value"
                    :class="['w-10 h-5 rounded-full transition-all duration-300 relative shrink-0', pref.value ? 'bg-[#1C1C1E]' : 'bg-[#D9D0C4]']">
                    <span
                        :class="['absolute top-0.5 w-4 h-4 bg-white rounded-full shadow transition-all duration-300', pref.value ? 'left-5' : 'left-0.5']"></span>
                </button>
            </div>
        </div>

        <div class="flex flex-col space-y-2">
            <div class="flex items-start gap-3 p-4 rounded-xl border border-[#EDE8E0]">
                <button type="button" @click="form.terms = !form.terms"
                    :class="['w-5 h-5 rounded-md border-2 flex items-center justify-center transition-all shrink-0 mt-0.5', form.terms ? 'bg-[#1C1C1E] border-[#1C1C1E]' : 'bg-white border border-[#1C1C1E] hover:border-[#9A9A8A]']">
                    <v-icon v-if="form.terms" size="12" icon="mdi-check" class="text-white" />
                </button>
                <p class="text-xs text-[#6B6B5A] leading-relaxed font-dm">
                    <router-link to="/terms" class="text-[#A8896C] hover:underline">Ulanyjy Şertlerini</router-link>
                    we
                    <router-link to="/privacy" class="text-[#A8896C] hover:underline">Gizlinlik
                        Syýasatyny</router-link>
                    okadym, kabul edýärin.
                </p>
            </div>
            <p v-if="fieldError.terms" class="pl-4 text-xs text-[#C0392B] font-dm">{{ fieldError.terms }}</p>
        </div>
    </div>
</template>

<script setup>
</script>