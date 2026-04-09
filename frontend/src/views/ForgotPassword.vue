<template>
    <div class="h-screen bg-[#F5F2EC] flex font-garamond">
        <div class="flex-1 flex flex-col justify-center px-6 sm:px-10 lg:px-16 py-12">
            <div class="w-full max-w-sm mx-auto">

                <!-- Back Button -->
                <router-link to="/login"
                    class="inline-flex items-center gap-2 text-xs tracking-widest uppercase text-[#A8896C] hover:text-[#6B6B5A] transition-colors mb-4 font-dm">
                    <v-icon size="14" icon="mdi-arrow-left" />
                    Yzyna
                </router-link>

                <Transition name="step" mode="out-in">
                    <!-- Step 1: Email -->
                    <div v-if="step === 1" key="step1">
                        <div class="mb-6 text-center">
                            <div
                                class="w-14 h-14 rounded-full bg-[#EDE8E0] flex items-center justify-center mx-auto mb-4">
                                <v-icon size="24" icon="mdi-lock-reset" class="text-[#A8896C]" />
                            </div>
                            <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-2 font-dm">Parol dikeltmek
                            </p>
                            <h1 class="text-3xl sm:text-4xl text-[#1C1C1E] leading-tight">
                                Paroly ýatdan çykardym
                            </h1>
                            <p class="text-sm text-[#9A9A8A] mt-3 font-dm leading-relaxed">
                                E-poçta salgyňyzy giriziň, size täzeden tassyklama kody ugradarys.
                            </p>
                        </div>

                        <ErrorMessage :errorMsg="errorMsg" />

                        <div class="space-y-4">
                            <!-- Email -->
                            <div>
                                <label
                                    class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">E-poçta</label>
                                <div class="relative">
                                    <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                                        <v-icon size="16" icon="mdi-email-outline" />
                                    </span>
                                    <input v-model="form.email" type="email" placeholder="meselem@gmail.com"
                                        @blur="validateEmail" :class="[
                                            'w-full pl-10 pr-4 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all font-dm',
                                            fieldError.email
                                                ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                                                : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
                                        ]" />
                                </div>
                                <p v-if="fieldError.email" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{
                                    fieldError.email }}</p>
                            </div>
                            <!-- New Password -->
                            <div>
                                <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Täze
                                    parol</label>
                                <div class="relative">
                                    <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                                        <v-icon size="16" icon="mdi-lock-outline" />
                                    </span>
                                    <input v-model="form.password" :type="showPassword ? 'text' : 'password'"
                                        placeholder="••••••••" @blur="validatePassword" :class="[
                                            'w-full px-10 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all font-dm',
                                            fieldError.password
                                                ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                                                : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
                                        ]" />
                                    <button type="button" @click="showPassword = !showPassword"
                                        class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#6B6B5A] transition-colors">
                                        <v-icon size="16"
                                            :icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye-outline'" />
                                    </button>
                                </div>
                                <p v-if="fieldError.password" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{
                                    fieldError.password }}</p>
                            </div>
                            <!-- Confirm Password -->
                            <div class="pb-2">
                                <label
                                    class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Paroly
                                    tassyklamak</label>
                                <div class="relative">
                                    <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                                        <v-icon size="16" icon="mdi-lock-check-outline" />
                                    </span>
                                    <input v-model="form.confirmPassword" :type="showConfirm ? 'text' : 'password'"
                                        placeholder="••••••••" @blur="validateConfirm" :class="[
                                            'w-full px-10 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all font-dm',
                                            fieldError.confirmPassword
                                                ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                                                : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
                                        ]" />
                                    <button type="button" @click="showConfirm = !showConfirm"
                                        class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#6B6B5A] transition-colors">
                                        <v-icon size="16"
                                            :icon="showConfirm ? 'mdi-eye-off-outline' : 'mdi-eye-outline'" />
                                    </button>
                                </div>
                                <p v-if="fieldError.confirmPassword" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{
                                    fieldError.confirmPassword }}</p>
                            </div>

                            <button @click="handleSendCode" :disabled="authStore.loading" :class="[
                                'w-full py-3.5 rounded-xl text-sm font-medium transition-all duration-200 mt-6 flex items-center justify-center gap-2 font-dm',
                                authStore.loading
                                    ? 'bg-[#EDE8E0] text-[#B0A898] cursor-not-allowed'
                                    : 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.99]'
                            ]">
                                {{ authStore.loading ? 'Ýüklenýär...' : 'Kod ugratmak' }}
                            </button>
                        </div>
                    </div>

                    <!-- Step 2: OTP -->
                    <div v-else-if="step === 2" key="step2">
                        <div class="mb-6 text-center">
                            <div
                                class="w-14 h-14 rounded-full bg-[#EDE8E0] flex items-center justify-center mx-auto mb-4">
                                <v-icon size="24" icon="mdi-shield-key-outline" class="text-[#A8896C]" />
                            </div>
                            <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-2 font-dm">Tassyklama</p>
                            <h1 class="text-3xl sm:text-4xl text-[#1C1C1E] leading-tight">
                                Kody giriziň
                            </h1>
                            <p class="text-sm text-[#9A9A8A] mt-3 font-dm leading-relaxed">
                                <span class="text-[#6B6B5A] font-medium">{{ form.email }}</span> adresine iberilen 6
                                belgili kody giriziň.
                            </p>
                        </div>

                        <ErrorMessage :errorMsg="errorMsg" />

                        <div class="space-y-4">
                            <!-- OTP Inputs -->
                            <div class="flex gap-2 justify-between">
                                <input v-for="(_, i) in otp" :key="i" :ref="el => otpRefs[i] = el" v-model="otp[i]"
                                    type="text" inputmode="numeric" maxlength="1" @input="onOtpInput(i)"
                                    @keydown.backspace="onOtpBackspace(i)" @paste.prevent="onOtpPaste($event)" :class="[
                                        'w-11 h-12 text-center text-lg font-medium rounded-xl outline-none transition-all font-dm',
                                        otp[i]
                                            ? 'bg-[#1C1C1E] text-[#F5F0E8] border-2 border-[#1C1C1E]'
                                            : 'bg-[#F0EBE1] text-[#1C1C1E] border-2 border-transparent focus:border-[#A8896C]'
                                    ]" />
                            </div>

                            <button @click="handleVerifyOtp" :disabled="otp.join('').length < 6 || authStore.loading"
                                :class="[
                                    'w-full py-3.5 rounded-xl text-sm font-medium transition-all duration-200 mt-6 flex items-center justify-center gap-2 font-dm',
                                    otp.join('').length < 6 || authStore.loading
                                        ? 'bg-[#EDE8E0] text-[#B0A898] cursor-not-allowed'
                                        : 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.99]'
                                ]">
                                {{ authStore.loading ? 'Ýüklenýär...' : 'Tassyklamak' }}
                            </button>

                            <!-- Resend -->
                            <p class="text-center text-xs text-[#B0A898] font-dm pt-1">
                                Kod gelmedi mi?
                                <button v-if="resendCooldown === 0" @click="handleSendCode"
                                    class="text-[#A8896C] hover:underline font-medium">
                                    Täzeden ugratmak
                                </button>
                                <span v-else class="text-[#A8896C]">{{ resendCooldown }}s garaşyň</span>
                            </p>
                        </div>
                    </div>

                    <!-- Step 3: Success -->
                    <div v-else-if="step === 3" key="step3" class="text-center">
                        <div class="w-16 h-16 rounded-full bg-[#EDE8E0] flex items-center justify-center mx-auto mb-6">
                            <v-icon size="28" icon="mdi-check" class="text-[#A8896C]" />
                        </div>
                        <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-2 font-dm">Üstünlikli!</p>
                        <h1 class="text-3xl text-[#1C1C1E] leading-tight mb-3">
                            Parol täzelendi
                        </h1>
                        <p class="text-sm text-[#9A9A8A] font-dm leading-relaxed mb-8">
                            Täze parolyňyz üstünlikli bellendi. Indi ulgama girip bilersiňiz.
                        </p>
                        <router-link to="/login" :class="[
                            'w-full py-3.5 rounded-xl text-sm font-medium transition-all duration-200 flex items-center justify-center gap-2 font-dm',
                            'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.99]'
                        ]">
                            Ulgama girmek
                        </router-link>
                    </div>
                </Transition>

                <!-- Step Indicator -->
                <div v-if="step < 3" class="flex items-center justify-center gap-2 mt-8">
                    <div v-for="s in 2" :key="s" :class="[
                        'h-1 rounded-full transition-all duration-300',
                        s === step ? 'w-6 bg-[#A8896C]' : s < step ? 'w-3 bg-[#C8B99A]' : 'w-3 bg-[#DDD8CE]'
                    ]" />
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
const authStore = useAuthStore()

