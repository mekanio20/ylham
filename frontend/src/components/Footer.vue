<template>
  <footer class="bg-[#1C1C1E] text-[#F5F0E8] font-garamond">

    <!-- Izgara dokusu -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.035]"
      style="background-image: repeating-linear-gradient(0deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px),repeating-linear-gradient(90deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px);">
    </div>

    <!-- Üst ayırıcı çizgi -->
    <div class="h-px bg-gradient-to-r from-transparent via-[#A8896C]/40 to-transparent"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

      <!-- ── Ana Bölüm ── -->
      <div class="py-12 sm:py-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-8">

        <!-- Kolon 1 — Marka -->
        <div class="sm:col-span-2 lg:col-span-1">
          <router-link to="/" class="inline-block mb-5">
            <span class="text-2xl text-[#F5F0E8] leading-none italic font-light">
              <span class="text-[#A8896C]">Ylham</span>
            </span>
          </router-link>
          <p class="text-sm text-[#6B6B6B] leading-relaxed mb-6 font-dm text-[13px]">
            Sözler ruhuň galdyran yzlarydyr. Goşgyňyzy ýazyň, paýlaşyň, yzyňyzy galdyryň.
          </p>
          <!-- Sosyal medya -->
          <div class="flex items-center gap-2">
            <a v-for="social in socials" :key="social.label" :href="social.href" target="_blank" rel="noopener"
              :aria-label="social.label"
              class="w-8 h-8 rounded-lg bg-[#2E2E30] hover:bg-[#A8896C]/20 border border-[#2E2E30] hover:border-[#A8896C]/40 flex items-center justify-center text-[#6B6B6B] hover:text-[#A8896C] transition-all duration-200">
              <v-icon size="16" :icon="social.icon" />
            </a>
          </div>
        </div>

        <!-- Kolon 2 — Keşfet -->
        <div>
          <h3 class="text-xs tracking-[0.2em] uppercase text-[#A8896C] mb-5 font-dm">Keşfet</h3>
          <ul class="space-y-3">
            <li v-for="link in discoverLinks" :key="link.label">
              <router-link :to="link.to"
                class="text-sm text-[#8A8A8A] hover:text-[#F5F0E8] transition-colors flex items-center gap-2 group font-dm text-[13px]">
                <span class="w-0 group-hover:w-2 h-px bg-[#A8896C] transition-all duration-200 shrink-0"></span>
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Kolon 3 — Platform -->
        <div>
          <h3 class="text-xs tracking-[0.2em] uppercase text-[#A8896C] mb-5 font-dm">Platform</h3>
          <ul class="space-y-3">
            <li v-for="link in platformLinks" :key="link.label">
              <router-link :to="link.to"
                class="text-sm text-[#8A8A8A] hover:text-[#F5F0E8] transition-colors flex items-center gap-2 group"
                style="font-family: 'DM Sans', sans-serif; font-size: 13px;">
                <span class="w-0 group-hover:w-2 h-px bg-[#A8896C] transition-all duration-200 shrink-0"></span>
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Kolon 4 — Newsletter -->
        <div>
          <h3 class="text-xs tracking-[0.2em] uppercase text-[#A8896C] mb-5 font-dm">Haftalık Şiir</h3>
          <p class="text-sm text-[#6B6B6B] leading-relaxed mb-4 font-dm text-[13px]">
            Her hafta seçilmiş bir şiir, doğrudan posta kutuna.
          </p>

          <div>
            <div class="flex gap-2">
              <div class="relative flex-1 min-w-0">
                <input
                  v-model="email"
                  type="email"
                  placeholder="e-posta adresin"
                  class="w-full px-3.5 py-2.5 bg-[#2E2E30] border border-[#3A3A3C] rounded-xl text-sm text-[#F5F0E8] placeholder-[#4A4A4C] outline-none focus:border-[#A8896C] transition-all font-dm text-[12px]"
                  @keyup.enter="subscribe"
                />
              </div>
              <button @click="subscribe"
                class="px-3.5 py-2.5 bg-[#A8896C] text-[#1C1C1E] rounded-xl text-xs font-semibold hover:bg-[#C8A87C] transition-all shrink-0 font-dm">
                <v-icon size="16" icon="mdi-send-outline" />
              </button>
            </div>
            <p v-if="emailError" class="mt-1.5 text-xs text-[#C0392B] font-dm">{{ emailError }}</p>
          </div>

        </div>
      </div>

      <!-- ── Alt Bar ── -->
      <div class="border-t border-[#2E2E30] py-5 flex flex-col sm:flex-row items-center justify-between gap-3">
        <p class="text-xs text-[#4A4A4C] order-2 sm:order-1 font-dm">
          © {{ new Date().getFullYear() }} Ylham. Ähli hukuklary goralan.
        </p>

        <div class="flex items-center gap-4 order-1 sm:order-2 flex-wrap justify-center">
          <router-link v-for="link in legalLinks" :key="link.label" :to="link.to"
            class="text-xs text-[#4A4A4C] hover:text-[#8A8A8A] transition-colors font-dm">
            {{ link.label }}
          </router-link>
          <span class="text-[#2E2E30]">·</span>
          <!-- Dil saýla -->
          <!-- <div class="relative lang-selector">
            <button @click="langOpen = !langOpen"
              class="flex items-center gap-1.5 text-xs text-[#4A4A4C] hover:text-[#8A8A8A] transition-colors font-dm">
              <v-icon size="13" icon="mdi-translate" />
              {{ currentLang.label }}
              <v-icon size="11" icon="mdi-chevron-up" />
            </button>
            <Transition
              enter-active-class="transition-all duration-150 ease-out"
              enter-from-class="opacity-0 translate-y-1"
              enter-to-class="opacity-100 translate-y-0"
              leave-active-class="transition-all duration-100"
              leave-from-class="opacity-100"
              leave-to-class="opacity-0">
              <div v-if="langOpen"
                class="absolute bottom-full right-0 mb-2 bg-[#2E2E30] border border-[#3A3A3C] rounded-xl overflow-hidden shadow-xl">
                <button v-for="lang in languages" :key="lang.code"
                  @click="currentLang = lang; langOpen = false"
                  :class="['flex items-center gap-2 w-full px-4 py-2 text-xs transition-colors whitespace-nowrap font-dm', currentLang.code === lang.code ? 'text-[#A8896C] bg-[#3A3A3C]' : 'text-[#8A8A8A] hover:text-[#F5F0E8] hover:bg-[#3A3A3C]']">
                  {{ lang.flag }} {{ lang.label }}
                </button>
              </div>
            </Transition>
          </div> -->
        </div>
      </div>

    </div>
  </footer>
