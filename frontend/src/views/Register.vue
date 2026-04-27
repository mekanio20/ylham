<template>
  <div class="min-h-screen bg-[#F5F2EC] flex font-garamond">
    <div class="flex-1 flex flex-col justify-center px-6 sm:px-10 lg:px-16 py-10 overflow-y-auto">
      <div class="w-full max-w-sm mx-auto">

        <!-- Header -->
        <div class="mb-7 text-center">
          <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-1.5 font-dm">{{ stepLabels[currentStep - 1] }}
          </p>
          <h1 class="text-3xl sm:text-4xl text-[#1C1C1E] leading-tight">
            {{ stepTitles[currentStep - 1] }}
          </h1>
          <p class="text-sm text-[#9A9A8A] mt-2 font-dm" v-if="currentStep !== 2">
            Hasabyňyz bar bolsa,
            <router-link to="/login" class="text-[#A8896C] hover:underline font-medium">Ulgama giriň!</router-link>
          </p>
          <!-- Step 2 subtitle -->
          <p v-else class="text-sm text-[#9A9A8A] mt-2 font-dm leading-relaxed">
            <span class="text-[#1C1C1E] font-medium">{{ maskedEmail }}</span> salgysyna<br />
            6 belgili kod ugradyldy
          </p>
        </div>

        <!-- Error message -->
        <ErrorMessage :errorMsg="errorMsg" />

        <!-- Success message -->
        <SuccessMessage :successMsg="successMsg" />

        <!-- ══ STEP 1 — Account info ══ -->
        <div v-if="currentStep === 1" class="space-y-4">
          <!-- Email -->
          <div>
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">E-poçta</label>
            <div class="relative">
              <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                <v-icon size="16" icon="mdi-email-outline" />
              </span>
              <input v-model="form.email" type="email" placeholder="meselem@gmail.com" :class="inputClass('email')"
                @blur="validateField('email')" />
            </div>
            <p v-if="fieldError.email" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ fieldError.email }}</p>
          </div>

          <!-- Password -->
          <div>
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Parol</label>
            <div class="relative">
              <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                <v-icon size="16" icon="mdi-lock-outline" />
              </span>
              <input v-model="form.password" :type="showPassword ? 'text' : 'password'"
                placeholder="Azyndan 8 belgi bolmaly" :class="inputClass('password')"
                @blur="validateField('password')" />
              <button type="button" @click="showPassword = !showPassword"
                class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#6B6B5A] transition-colors">
                <v-icon size="16" :icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye-outline'" />
              </button>
            </div>
            <!-- Password strength -->
            <div class="mt-2 flex gap-1">
              <div v-for="i in 4" :key="i"
                :class="['h-1 flex-1 rounded-full transition-all duration-300', passwordStrength >= i ? strengthColor : 'bg-[#EDE8E0]']">
              </div>
            </div>
            <p class="mt-1 text-xs font-dm" :class="strengthTextColor">{{ strengthLabel }}</p>
            <p v-if="fieldError.password" class="mt-1 text-xs text-[#C0392B] font-dm">{{ fieldError.password }}</p>
          </div>

          <!-- Confirm password -->
          <div>
            <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">Paroly gaýtadan
              giriziň</label>
            <div class="relative">
              <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                <v-icon size="16" icon="mdi-lock-check-outline" />
              </span>
              <input v-model="form.confirmPassword" :type="showPassword ? 'text' : 'password'"
                placeholder="Paroly gaýtadan giriziň" :class="inputClass('confirmPassword')"
                @blur="validateField('confirmPassword')" />
              <span v-if="form.confirmPassword && !fieldError.confirmPassword"
                class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#2E7D32]">
                <v-icon size="16" icon="mdi-check-circle-outline" />
              </span>
            </div>
            <p v-if="fieldError.confirmPassword" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{
              fieldError.confirmPassword }}</p>
          </div>
        </div>

        <div v-if="currentStep === 1" class="flex flex-col space-y-2 mt-4">
          <div class="flex items-center gap-3 rounded-xl">
            <button type="button" @click="form.terms = !form.terms"
              :class="['w-5 h-5 rounded-md border-2 flex items-center justify-center transition-all shrink-0 mt-0.5', form.terms ? 'bg-[#1C1C1E] border-[#1C1C1E]' : 'bg-white border border-[#1C1C1E] hover:border-[#9A9A8A]']">
              <v-icon v-if="form.terms" size="12" icon="mdi-check" class="text-white" />
            </button>
            <p class="text-xs text-[#6B6B5A] leading-relaxed font-dm">
              <a href="/terms" target="_blank" class="text-[#A8896C] hover:underline">Ulanyjy Şertlerini</a>
              we
              <a href="/privacy" target="_blank" class="text-[#A8896C] hover:underline">Gizlinlik
                Syýasatyny</a>
              okadym, kabul edýärin.
            </p>
          </div>
          <p v-if="fieldError.terms" class="pl-4 text-xs text-[#C0392B] font-dm">{{ fieldError.terms }}</p>
        </div>

        <!-- ══ STEP 2 — OTP ══ -->
        <div v-if="currentStep === 2" class="space-y-4">
          <!-- OTP Inputs -->
          <div class="flex justify-center gap-3">
            <input v-for="(digit, i) in otp" :key="i" :ref="el => { if (el) otpInputs[i] = el }" v-model="otp[i]"
              type="text" inputmode="numeric" maxlength="1" :class="[
                'w-12 h-14 text-center text-xl text-[#1C1C1E] rounded-lg outline-none transition-all duration-200 font-dm',
                otpHasError
                  ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                  : otp[i]
                    ? 'bg-[#F0EBE1] border-2 border-[#A8896C]'
                    : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
              ]" @input="onOtpInput(i, $event)" @keydown="onOtpKeydown(i, $event)" @paste="onOtpPaste($event)" />
          </div>

          <!-- Resend -->
          <div class="text-center pt-2">
            <p class="text-sm text-[#9A9A8A] font-dm mb-1">Kody almadyňyzmy?</p>
            <button @click="handleResend" :disabled="resendCooldown > 0" :class="[
              'text-sm font-medium font-dm transition-colors',
              resendCooldown > 0 ? 'text-[#B0A898] cursor-not-allowed' : 'text-[#A8896C] hover:underline'
            ]">
              <span v-if="resendCooldown > 0">{{ resendCooldown }}s soň täzeden ugradyň</span>
              <span v-else>Täzeden ugratmak</span>
            </button>
          </div>
        </div>

        <!-- ══ Buttons ══ -->
        <div class="flex gap-3 mt-7">
          <!-- Prev button -->
          <button v-if="currentStep > 1" @click="prevStep"
            class="flex-1 py-3 rounded-xl border border-[#D9D0C4] text-[#6B6B5A] text-sm hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-all font-dm">
            ← Yza
          </button>

          <!-- Otp button -->
          <button v-if="currentStep === 2" @click="handleVerifyOtp" :disabled="otpValue.length < 6 || authStore.loading"
            :class="[
              'flex-1 py-3 rounded-xl text-sm font-medium transition-all duration-200 flex items-center justify-center gap-2 font-dm',
              otpValue.length < 6 || authStore.loading
                ? 'bg-[#EDE8E0] text-[#B0A898] cursor-not-allowed'
                : 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.99]'
            ]">
            <v-icon v-if="authStore.loading" size="16" icon="mdi-loading" class="animate-spin" />
            {{ authStore.loading ? 'Ýüklenýär...' : 'Tassyklamak' }}
          </button>

          <!-- Next button -->
          <button v-else-if="currentStep === 1" @click="nextStep" :disabled="authStore.loading"
            class="flex-1 py-3 rounded-xl text-[#F5F0E8] text-sm transition-all font-dm"
            :class="[authStore.loading ? 'bg-[#3A3A2E] cursor-not-allowed' : 'bg-[#1C1C1E] hover:bg-[#3A3A2E] active:scale-[0.99] cursor-pointer']">
            {{ authStore.loading ? 'Ýüklenýär...' : 'Dowam et →' }}
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
const router = useRouter()
const authStore = useAuthStore()
const errorMsg = ref('')
const successMsg = ref('')
const showPassword = ref(false)
const currentStep = ref(Number(sessionStorage.getItem('step')) || 1)