const step = ref(Number(sessionStorage.getItem('forgot_step')) || 1)
const errorMsg = ref('')
const showPassword = ref(false)
const showConfirm = ref(false)
const resendCooldown = ref(0)

const form = ref({
    email: '',
    password: '',
    confirmPassword: ''
})

const fieldError = ref({
    email: '',
    password: '',
    confirmPassword: ''
})

const otp = ref(['', '', '', '', '', ''])
const otpRefs = ref([])

// OTP handlers
const onOtpInput = (i) => {
    otp.value[i] = otp.value[i].replace(/\D/g, '')
    if (otp.value[i] && i < 5) otpRefs.value[i + 1]?.focus()
}

const onOtpBackspace = (i) => {
    if (!otp.value[i] && i > 0) {
        otp.value[i - 1] = ''
        otpRefs.value[i - 1]?.focus()
    }
}

const onOtpPaste = (e) => {
    const text = e.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6)
    text.split('').forEach((char, i) => { otp.value[i] = char })
    otpRefs.value[Math.min(text.length, 5)]?.focus()
}

// Validation
const validateEmail = () => {
    if (!form.value.email) {
        fieldError.value.email = 'E-poçta hökmany'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
        fieldError.value.email = 'Dogry e-poçta salgysy giriziň'
    } else {
        fieldError.value.email = ''
    }
}