</template>

<script setup>
const email = ref('')
const emailError = ref('')
const subscribed = ref(false)
const langOpen = ref(false)

const languages = [
  { code: 'tr', label: 'Türkçe',     flag: '🇹🇷' },
  { code: 'en', label: 'English',    flag: '🇬🇧' },
  { code: 'tk', label: 'Türkmençe', flag: '🇹🇲' },
]
const currentLang = ref(languages[0])

const socials = [
  { label: 'X / Twitter', icon: 'mdi-twitter',   href: '#' },
  { label: 'Instagram',   icon: 'mdi-instagram',  href: '#' },
  { label: 'RSS',         icon: 'mdi-rss',        href: '#' },
]

const discoverLinks = [
  { label: 'Öne Çıkan Şiirler', to: '/' },
  { label: 'En Çok Beğenilenler', to: '/explore' },
  { label: 'Yeni Şiirler', to: '/new' },
  { label: 'Temalar', to: '/themes' },
  { label: 'Şairler', to: '/poets' },
]

const platformLinks = [
  { label: 'Şiir Yaz', to: '/create' },
  { label: 'Giriş Yap', to: '/login' },
  { label: 'Kayıt Ol', to: '/register' },
  { label: 'Yardım', to: '/help' },
]

const legalLinks = [
  { label: 'Gizlinlik syýasaty',        to: '/privacy' },
  { label: 'Ulanyjy şertleri', to: '/terms' },
  { label: 'Kukiler',        to: '/cookies' },
]

const subscribe = () => {
  emailError.value = ''
  if (!email.value.trim()) {
    emailError.value = 'E-posta adresi gerekli'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    emailError.value = 'Geçerli bir e-posta girin'
    return
  }
  subscribed.value = true
}

// Dışarı tıklayınca dil menüsünü kapat
const handleClickOutside = (e) => {
  if (!e.target.closest('.lang-selector')) langOpen.value = false
}
onMounted(() => document.addEventListener('click', handleClickOutside))
onUnmounted(() => document.removeEventListener('click', handleClickOutside))
</script>