const stepLabels = ['Hasap maglumatlary', 'E-poçta tassyklama']
const stepTitles = ['Hasabyňyzy dörediň', 'Kodyny giriziň']

// ── Form ──
const form = reactive(sessionStorage.getItem('form') ? JSON.parse(sessionStorage.getItem('form')) : {
  email: '', password: '', confirmPassword: '',
  terms: false,
})

const fieldError = reactive({
  email: '', password: '', confirmPassword: '',
  terms: '',
})

// ── OTP ──
const otp = ref(['', '', '', '', '', ''])
const otpInputs = ref([])
const otpHasError = ref(false)
const resendCooldown = ref(0)
let cooldownTimer = null

const otpValue = computed(() => otp.value.join(''))

const maskedEmail = computed(() => {
  const email = form.email
  if (!email) return
  const [local, domain] = email?.split('@')
  if (!domain) return email
  return `${local.slice(0, 2)}***@${domain}`
})

const onOtpInput = (index, event) => {
  const val = event.target.value.replace(/\D/g, '')
  otp.value[index] = val.slice(-1)
  otpHasError.value = false
  errorMsg.value = ''
  if (val && index < 5) otpInputs.value[index + 1]?.focus()
}

const onOtpKeydown = (index, event) => {
  if (event.key === 'Backspace') {
    if (!otp.value[index] && index > 0) {
      otp.value[index - 1] = ''
      otpInputs.value[index - 1]?.focus()
    } else {
      otp.value[index] = ''
    }
  }
  if (event.key === 'ArrowLeft' && index > 0) otpInputs.value[index - 1]?.focus()
  if (event.key === 'ArrowRight' && index < 5) otpInputs.value[index + 1]?.focus()
}

