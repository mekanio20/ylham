<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-show="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" @click="$emit('close')" />

        <!-- Modal -->
        <div class="relative w-full max-w-sm bg-[#F5F2EC] rounded-2xl shadow-2xl font-garamond p-8">
          <!-- Close Button -->
          <button @click="$emit('close')"
            class="absolute top-4 right-4 text-[#B0A898] hover:text-[#6B6B5A] transition-colors">
            <v-icon size="20" icon="mdi-close" />
          </button>

          <!-- Header -->
          <div class="mb-8 text-center">
            <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-2 font-dm">Hoş geldiňiz</p>
            <h1 class="text-3xl text-[#1C1C1E] leading-tight">
              Hasaba girmek
            </h1>
            <p class="text-sm text-[#9A9A8A] mt-2 font-dm">
              Heniz hasabyňyz ýokmy?
              <button @click="toRegister" class="text-[#A8896C] hover:underline font-medium">
                Hasap döret
              </button>
            </p>
          </div>

          <!-- Error message -->
          <ErrorMessage :errorMsg="errorMsg" />

          <!-- Form -->
          <div class="space-y-4">
            <!-- Email -->
            <div>
              <label class="block text-xs tracking-widest uppercase text-[#6B6B5A] mb-2 font-dm">E-poçta</label>
              <div class="relative">
                <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                  <v-icon size="16" icon="mdi-email-outline" />
                </span>
                <input v-model="form.email" type="email" placeholder="meselem@gmail.com" :class="[
                  'w-full pl-10 pr-4 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all font-dm',
                  fieldError.email
                    ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                    : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
                ]" @blur="validateField('email')" />
              </div>
              <p v-if="fieldError.email" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ fieldError.email }}</p>
            </div>

            <!-- Password -->
            <div class="pb-2">
              <div class="flex items-center justify-between mb-2">
                <label class="text-xs tracking-widest uppercase text-[#6B6B5A] font-dm">Parol</label>
                <button @click="toForgotPassword" class="text-xs text-[#A8896C] hover:underline font-dm">
                  Paroly ýatdan çykardym
                </button>
              </div>
              <div class="relative">
                <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-[#B0A898]">
                  <v-icon size="16" icon="mdi-lock-outline" />
                </span>
                <input v-model="form.password" :type="showPassword ? 'text' : 'password'" placeholder="••••••••" :class="[
                  'w-full px-10 py-3 rounded-xl text-sm text-[#1C1C1E] placeholder-[#C8C0B0] outline-none transition-all',
                  fieldError.password
                    ? 'bg-[#FFF8F8] border-2 border-[#F5C6C6] focus:border-[#C0392B]'
                    : 'bg-[#F0EBE1] border-2 border-transparent focus:border-[#A8896C]'
                ]" @keyup.enter="handleLogin" @blur="validateField('password')" />
                <button type="button" @click="showPassword = !showPassword"
                  class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#6B6B5A] transition-colors">
                  <v-icon size="16" :icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye-outline'" />
                </button>
              </div>
              <p v-if="fieldError.password" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ fieldError.password }}</p>
            </div>

            <!-- Login button -->
            <button @click="handleLogin" :disabled="authStore.loading" :class="[
              'w-full py-3.5 rounded-xl text-sm font-medium transition-all duration-200 mt-2 flex items-center justify-center gap-2 font-dm',
              authStore.loading
                ? 'bg-[#EDE8E0] text-[#B0A898] cursor-not-allowed'
                : 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.99]'
            ]">
              {{ authStore.loading ? 'Ýüklenýär...' : 'Ulgama girmek' }}
            </button>
          </div>

          <!-- Privacy -->
          <p class="text-center text-xs text-[#B0A898] mt-8 leading-relaxed font-dm">
            Ulgama gireniňizde,
            <a href="/terms" target="_blank" class="text-[#A8896C] hover:underline">Ulanyjy Şertlerini</a> we
            <a href="/privacy" target="_blank" class="text-[#A8896C] hover:underline">Gizlinlik Syýasatyny</a>
            kabul edýärsiňiz.
          </p>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const router = useRouter()
const authStore = useAuthStore()
const form = ref({ email: '', password: '' })
const fieldError = ref({ email: '', password: '' })
const errorMsg = ref('')
const showPassword = ref(false)

const validateField = (field) => {
  if (field === 'email') {
    if (!form.value.email) {
      fieldError.value.email = 'E-poçta hökmany'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
      fieldError.value.email = 'Dogry e-poçta salgysy giriziň'
    } else {
      fieldError.value.email = ''
    }
  }
  if (field === 'password') {
    if (!form.value.password) {
      fieldError.value.password = 'Parol hökmany'
    } else if (form.value.password.length < 6) {
      fieldError.value.password = 'Parol azyndan 6 harp bolmaly'
    } else {
      fieldError.value.password = ''
    }
  }
}

const resetForm = () => {
  form.value = { email: '', password: '' }
  fieldError.value = { email: '', password: '' }
  errorMsg.value = ''
  showPassword.value = false
}

const handleLogin = async () => {
  validateField('email')
  validateField('password')
  if (fieldError.value.email || fieldError.value.password) return

  errorMsg.value = ''

  const response = await authStore.login({ login: form.value.email, password: form.value.password })
  if (response.status >= 400) {
    errorMsg.value = response.data.non_field_errors[0]
    return
  }

  resetForm()
  emit('close')
}

const toRegister = () => {
  emit('close')
  router.push({ name: "Register" })
}

const toForgotPassword = () => {
  emit('close')
  router.push({ name: "ForgotPassword" })
}

// Reset form when modal closes
watch(() => props.isOpen, (val) => {
  if (!val) resetForm()
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.25s ease;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.25s ease, opacity 0.25s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .relative {
  transform: translateY(16px);
  opacity: 0;
}

.modal-leave-to .relative {
  transform: translateY(8px);
  opacity: 0;
}
</style>