const validatePassword = () => {
    if (!form.value.password) {
        fieldError.value.password = 'Parol hökmany'
    } else if (form.value.password.length < 6) {
        fieldError.value.password = 'Parol azyndan 6 harp bolmaly'
    } else {
        fieldError.value.password = ''
    }
}

const validateConfirm = () => {
    if (!form.value.confirmPassword) {
        fieldError.value.confirmPassword = 'Paroly tassyklaň'
    } else if (form.value.confirmPassword !== form.value.password) {
        fieldError.value.confirmPassword = 'Parollar deň däl'
    } else {
        fieldError.value.confirmPassword = ''
    }
}

// Cooldown timer
const startCooldown = () => {
    resendCooldown.value = 60
    const interval = setInterval(() => {
        resendCooldown.value--
        if (resendCooldown.value <= 0) clearInterval(interval)
    }, 1000)
}

// Step handlers
const handleSendCode = async () => {
    validateEmail()
    validatePassword()
    validateConfirm()
    if (fieldError.value.email) return
    if (fieldError.value.password || fieldError.value.confirmPassword) return
    errorMsg.value = ''
    try {
        await authStore.sendOtp({ email: form.value.email }, 'reset')
        sessionStorage.setItem('temp_reset_data', JSON.stringify({
            email: form.value.email,
            new_password: form.value.password,
            new_password_confirm: form.value.confirmPassword,
        }))
        otp.value = ['', '', '', '', '', '']
        step.value = 2
        sessionStorage.setItem('forgot_step', 2)
        startCooldown()
    } catch (e) {
        errorMsg.value = e?.response?.data?.detail || 'Ýalňyşlyk ýüze çykdy'
    }
}

const handleVerifyOtp = async () => {
    errorMsg.value = ''
    const temp_reset_data = JSON.parse(sessionStorage.getItem('temp_reset_data'))
    temp_reset_data.code = otp.value.join('')
    const response = await authStore.resetPassword(temp_reset_data)
    if (response.status === 200) {
        sessionStorage.clear()
        step.value = 3
    } else errorMsg.value = response.data?.code[0] || 'Ýalňyşlyk ýüze çykdy!'
}
</script>

<style scoped>
.step-enter-active,
.step-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}

.step-enter-from {
    opacity: 0;
    transform: translateX(16px);
}

.step-leave-to {
    opacity: 0;
    transform: translateX(-16px);
}
</style>