const onOtpPaste = (event) => {
  event.preventDefault()
  const pasted = event.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6)
  pasted.split('').forEach((char, i) => { if (i < 6) otp.value[i] = char })
  otpInputs.value[Math.min(pasted.length, 5)]?.focus()
}

const handleVerifyOtp = async () => {
  if (otpValue.value.length < 6 || authStore.loading) return
  errorMsg.value = ''
  successMsg.value = ''
  otpHasError.value = false
  const response = await authStore.verifyOtp({ email: form.email, code: otpValue.value, purpose: 'registration' })
  if (response.status === 200) {  
    successMsg.value = 'E-poçta tassyklandy!'
    sessionStorage.clear()
    setTimeout(() => {
      router.push({ name: "Home" })
    }, 1000);
  }
  
  else if (response.status >= 400) {
    errorMsg.value = response.msg
    return
  }
}

const handleResend = async () => {
  if (resendCooldown.value > 0) return
  successMsg.value = ''
  errorMsg.value = ''
  try {
    const response = await authStore.register({ email: form.email, password: form.password, termsAccepted: form.terms, purpose: 'registration' })
    if (response.status >= 400) {
      errorMsg.value = response.data.msg
      return
    }
    successMsg.value = 'Kod täzeden ugradyldy!'
    startCooldown(60)
  } catch {
    errorMsg.value = 'Ýalňyşlyk ýüze çykdy.'
  }
}

const startCooldown = (seconds) => {
  clearInterval(cooldownTimer)
  resendCooldown.value = seconds
  cooldownTimer = setInterval(() => {
    resendCooldown.value--
    if (resendCooldown.value <= 0) clearInterval(cooldownTimer)
  }, 1000)
}

// ── Password Strength ──
const passwordStrength = computed(() => {
  const p = form.password
  if (!p) return 0
  let score = 0
  if (p.length >= 8) score++
  if (/[A-Z]/.test(p)) score++
  if (/[0-9]/.test(p)) score++
  if (/[^A-Za-z0-9]/.test(p)) score++
  return score
})
const strengthColor = computed(() =>
  ['bg-[#C0392B]', 'bg-[#E67E22]', 'bg-[#F1C40F]', 'bg-[#27AE60]'][passwordStrength.value - 1] || 'bg-[#EDE8E0]'
)
const strengthTextColor = computed(() =>
  ['text-[#C0392B]', 'text-[#E67E22]', 'text-[#F1C40F]', 'text-[#27AE60]'][passwordStrength.value - 1] || 'text-[#9A9A8A]'
)
const strengthLabel = computed(() =>
  ['Örän gowşak', 'Gowşak', 'Ortaça', 'Güýçli'][passwordStrength.value - 1] || ''
)

// ── Input class helper ──
const inputClass = (field) => [
  'w-full px-10 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all border-2 font-dm',
  fieldError[field]
    ? 'bg-[#FFF8F8] border-[#F5C6C6] focus:border-[#C0392B]'
    : 'bg-[#F0EBE1] border-transparent focus:border-[#A8896C]'
]

// ── Validation ──
const validateField = (field) => {
  const v = form
  const e = fieldError
  if (field === 'email') {
    e.email = !v.email ? 'E-poçta hökmany'
      : !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.email) ? 'Dogry e-poçta giriziň' : ''
  }
  if (field === 'password') {
    e.password = !v.password ? 'Açar söz hökmany'
      : v.password.length < 8 ? 'Iň azyndan 8 belgi bolmaly' : ''
  }
  if (field === 'confirmPassword') {
    e.confirmPassword = !v.confirmPassword ? 'Açar sözi gaýtadan giriziň'
      : v.confirmPassword !== v.password ? 'Açar sözler gabat gelenok' : ''
  }
}

const validateStep = (step) => {
  errorMsg.value = ''
  if (step === 1) {
    validateField('email'); validateField('password'); validateField('confirmPassword')
    if (!form.terms) fieldError.terms = 'Dowam etmek üçin şertleri kabul etmelisiňiz'
    return !fieldError.email && !fieldError.password && !fieldError.confirmPassword && form.terms
  }
  return true
}

const nextStep = async () => {
  if (!validateStep(currentStep.value)) return
  try {
    if (currentStep.value === 1) {
      const response = await authStore.register({ email: form.email, password: form.password, termsAccepted: form.terms })
      if (response.status >= 400) {
        errorMsg.value = response.data.msg
        return
      }
      startCooldown(60)
    }
    currentStep.value++
    sessionStorage.setItem('step', currentStep.value)
    sessionStorage.setItem('form', JSON.stringify(form))
    if (currentStep.value === 2) {
      nextTick(() => otpInputs.value[0]?.focus())
    }
  } catch (error) {
    console.error('Registration error:', error)
  }
}

const prevStep = () => {
  errorMsg.value = ''
  successMsg.value = ''
  if (currentStep.value === 2) {
    otp.value = ['', '', '', '', '', '']
    otpHasError.value = false
    clearInterval(cooldownTimer)
    resendCooldown.value = 0
  }
  currentStep.value--
  sessionStorage.setItem('step', currentStep.value)
}

onUnmounted(() => clearInterval(cooldownTimer))
</script>