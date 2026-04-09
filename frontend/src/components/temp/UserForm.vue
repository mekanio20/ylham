<template>
    <!-- ══ STEP 3 — Profil ══ -->
    <div v-if="currentStep === 3" key="step3" class="space-y-4">
        <div>
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Adyňyz we
                Familiýaňyz</label>
            <input v-model="form.name" type="text" placeholder="FAA"
                class="w-full px-4 py-3 bg-[#F0EBE1] border-2 border-transparent rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none focus:border-[#A8896C] resize-none transition-all"
                @blur="validateField('name')" />
            <p v-if="fieldError.name" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ fieldError.name }}</p>
        </div>

        <div>
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Ulanyjy ady</label>
            <div class="relative">
                <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898] text-sm font-dm">@</span>
                <input v-model="form.username" type="text" placeholder="Ulanyjy adyny giriziň"
                    :class="[...inputClass('username'), 'pl-8']" @blur="validateField('username')" />
                <span v-if="form.username && !fieldError.username && usernameAvailable"
                    class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#2E7D32]">
                    <v-icon size="16" icon="mdi-check-circle-outline" />
                </span>
                <span v-else-if="form.username && fieldError.username"
                    class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#C0392B]">
                    <v-icon size="16" icon="mdi-close-circle-outline" />
                </span>
            </div>
            <p v-if="fieldError.username" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ fieldError.username }}
            </p>
            <p v-else-if="form.username && usernameAvailable" class="mt-1.5 text-xs text-[#2E7D32] font-dm">Ulanyjy
                ady tassyklandy ✓</p>
        </div>

        <div>
            <label
                class="text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 flex items-center gap-2 font-dm">Biogorafiýa</label>
            <textarea v-model="form.bio" rows="2" placeholder="Özüňiz barada ýazyň..."
                class="w-full px-4 py-3 bg-[#F0EBE1] border-2 border-transparent rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none focus:border-[#A8896C] resize-none transition-all italic"
                maxlength="160"></textarea>
            <p class="text-right text-xs text-[#B0A898] mt-1 font-dm">{{ form.bio.length }}/160</p>
        </div>
    </div>
</template>

<script setup>
</script>