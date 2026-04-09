<template>
  <header class="sticky top-0 z-50 bg-[#FAFAF7] border-b border-[#EAE5DC] font-garamond">

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-14 md:h-16 gap-3 sm:gap-4">

        <!-- Logo -->
        <router-link to="/" class="flex items-center gap-2 shrink-0">
          <span class="text-xl sm:text-2xl text-[#1C1C1E] leading-none italic font-garamond">
            <span class="text-[#A8896C]">Ylham</span>
          </span>
        </router-link>

        <!-- Search Bar — tablet ve üstü -->
        <div class="flex-1 max-w-sm mx-2 sm:mx-4 hidden sm:block">
          <div class="relative">
            <span class="absolute left-3 top-1/2 -translate-y-1/2 text-[#B0A898]">
              <v-icon size="16" icon="mdi-magnify" />
            </span>
            <input v-model="searchQuery" type="text" placeholder="Goşgy, şahyry gözle..."
              class="w-full pl-9 pr-4 py-2 bg-[#F0EBE1] rounded-full text-sm text-[#1C1C1E] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C] transition-all font-dm text-[13px]"
              @keyup.enter="performSearch" />
          </div>
        </div>

        <!-- Right Actions -->
        <div class="flex items-center justify-center gap-1 sm:gap-2 shrink-0">

          <!-- Mobile arama ikonu -->
          <button class="sm:hidden p-2 flex items-center justify-center rounded-full hover:bg-[#F0EBE1] text-[#6B6B5A] transition-all"
            @click="mobileSearchOpen = !mobileSearchOpen">
            <v-icon size="17" icon="mdi-magnify" />
          </button>

          <!-- Goşgy Yaz -->
          <button @click="routeToPoemCreate"
            class="flex items-center justify-center gap-1.5 p-2 text-[#6B6B5A] hover:text-[#1C1C1E] rounded-full hover:bg-[#F0EBE1] transition-all mr-2 font-dm text-[13px] font-medium">
            <v-icon size="17" icon="mdi-pencil-outline" />
            <span class="hidden md:inline">Ýaz</span>
          </button>

          <!-- Auth -->
          <template v-if="!authStore.isAuthenticated">
            <router-link to="/login"
              class="px-4 py-1.5 bg-[#1C1C1E] text-[#F5F0E8] rounded-full hover:bg-[#3A3A2E] transition-all font-dm text-[12px] font-medium">
              Girmek
            </router-link>
            <router-link to="/register"
              class="hidden sm:block px-4 py-1.5 border border-[#D9D0C4] text-[#1C1C1E] rounded-full hover:border-[#1C1C1E] transition-all font-dm text-[12px] font-medium">
              Hasap aç
            </router-link>
          </template>

          <!--Authenticated -->
          <template v-else>
            <!-- Profil Dropdown -->
          <div class="relative flex profile-dropdown-container">
              <button type="button" @click="toggleDropdown"
                class="w-8 h-8 sm:w-9 sm:h-9 rounded-full overflow-hidden ring-1 ring-[#EAE5DC] hover:ring-[#A8896C] focus:outline-none transition-all duration-200">
                <img :src="authStore.user?.avatar || '/poet_images/default.webp'" alt="Profil"
                  class="w-full h-full object-cover" />
              </button>

              <!-- Dropdown -->
              <Transition enter-active-class="transition-all duration-150 ease-out"
                enter-from-class="opacity-0 scale-95 translate-y-1" enter-to-class="opacity-100 scale-100 translate-y-0"
                leave-active-class="transition-all duration-100 ease-in"
                leave-from-class="opacity-100 scale-100 translate-y-0"
                leave-to-class="opacity-0 scale-95 translate-y-1">
                <div v-if="showDropdown"
                  class="absolute right-0 mt-2.5 w-56 bg-white rounded-2xl shadow-xl border border-[#EAE5DC] overflow-hidden z-50"
                  style="box-shadow: 0 8px 32px rgba(28,28,30,0.10);">

                  <!-- User info -->
                  <div class="px-4 py-4 border-b border-[#F0EBE1] bg-[#FAFAF7]">
                    <router-link to="/dashboard" class="flex items-center gap-3">
                      <img :src="authStore.user?.avatar || '/poet_images/default.webp'"
                        class="w-9 h-9 rounded-full ring-1 ring-[#A8896C] ring-offset-1" />
                      <div class="min-w-0">
                        <p class="text-sm font-medium text-[#1C1C1E] truncate font-dm">
                          {{ authStore.user?.username }}
                        </p>
                        <p class="text-xs text-[#9A9A8A] truncate font-dm">
                          @{{ authStore.user?.username }}</p>
                      </div>
                    </router-link>
                  </div>

                  <!-- Menu Items -->
                  <div class="py-1.5">
                    <router-link v-for="item in dropdownItems" :key="item.to" :to="item.to"
                      class="flex items-center gap-3 px-4 py-2.5 text-[#3A3A2E] hover:bg-[#F5F2EC] transition-colors group font-dm text-[13px]" @click="showDropdown = false">
                      <v-icon size="16" :icon="item.icon"
                        class="text-[#9A9A8A] group-hover:text-[#A8896C] transition-colors shrink-0" />
                      {{ item.label }}
                    </router-link>
                  </div>

                  <!-- Logout -->
                  <div class="px-3 pb-3">
                    <button type="button" @click="signOut"
                      class="flex items-center gap-2 w-full px-4 py-2 text-[#9A9A8A] hover:text-[#C0392B] hover:bg-[#FFF0F0] rounded-xl text-xs transition-all font-dm text-[13px]">
                      <v-icon size="15" icon="mdi-logout" />
                      Hasapdan çykmak
                    </button>
                  </div>
                </div>
              </Transition>
            </div>
          </template>
        </div>
      </div>
    </div>

    <!-- Mobile Search Bar (açılır/kapanır) -->
    <Transition enter-active-class="transition-all duration-200 ease-out" enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-2">
      <div v-if="mobileSearchOpen" class="sm:hidden px-4 pb-3 border-t border-[#EAE5DC] pt-3">
        <div class="relative">
          <span class="absolute left-3 top-1/2 -translate-y-1/2 text-[#B0A898]">
            <v-icon size="16" icon="mdi-magnify" />
          </span>
          <input v-model="searchQuery" type="text" placeholder="Goşgy, şair ara..." autofocus
            class="w-full pl-9 pr-10 py-2.5 bg-[#F0EBE1] rounded-full text-sm text-[#1C1C1E] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C] transition-all"
            style="font-family: 'DM Sans', sans-serif; font-size: 13px;" @keyup.enter="performSearch" />
          <button
            class="absolute right-3 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#1C1C1E] transition-colors"
            @click="mobileSearchOpen = false">
            <v-icon size="16" icon="mdi-close" />
          </button>
        </div>
      </div>
    </Transition>

  </header>
</template>

<script setup>
const router = useRouter()
const authStore = useAuthStore()
const appStore = useAppStore()
const searchQuery = ref('')
const showDropdown = ref(false)
const mobileSearchOpen = ref(false)

const dropdownItems = [
  { to: '/dashboard', label: 'Statistika', icon: 'mdi-view-dashboard-outline' },
  { to: '/dashboard', label: 'Goşgularym', icon: 'mdi-book-open-page-variant-outline' },
  { to: '/dashboard', label: 'Bildirişler', icon: 'mdi-bell-outline' },
  { to: '/dashboard', label: 'Sazlamalar', icon: 'mdi-cog-outline' },
]

const toggleDropdown = () => {
  showDropdown.value = !showDropdown.value
}

const performSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({ path: '/search', query: { q: searchQuery.value } })
    showDropdown.value = false
    mobileSearchOpen.value = false
  }
}

const signOut = () => {
  showDropdown.value = false
  authStore.logout()
}

const routeToPoemCreate = () => {
  if (!authStore.isAuthenticated) {
    appStore.toggleModal('login')
  } else router.push({ name: "PoemCreate" })
}

onMounted(() => {
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.profile-dropdown-container')) {
      showDropdown.value = false
    }
  })
})
</script>