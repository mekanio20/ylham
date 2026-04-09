<template>
  <div class="min-h-screen bg-[#F5F2EC] font-garamond">

    <!-- Mobile Overlay -->
    <div v-if="mobileSidebarOpen" class="fixed inset-0 bg-black/50 z-30 lg:hidden" @click="mobileSidebarOpen = false"></div>

    <div class="flex h-screen overflow-hidden">

      <!-- ══ SIDEBAR desktop ══ -->
      <aside
        :class="['bg-[#1C1C1E] text-[#F5F0E8] flex-col transition-all duration-300 shrink-0 z-40 h-screen sticky top-0 hidden lg:flex', desktopSidebarOpen ? 'lg:w-60' : 'lg:w-16']"
      >
        <!-- Logo -->
        <div class="flex items-center justify-between px-4 py-5 border-b border-[#2E2E30] min-h-[64px]">
          <router-link to="/" v-if="desktopSidebarOpen" class="text-xl leading-none" style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:400;">
            <span class="text-[#A8896C]">Ylham</span>
          </router-link>
          <button @click="desktopSidebarOpen = !desktopSidebarOpen"
            class="p-1.5 rounded-lg hover:bg-[#2E2E30] text-[#9A9A8A] hover:text-[#F5F0E8] transition-all ml-auto shrink-0">
            <v-icon size="18" :icon="desktopSidebarOpen ? 'mdi-chevron-left' : 'mdi-menu'" />
          </button>
        </div>
        <!-- User mini -->
        <div class="px-3 py-4 border-b border-[#2E2E30]">
          <div class="flex items-center gap-3 cursor-pointer" @click="activeSection='profile'">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99" class="w-9 h-9 rounded-full ring-1 ring-[#A8896C] shrink-0" />
            <div v-if="desktopSidebarOpen" class="flex-1 min-w-0">
              <p class="text-sm font-medium text-[#F5F0E8] truncate" style="font-family:'DM Sans',sans-serif;">Leyla Narin</p>
              <p class="text-xs text-[#6B6B6B] truncate" style="font-family:'DM Sans',sans-serif;">@leylanarin</p>
            </div>
          </div>
        </div>
        <!-- Nav -->
        <nav class="flex-1 px-2 py-4 space-y-0.5 overflow-y-auto">
          <button v-for="item in navItems" :key="item.id" @click="activeSection=item.id"
            :class="['w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-150 text-left', activeSection===item.id ? 'bg-[#A8896C] text-[#1C1C1E]' : 'text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8]']">
            <v-icon size="18" :icon="item.icon" class="shrink-0" />
            <span v-if="desktopSidebarOpen" class="text-sm truncate flex-1" style="font-family:'DM Sans',sans-serif;font-weight:500;">{{ item.label }}</span>
            <span v-if="desktopSidebarOpen && item.badge"
              class="ml-auto text-xs px-1.5 py-0.5 rounded-full font-semibold shrink-0"
              :class="activeSection===item.id ? 'bg-[#1C1C1E] text-[#A8896C]' : 'bg-[#A8896C] text-[#1C1C1E]'"
              style="font-family:'DM Sans',sans-serif;">{{ item.badge }}</span>
          </button>
        </nav>
        <!-- Bottom -->
        <div class="px-2 py-4 border-t border-[#2E2E30] space-y-1">
          <button @click="activeSection='settings'"
            :class="['w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all', activeSection==='settings' ? 'bg-[#A8896C] text-[#1C1C1E]' : 'text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8]']">
            <v-icon size="18" icon="mdi-cog-outline" class="shrink-0" />
            <span v-if="desktopSidebarOpen" class="text-sm" style="font-family:'DM Sans',sans-serif;font-weight:500;">Sazlamalar</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8] transition-all">
            <v-icon size="18" icon="mdi-logout" class="shrink-0" />
            <span v-if="desktopSidebarOpen" class="text-sm" style="font-family:'DM Sans',sans-serif;font-weight:500;">Hasapdan çykmak</span>
          </button>
        </div>
      </aside>

      <!-- ══ SIDEBAR mobile drawer ══ -->
      <aside :class="['fixed top-0 left-0 h-full bg-[#1C1C1E] text-[#F5F0E8] flex flex-col z-40 w-72 transition-transform duration-300 lg:hidden', mobileSidebarOpen ? 'translate-x-0' : '-translate-x-full']">
        <div class="flex items-center justify-between px-4 py-5 border-b border-[#2E2E30]">
          <router-link to="/" class="text-xl leading-none" style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:400;">
            <span class="text-[#A8896C]">Ylham</span>
          </router-link>
          <button @click="mobileSidebarOpen=false" class="p-1.5 rounded-lg hover:bg-[#2E2E30] text-[#9A9A8A] hover:text-[#F5F0E8] transition-all">
            <v-icon size="18" icon="mdi-close" />
          </button>
        </div>
        <div class="px-3 py-4 border-b border-[#2E2E30]">
          <div class="flex items-center gap-3 cursor-pointer" @click="activeSection='profile'; mobileSidebarOpen=false">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99" class="w-9 h-9 rounded-full ring-1 ring-[#A8896C] shrink-0" />
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-[#F5F0E8] truncate" style="font-family:'DM Sans',sans-serif;">Leyla Narin</p>
              <p class="text-xs text-[#6B6B6B]" style="font-family:'DM Sans',sans-serif;">@leylanarin</p>
            </div>
          </div>
        </div>
        <nav class="flex-1 px-2 py-4 space-y-0.5 overflow-y-auto">
          <button v-for="item in navItems" :key="item.id" @click="activeSection=item.id; mobileSidebarOpen=false"
            :class="['w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all text-left', activeSection===item.id ? 'bg-[#A8896C] text-[#1C1C1E]' : 'text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8]']">
            <v-icon size="18" :icon="item.icon" class="shrink-0" />
            <span class="text-sm flex-1" style="font-family:'DM Sans',sans-serif;font-weight:500;">{{ item.label }}</span>
            <span v-if="item.badge" class="text-xs px-1.5 py-0.5 rounded-full font-semibold bg-[#A8896C] text-[#1C1C1E]"
              style="font-family:'DM Sans',sans-serif;">{{ item.badge }}</span>
          </button>
        </nav>
        <div class="px-2 py-4 border-t border-[#2E2E30] space-y-0.5">
          <button @click="activeSection='settings'; mobileSidebarOpen=false"
            :class="['w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all', activeSection==='settings' ? 'bg-[#A8896C] text-[#1C1C1E]' : 'text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8]']">
            <v-icon size="18" icon="mdi-cog-outline" />
            <span class="text-sm" style="font-family:'DM Sans',sans-serif;font-weight:500;">Sazlamalar</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-[#8A8A8A] hover:bg-[#2E2E30] hover:text-[#F5F0E8] transition-all">
            <v-icon size="18" icon="mdi-logout" />
            <span class="text-sm" style="font-family:'DM Sans',sans-serif;font-weight:500;">Çıkış</span>
          </button>
        </div>
      </aside>

      <!-- ══ MAIN ══ -->
      <div class="flex-1 min-w-0 flex flex-col overflow-hidden">

        <!-- Top Bar -->
        <header class="sticky top-0 z-20 bg-[#F5F2EC] border-b border-[#E5DFD5] px-4 sm:px-6 py-3.5 flex items-center gap-3 shrink-0">
          <button @click="mobileSidebarOpen=true" class="lg:hidden p-2 -ml-1 rounded-lg hover:bg-[#EDE8E0] text-[#6B6B5A] transition-all">
            <v-icon size="20" icon="mdi-menu" />
          </button>
          <div class="min-w-0 flex-1">
            <h1 class="text-lg sm:text-2xl text-[#1C1C1E] leading-none truncate" style="font-family:'Cormorant Garamond',serif;font-weight:400;">
              {{ currentSection.title }}
            </h1>
            <p class="text-xs text-[#9A9A8A] mt-0.5 hidden sm:block" style="font-family:'DM Sans',sans-serif;">{{ currentSection.subtitle }}</p>
          </div>
          <router-link to="/" class="text-[#A8896C] hover:underline">
            <v-icon size="25" icon="mdi-home" />
          </router-link>
        </header>

        <!-- Scrollable page content -->
        <main class="flex-1 overflow-y-auto pb-20 lg:pb-6">

          <!-- ─── OVERVIEW ─── -->
          <div v-if="activeSection==='overview'" class="p-4 sm:p-6 space-y-5 sm:space-y-6">
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
              <div v-for="stat in stats" :key="stat.label" class="bg-white rounded-2xl p-4 sm:p-5 border border-[#EAE5DC] hover:shadow-md transition-shadow">
                <div class="flex items-start justify-between mb-3">
                  <div class="w-8 h-8 sm:w-10 sm:h-10 rounded-xl flex items-center justify-center" :class="stat.iconBg">
                    <v-icon size="16" :icon="stat.icon" :class="stat.iconColor" />
                  </div>
                </div>
                <p class="text-2xl sm:text-3xl font-light text-[#1C1C1E] mb-0.5 font-dm">{{ stat.value }}</p>
                <p class="text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">{{ stat.label }}</p>
              </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6">
              <div class="lg:col-span-2 bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden">
                <div class="flex items-center justify-between px-4 sm:px-6 py-4 border-b border-[#EAE5DC]">
                  <h2 class="text-base text-[#1C1C1E]">Soňky Goşgularym</h2>
                  <button @click="activeSection='poems'" class="text-xs text-[#A8896C] hover:underline font-dm">Ählisini gör</button>
                </div>
                <div class="divide-y divide-[#F0EBE1]">
                  <div v-for="poem in myPoems.slice(0,4)" :key="poem.id"
                    class="flex items-center gap-3 px-4 sm:px-6 py-3.5 hover:bg-[#FAFAF7] transition-colors">
                    <div class="w-7 h-7 rounded-lg bg-[#F0EBE1] flex items-center justify-center text-[#C8B89A] shrink-0 text-lg"
                      style="font-family:'Cormorant Garamond',serif;font-style:italic;">"</div>
                    <div class="flex-1 min-w-0">
                      <p class="text-sm text-[#1C1C1E] truncate" style="font-family:'Cormorant Garamond',serif;font-size:15px;">{{ poem.title }}</p>
                      <p class="text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">{{ poem.date }}</p>
                    </div>
                    <div class="flex items-center gap-2 sm:gap-3 text-xs text-[#9A9A8A] shrink-0" style="font-family:'DM Sans',sans-serif;">
                      <span class="hidden sm:flex items-center gap-1"><v-icon size="12" icon="mdi-heart-outline"/>{{ poem.likes }}</span>
                      <span class="hidden sm:flex items-center gap-1"><v-icon size="12" icon="mdi-comment-outline"/>{{ poem.comments }}</span>
                      <span :class="poem.status==='Yayında'?'text-[#2E7D32] bg-[#E8F5E9]':'text-[#E65100] bg-[#FFF3E0]'"
                        class="px-2 py-0.5 rounded-full" style="font-size:10px;">{{ poem.status }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden">
                <div class="px-4 sm:px-6 py-4 border-b border-[#EAE5DC]">
                  <h2 class="text-base text-[#1C1C1E]">Bu Hepde</h2>
                </div>
                <div class="p-4 sm:p-6 space-y-4">
                  <div v-for="act in weekActivity" :key="act.label" class="flex items-center gap-3">
                    <div class="w-7 h-7 rounded-full flex items-center justify-center shrink-0" :class="act.bg">
                      <v-icon size="14" :icon="act.icon" :class="act.color" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="text-xs text-[#1C1C1E] mb-1" style="font-family:'DM Sans',sans-serif;">{{ act.label }}</p>
                      <div class="h-1.5 bg-[#F0EBE1] rounded-full overflow-hidden">
                        <div class="h-full rounded-full" :class="act.barColor" :style="`width:${act.pct}%`"></div>
                      </div>
                    </div>
                    <span class="text-sm font-medium text-[#1C1C1E] shrink-0" style="font-family:'DM Sans',sans-serif;">{{ act.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ─── POEMS ─── -->
          <div v-if="activeSection==='poems'" class="p-4 sm:p-6">
            <div class="flex items-center gap-2 mb-4 flex-wrap">
              <button v-for="f in ['Tümü','Yayında','Taslak','Arşiv']" :key="f" @click="poemFilter=f"
                :class="['px-3 py-1.5 rounded-full text-xs border transition-all', poemFilter===f?'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]':'border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E]']"
                style="font-family:'DM Sans',sans-serif;">{{ f }}</button>
            </div>
            <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden">
              <div class="divide-y divide-[#F0EBE1]">
                <div v-for="poem in filteredMyPoems" :key="poem.id"
                  class="flex items-center gap-3 px-4 sm:px-6 py-4 hover:bg-[#FAFAF7] transition-colors group">
                  <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center text-[#C8B89A] shrink-0 text-xl"
                    style="font-family:'Cormorant Garamond',serif;font-style:italic;">"</div>
                  <div class="flex-1 min-w-0">
                    <p class="text-sm sm:text-base text-[#1C1C1E] truncate" style="font-family:'Cormorant Garamond',serif;font-size:16px;">{{ poem.title }}</p>
                    <p class="text-xs text-[#9A9A8A] mt-0.5" style="font-family:'DM Sans',sans-serif;">{{ poem.category }} · {{ poem.date }}</p>
                  </div>
                  <div class="hidden md:flex items-center gap-3 text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">
                    <span class="flex items-center gap-1"><v-icon size="13" icon="mdi-eye-outline"/>{{ poem.views }}</span>
                    <span class="flex items-center gap-1"><v-icon size="13" icon="mdi-heart-outline"/>{{ poem.likes }}</span>
                    <span class="flex items-center gap-1"><v-icon size="13" icon="mdi-comment-outline"/>{{ poem.comments }}</span>
                  </div>
                  <span :class="poem.status==='Yayında'?'text-[#2E7D32] bg-[#E8F5E9]':poem.status==='Taslak'?'text-[#B8860B] bg-[#FFF8E1]':'text-[#9A9A8A] bg-[#F0EBE1]'"
                    class="px-2 py-0.5 rounded-full text-xs shrink-0" style="font-family:'DM Sans',sans-serif;font-size:10px;">{{ poem.status }}</span>
                  <div class="flex items-center gap-0.5 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                    <button class="p-1.5 rounded-lg hover:bg-[#F0EBE1] text-[#9A9A8A] hover:text-[#1C1C1E] transition-all"><v-icon size="15" icon="mdi-pencil-outline"/></button>
                    <button class="p-1.5 rounded-lg hover:bg-[#FFF0F0] text-[#9A9A8A] hover:text-[#C0392B] transition-all"><v-icon size="15" icon="mdi-trash-can-outline"/></button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ─── NOTIFICATIONS ─── -->
          <div v-if="activeSection==='notifications'" class="p-4 sm:p-6">
            <div class="overflow-x-auto no-scrollbar pb-1 mb-4">
              <div class="flex items-center gap-2 min-w-max no-scrollbar">
                <button v-for="f in notifFilters" :key="f.id" @click="notifFilter=f.id"
                  :class="['flex items-center gap-1 px-3 py-1.5 rounded-full text-xs border transition-all whitespace-nowrap', notifFilter===f.id?'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]':'border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E]']"
                  style="font-family:'DM Sans',sans-serif;">
                  <v-icon size="12" :icon="f.icon"/>{{ f.label }}
                  <span v-if="f.count" class="w-4 h-4 rounded-full bg-[#A8896C] text-[#1C1C1E] flex items-center justify-center font-bold" style="font-size:9px;">{{ f.count }}</span>
                </button>
                <button @click="markAllRead" class="ml-2 text-xs text-[#A8896C] hover:underline whitespace-nowrap" style="font-family:'DM Sans',sans-serif;">Tümünü okundu say</button>
              </div>
            </div>
            <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden">
              <div class="divide-y divide-[#F0EBE1]">
                <div v-for="notif in filteredNotifs" :key="notif.id"
                  :class="['flex items-start gap-3 px-4 sm:px-6 py-4 cursor-pointer transition-colors', !notif.read?'bg-[#FDFCF9]':'hover:bg-[#FAFAF7]']"
                  @click="notif.read=true">
                  <div class="relative shrink-0">
                    <img :src="notif.avatar" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full"/>
                    <div class="absolute -bottom-0.5 -right-0.5 w-4 h-4 sm:w-5 sm:h-5 rounded-full flex items-center justify-center" :class="notif.typeBg">
                      <v-icon size="10" :icon="notif.typeIcon" :class="notif.typeColor"/>
                    </div>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="text-sm text-[#1C1C1E] leading-snug" style="font-family:'DM Sans',sans-serif;">
                      <span class="font-semibold">{{ notif.user }}</span>
                      {{ notif.action }}
                      <span v-if="notif.poem" class="text-[#A8896C] italic" style="font-family:'Cormorant Garamond',serif;font-size:15px;"> {{ notif.poem }}</span>
                    </p>
                    <p v-if="notif.preview" class="text-xs text-[#9A9A8A] mt-0.5 italic line-clamp-1" style="font-family:'Cormorant Garamond',serif;font-size:13px;">"{{ notif.preview }}"</p>
                    <p class="text-xs text-[#B0A898] mt-1" style="font-family:'DM Sans',sans-serif;">{{ notif.time }}</p>
                  </div>
                  <div v-if="!notif.read" class="w-2 h-2 rounded-full bg-[#A8896C] shrink-0 mt-2"></div>
                </div>
                <div v-if="filteredNotifs.length===0" class="py-14 text-center">
                  <v-icon size="36" icon="mdi-bell-sleep-outline" class="text-[#D9D0C4] mb-2"/>
                  <p class="text-sm text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">Bildirim yok</p>
                </div>
              </div>
            </div>
          </div>

          <!-- ─── COMMENTS ─── -->
          <div v-if="activeSection==='comments'" class="p-4 sm:p-6">
            <div class="overflow-x-auto no-scrollbar pb-1 mb-4">
              <div class="flex items-center gap-2 min-w-max">
                <button v-for="f in commentFilters" :key="f.id" @click="commentFilter=f.id"
                  :class="['flex items-center gap-1 px-3 py-1.5 rounded-full text-xs border transition-all whitespace-nowrap', commentFilter===f.id?'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]':'border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E]']"
                  style="font-family:'DM Sans',sans-serif;">
                  <v-icon size="12" :icon="f.icon"/>{{ f.label }}
                  <span v-if="f.count" class="px-1.5 py-0.5 rounded-full bg-[#EDE8E0] text-[#6B5E4E] font-semibold" style="font-size:9px;">{{ f.count }}</span>
                </button>
              </div>
            </div>
            <div class="space-y-3">
              <div v-for="c in filteredComments" :key="c.id" class="bg-white rounded-2xl border border-[#EAE5DC] p-4 sm:p-5">
                <div class="flex items-center gap-2 mb-3 pb-3 border-b border-[#F0EBE1]">
                  <v-icon size="13" icon="mdi-book-open-variant-outline" class="text-[#A8896C] shrink-0"/>
                  <span class="text-xs text-[#A8896C] italic truncate flex-1" style="font-family:'Cormorant Garamond',serif;font-size:13px;">{{ c.poem }}</span>
                  <span class="ml-auto flex items-center gap-1 text-xs shrink-0"
                    :class="c.status==='okunmadı'?'text-[#A8896C]':c.status==='cevaplandı'?'text-[#2E7D32]':c.status==='beğenildi'?'text-[#C0392B]':'text-[#9A9A8A]'"
                    style="font-family:'DM Sans',sans-serif;font-size:10px;">
                    <v-icon size="11" :icon="commentStatusIcon(c.status)"/>{{ commentStatusLabel(c.status) }}
                  </span>
                </div>
                <div class="flex items-start gap-3">
                  <img :src="c.avatar" class="w-8 h-8 sm:w-9 sm:h-9 rounded-full ring-1 ring-[#E0D9CE] shrink-0"/>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2 mb-1.5">
                      <span class="text-sm font-semibold text-[#1C1C1E]" style="font-family:'DM Sans',sans-serif;">{{ c.author }}</span>
                      <span class="text-xs text-[#B0A898]" style="font-family:'DM Sans',sans-serif;">· {{ c.time }}</span>
                    </div>
                    <p class="text-[#3A3020] leading-relaxed mb-3" style="font-family:'Cormorant Garamond',serif;font-size:15px;">{{ c.text }}</p>
                    <div v-if="c.reply" class="ml-3 pl-3 border-l-2 border-[#A8896C] mb-3">
                      <p class="text-xs text-[#A8896C] mb-0.5 font-semibold" style="font-family:'DM Sans',sans-serif;">Sen cevapladın:</p>
                      <p class="text-sm text-[#5A5040] italic" style="font-family:'Cormorant Garamond',serif;font-size:14px;">{{ c.reply }}</p>
                    </div>
                    <div class="flex items-center gap-3">
                      <button class="flex items-center gap-1 text-xs text-[#9A9A8A] hover:text-[#C0392B] transition-colors" style="font-family:'DM Sans',sans-serif;">
                        <v-icon size="13" icon="mdi-heart-outline"/>{{ c.likes }}
                      </button>
                      <button v-if="!c.reply" @click="c.replying=!c.replying"
                        class="flex items-center gap-1 text-xs text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors" style="font-family:'DM Sans',sans-serif;">
                        <v-icon size="13" icon="mdi-reply-outline"/>Yanıtla
                      </button>
                      <button class="flex items-center gap-1 text-xs text-[#9A9A8A] hover:text-[#C0392B] transition-colors ml-auto" style="font-family:'DM Sans',sans-serif;">
                        <v-icon size="13" icon="mdi-flag-outline"/>Şikayet
                      </button>
                    </div>
                    <div v-if="c.replying" class="mt-3 flex gap-2">
                      <input v-model="c.replyInput" type="text" placeholder="Yanıtını yaz..."
                        class="flex-1 min-w-0 px-3 py-2 bg-[#F0EBE1] rounded-lg text-sm text-[#2A2418] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C]"
                        style="font-family:'Cormorant Garamond',serif;font-size:14px;"/>
                      <button @click="sendReply(c)"
                        class="px-3 py-2 bg-[#1C1C1E] text-[#F5F0E8] rounded-lg text-xs hover:bg-[#3A3A2E] transition-all shrink-0"
                        style="font-family:'DM Sans',sans-serif;">Gönder</button>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="filteredComments.length===0" class="bg-white rounded-2xl border border-[#EAE5DC] py-14 text-center">
                <v-icon size="36" icon="mdi-comment-off-outline" class="text-[#D9D0C4] mb-2"/>
                <p class="text-sm text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">Bu kategoride yorum yok</p>
              </div>
            </div>
          </div>

          <!-- ─── PROFILE ─── -->
          <div v-if="activeSection==='profile'" class="p-4 sm:p-6 max-w-3xl">
            <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden mb-4 sm:mb-5">
              <div class="h-24 sm:h-32 bg-gradient-to-r from-[#1C1C1E] via-[#3A3020] to-[#2A2010] relative">
              </div>
              <div class="px-4 sm:px-6 pb-5">
                <div class="flex items-end gap-3 -mt-7 sm:-mt-8 mb-4">
                  <div class="relative shrink-0">
                    <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99" class="w-14 h-14 sm:w-20 sm:h-20 rounded-full ring-4 ring-white bg-[#F0EBE1]"/>
                    <button class="absolute bottom-0 right-0 w-6 h-6 bg-[#1C1C1E] text-white rounded-full flex items-center justify-center hover:bg-[#3A3A2E] transition-all">
                      <v-icon size="12" icon="mdi-camera-outline"/>
                    </button>
                  </div>
                  <div class="flex-1 min-w-0 mb-1 pt-8">
                    <h2 class="text-lg sm:text-2xl text-[#1C1C1E] truncate" style="font-family:'Cormorant Garamond',serif;font-weight:400;">Leyla Narin</h2>
                    <p class="text-xs sm:text-sm text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">@leylanarin</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5" style="font-family:'DM Sans',sans-serif;">Ad Soyad</label>
                      <input v-model="profileForm.name" type="text" class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C]" style="font-family:'DM Sans',sans-serif;"/>
                    </div>
                    <div>
                      <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5" style="font-family:'DM Sans',sans-serif;">Kullanıcı Adı</label>
                      <input v-model="profileForm.username" type="text" class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C]" style="font-family:'DM Sans',sans-serif;"/>
                    </div>
                  </div>
                  <div>
                    <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5" style="font-family:'DM Sans',sans-serif;">Biyografi</label>
                    <textarea v-model="profileForm.bio" rows="3" class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] resize-none" style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:15px;"></textarea>
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5" style="font-family:'DM Sans',sans-serif;">Konum</label>
                      <input v-model="profileForm.location" type="text" class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C]" style="font-family:'DM Sans',sans-serif;"/>
                    </div>
                    <div>
                      <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5" style="font-family:'DM Sans',sans-serif;">Website</label>
                      <input v-model="profileForm.website" type="text" class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C]" style="font-family:'DM Sans',sans-serif;"/>
                    </div>
                  </div>
                  <div class="flex justify-end gap-2 pt-1">
                    <button @click="saveProfile" class="px-4 py-1.5 bg-[#1C1C1E] text-[#F5F0E8] rounded-full text-xs hover:bg-[#3A3A2E] transition-all" style="font-family:'DM Sans',sans-serif;">Kaydet</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ─── SETTINGS ─── -->
          <div v-if="activeSection==='settings'" class="p-4 sm:p-6 max-w-2xl space-y-4">
            <div v-for="section in settingsSections" :key="section.title" class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden">
              <div class="px-4 sm:px-6 py-4 border-b border-[#F0EBE1] flex items-center gap-2">
                <v-icon size="16" :icon="section.icon" class="text-[#A8896C]"/>
                <h2 class="text-base text-[#1C1C1E]" style="font-family:'Cormorant Garamond',serif;font-weight:500;">{{ section.title }}</h2>
              </div>
              <div class="divide-y divide-[#F9F6F2]">
                <div v-for="item in section.items" :key="item.id" class="px-4 sm:px-6 py-3.5 flex items-center gap-3">
                  <div class="flex-1 min-w-0">
                    <p class="text-sm text-[#1C1C1E]" style="font-family:'DM Sans',sans-serif;font-weight:500;">{{ item.label }}</p>
                    <p class="text-xs text-[#9A9A8A] mt-0.5 hidden sm:block" style="font-family:'DM Sans',sans-serif;">{{ item.desc }}</p>
                  </div>
                  <button v-if="item.type==='toggle'" @click="item.value=!item.value"
                    :class="['w-11 h-6 rounded-full transition-all duration-300 relative shrink-0', item.value?'bg-[#1C1C1E]':'bg-[#D9D0C4]']">
                    <span :class="['absolute top-1 w-4 h-4 bg-white rounded-full shadow transition-all duration-300', item.value?'left-6':'left-1']"></span>
                  </button>
                  <select v-else-if="item.type==='select'" v-model="item.value"
                    class="px-2 py-1.5 bg-[#F0EBE1] rounded-lg text-xs text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] shrink-0 max-w-[110px]"
                    style="font-family:'DM Sans',sans-serif;">
                    <option v-for="opt in item.options" :key="opt" :value="opt">{{ opt }}</option>
                  </select>
                  <button v-else-if="item.type==='button'"
                    :class="['px-3 py-1.5 rounded-full text-xs shrink-0 transition-all', item.danger?'border border-[#C0392B] text-[#C0392B] hover:bg-[#C0392B] hover:text-white':'border border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E] hover:text-[#1C1C1E]']"
                    style="font-family:'DM Sans',sans-serif;font-size:11px;">{{ item.btnLabel }}</button>
                </div>
              </div>
            </div>
          </div>

        </main>
      </div>
    </div>

    <!-- ══ MOBILE BOTTOM NAV ══ -->
    <nav class="fixed bottom-0 left-0 right-0 bg-[#1C1C1E] border-t border-[#2E2E30] flex items-center lg:hidden z-30 safe-area-pb">
      <button v-for="item in mobileNavItems" :key="item.id" @click="activeSection=item.id"
        :class="['flex-1 flex flex-col items-center gap-0.5 py-2.5 relative transition-colors', activeSection===item.id?'text-[#A8896C]':'text-[#6B6B6B]']">
        <v-icon size="22" :icon="item.icon"/>
        <span style="font-family:'DM Sans',sans-serif;font-size:9px;letter-spacing:0.04em;">{{ item.label }}</span>
        <span v-if="item.badge"
          class="absolute top-1.5 left-1/2 ml-2 w-4 h-4 bg-[#C0392B] text-white rounded-full flex items-center justify-center font-bold"
          style="font-size:8px;">{{ item.badge }}</span>
      </button>
    </nav>

  </div>
</template>

<script setup>
const mobileSidebarOpen = ref(false)
const desktopSidebarOpen = ref(true)
const activeSection = ref('overview')
const poemFilter = ref('Tümü')
const notifFilter = ref('all')
const commentFilter = ref('all')

const mobileNavItems = [
  { id:'overview',      label:'Statistika',      icon:'mdi-view-dashboard-outline' },
  { id:'poems',         label:'Goşgularym', icon:'mdi-book-open-page-variant-outline' },
  { id:'notifications', label:'Bildirişler',  icon:'mdi-bell-outline',            badge:4 },
  { id:'comments',      label:'Teswirler',  icon:'mdi-comment-multiple-outline', badge:7 },
]

const navItems = ref([
  { id:'overview',      label:'Statistika', icon:'mdi-view-dashboard-outline' },
  { id:'poems',         label:'Goşgularym',   icon:'mdi-book-open-page-variant-outline' },
  { id:'notifications', label:'Bildirişler', icon:'mdi-bell-outline',            badge:4 },
  { id:'comments',      label:'Teswirler',    icon:'mdi-comment-multiple-outline', badge:7 },
])

const sectionMeta = {
  overview:      { title:'Statistika',  subtitle:'Statistiki maglumatlar' },
  poems:         { title:'Goşgularym',    subtitle:'Tüm Goşgylerinizi yönetin' },
  notifications: { title:'Bildirişler', subtitle:'Son etkileşimleriniz' },
  comments:      { title:'Teswirler',    subtitle:'Goşgylerinize gelen teswirler' },
  settings:      { title:'Sazlamalar',     subtitle:'Hesap ve uygulama tercihleri' },
  profile:      { title:'Profil',      subtitle:'Kişisel bilgilerinizi düzenleyin' },
}
const currentSection = computed(() => sectionMeta[activeSection.value] || { title:'', subtitle:'' })

const stats = ref([
  { label:'Jemi Goşgular',   value:'43',   trend:12, icon:'mdi-book-open-variant-outline', iconBg:'bg-[#F0EBE1]', iconColor:'text-[#A8896C]' },
  { label:'Jemi Halananlar', value:'1.2K', trend:8,  icon:'mdi-heart-outline',             iconBg:'bg-[#FFF0F0]', iconColor:'text-[#C0392B]' },
  { label:'Yzarlaýanlar',       value:'384',  trend:5,  icon:'mdi-account-group-outline',     iconBg:'bg-[#E8F5E9]', iconColor:'text-[#2E7D32]' },
  { label:'Jemi okalan',  value:'8.4K', trend:-2, icon:'mdi-eye-outline',              iconBg:'bg-[#EDE7F6]', iconColor:'text-[#5E35B1]' },
])

const weekActivity = ref([
  { label:'Beğeni', value:128, pct:80, icon:'mdi-heart-outline',        bg:'bg-[#FFF0F0]', color:'text-[#C0392B]', barColor:'bg-[#C0392B]' },
  { label:'Yorum',  value:34,  pct:45, icon:'mdi-comment-outline',      bg:'bg-[#EDE7F6]', color:'text-[#5E35B1]', barColor:'bg-[#5E35B1]' },
  { label:'Kaydet', value:56,  pct:60, icon:'mdi-bookmark-outline',     bg:'bg-[#F0EBE1]', color:'text-[#A8896C]', barColor:'bg-[#A8896C]' },
  { label:'Takip',  value:12,  pct:30, icon:'mdi-account-plus-outline', bg:'bg-[#E8F5E9]', color:'text-[#2E7D32]', barColor:'bg-[#2E7D32]' },
])

const myPoems = ref([
  { id:1, title:'Gece Yarısı Şehri',    category:'Şehir',     date:'8 Mar',  views:420, likes:248, comments:34, status:'Yayında' },
  { id:2, title:'Sonbaharda Kaybolmak', category:'Aşk',       date:'5 Mar',  views:310, likes:189, comments:21, status:'Yayında' },
  { id:3, title:'Hafıza Kırıkları',     category:'İç Dünya',  date:'1 Mar',  views:290, likes:201, comments:45, status:'Yayında' },
  { id:4, title:'Beyaz Sessizlik',      category:'Doğa',      date:'25 Şub', views:180, likes:94,  comments:12, status:'Taslak'  },
  { id:5, title:'Kıyıda Bekleyiş',      category:'Melankoli', date:'20 Şub', views:0,   likes:0,   comments:0,  status:'Taslak'  },
  { id:6, title:'İlk Kar',              category:'Doğa',      date:'10 Oca', views:88,  likes:43,  comments:6,  status:'Arşiv'   },
])
const filteredMyPoems = computed(() => poemFilter.value==='Tümü' ? myPoems.value : myPoems.value.filter(p => p.status===poemFilter.value))

const notifFilters = ref([
  { id:'all',      label:'Tümü',    icon:'mdi-all-inclusive',       count:4 },
  { id:'unread',   label:'Okunmadı',icon:'mdi-circle-medium',       count:4 },
  { id:'likes',    label:'Beğeni',  icon:'mdi-heart-outline' },
  { id:'comments', label:'Yorum',   icon:'mdi-comment-outline' },
  { id:'follows',  label:'Takip',   icon:'mdi-account-plus-outline' },
])

const notifications = ref([
  { id:1, user:'Mete Aydın',  action:'Goşgyini beğendi:',           poem:'Gece Yarısı Şehri',    time:'2 saat önce', read:false, type:'like',    typeIcon:'mdi-heart',        typeBg:'bg-[#FFF0F0]', typeColor:'text-[#C0392B]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=mete1'   },
  { id:2, user:'Selin Çelik', action:'yorum yaptı:',               poem:'Hafıza Kırıkları',     time:'3 saat önce', read:false, type:'comment', preview:'Son iki dize beni derinden sarstı.', typeIcon:'mdi-comment',      typeBg:'bg-[#EDE7F6]', typeColor:'text-[#5E35B1]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=selin2'  },
  { id:3, user:'Can Demirci', action:'seni takip etmeye başladı.', poem:'',                     time:'5 saat önce', read:false, type:'follow',  typeIcon:'mdi-account-plus', typeBg:'bg-[#E8F5E9]', typeColor:'text-[#2E7D32]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=can3'    },
  { id:4, user:'Naz Kaya',    action:'Goşgyini kaydetti:',          poem:'Sonbaharda Kaybolmak', time:'1 gün önce',  read:false, type:'save',    typeIcon:'mdi-bookmark',     typeBg:'bg-[#F0EBE1]', typeColor:'text-[#A8896C]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=naz4'    },
  { id:5, user:'Ali Kara',    action:'Goşgyini beğendi:',           poem:'Beyaz Sessizlik',      time:'2 gün önce',  read:true,  type:'like',    typeIcon:'mdi-heart',        typeBg:'bg-[#FFF0F0]', typeColor:'text-[#C0392B]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=ali5'    },
  { id:6, user:'Zeynep Öz',   action:'yorum yaptı:',               poem:'Gece Yarısı Şehri',    time:'3 gün önce',  read:true,  type:'comment', preview:'Tramvay imgesi mükemmel.', typeIcon:'mdi-comment',      typeBg:'bg-[#EDE7F6]', typeColor:'text-[#5E35B1]', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=zeynep6' },
])

const filteredNotifs = computed(() => {
  if (notifFilter.value==='all')     return notifications.value
  if (notifFilter.value==='unread')  return notifications.value.filter(n => !n.read)
  if (notifFilter.value==='likes')   return notifications.value.filter(n => n.type==='like')
  if (notifFilter.value==='comments')return notifications.value.filter(n => n.type==='comment')
  if (notifFilter.value==='follows') return notifications.value.filter(n => n.type==='follow')
  return notifications.value
})
const markAllRead = () => notifications.value.forEach(n => n.read=true)

const commentFilters = ref([
  { id:'all',        label:'Tümü',       icon:'mdi-comment-multiple-outline', count:7 },
  { id:'okunmadı',   label:'Okunmadı',   icon:'mdi-circle-medium',            count:3 },
  { id:'okundu',     label:'Okundu',     icon:'mdi-check' },
  { id:'cevaplandı', label:'Cevaplandı', icon:'mdi-reply-outline' },
  { id:'beğenildi',  label:'Beğenildi',  icon:'mdi-heart-outline' },
])

const comments = ref([
  { id:1, author:'Mete Aydın',  poem:'Gece Yarısı Şehri',   text:'Son iki dize beni derinden sarstı. "Yalnız ben sönerim bazen" — nadir görülen bir kapanış.', time:'2 saat önce', likes:14, status:'okunmadı',   reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=mete1'   },
  { id:2, author:'Selin Çelik', poem:'Hafıza Kırıkları',     text:'Tramvay imgesi mükemmel. Şehrin anonim kalabalığını o kadar güzel yakalamışsın ki.',          time:'5 saat önce', likes:8,  status:'okunmadı',   reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=selin2'  },
  { id:3, author:'Can Demirci', poem:'Sonbaharda Kaybolmak', text:'Okuduğumda İstanbul\'un o sisli sabahlarını hissettim.',                                        time:'1 gün önce',  likes:22, status:'cevaplandı', reply:'Çok teşekkür ederim, o sabahları yaşatabildiysem ne mutlu bana.', replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=can3'    },
  { id:4, author:'Naz Kaya',    poem:'Gece Yarısı Şehri',   text:'Gerçekten içimi ısıttı. Devam et lütfen!',                                                      time:'2 gün önce',  likes:5,  status:'beğenildi',  reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=naz4'    },
  { id:5, author:'Ali Kara',    poem:'Beyaz Sessizlik',      text:'Bu Goşgyi bir anda bitirdim, bırakamadım.',                                                       time:'3 gün önce',  likes:11, status:'okundu',     reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=ali5'    },
  { id:6, author:'Zeynep Öz',   poem:'Kıyıda Bekleyiş',     text:'Melankoli ve umut arasındaki o ince çizgiyi yakalamışsın.',                                      time:'4 gün önce',  likes:18, status:'okundu',     reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=zeynep6' },
  { id:7, author:'Cem Yılmaz',  poem:'İlk Kar',              text:'Kısa ama derinden.',                                                                              time:'5 gün önce',  likes:3,  status:'okunmadı',   reply:null,  replying:false, replyInput:'', avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=cem7'    },
])

const filteredComments = computed(() => commentFilter.value==='all' ? comments.value : comments.value.filter(c => c.status===commentFilter.value))
const commentStatusIcon  = s => ({ 'okunmadı':'mdi-circle-medium','okundu':'mdi-check-circle-outline','cevaplandı':'mdi-reply-circle-outline','beğenildi':'mdi-heart-outline' }[s]||'mdi-circle-medium')
const commentStatusLabel = s => ({ 'okunmadı':'Okunmadı','okundu':'Okundu','cevaplandı':'Cevaplandı','beğenildi':'Beğenildi' }[s]||s)
const sendReply = (c) => {
  if (!c.replyInput.trim()) return
  c.reply=c.replyInput.trim(); c.status='cevaplandı'; c.replying=false; c.replyInput=''
}

const profileForm = ref({ name:'Leyla Narin', username:'leylanarin', bio:'Kelimeler ruhun bıraktığı izlerdir. İstanbul gecelerinde Goşgy yazarım.', location:'İstanbul, Türkiye', website:'leylanarin.com' })
const settingsSections = ref([
  {
    title:'Hasap', icon:'mdi-account-cog-outline',
    items:[
      { id:'email',    label:'E-poçta',       desc:'example@gmail.com',           type:'button', btnLabel:'Üýtget' },
      { id:'password', label:'Parol',         desc:'••••••••', type:'button', btnLabel:'Üýtget' },
    ]
  },
  {
    title:'Bildirişler', icon:'mdi-bell-cog-outline',
    items:[
      { id:'notif_like',    label:'Halanlar',       desc:'Goşgy halananda',     type:'toggle', value:true  },
      { id:'notif_comment', label:'Teswirler',         desc:'Teswir gelende',          type:'toggle', value:true  },
      { id:'notif_follow',  label:'Yzarlaýanlar',         desc:'Biri yzarlanda', type:'toggle', value:true  },
    ]
  },
  {
    title:'Gizlinlik', icon:'mdi-shield-lock-outline',
    items:[
      { id:'private',    label:'Gizlin hasap',        desc:'Diňe yzarlaýanlar görüp biler', type:'toggle', value:false },
    ]
  },
  {
    title:'Tema', icon:'mdi-palette-outline',
    items:[
      { id:'theme',    label:'Tema',        desc:'Platformanyň temasy',  type:'select', value:'Açyk',      options:['Açyk','Garaňky','Awto'] },
      { id:'fontsize', label:'Font ölçegi', desc:'Goşgynyň fondunyň ölçegi',   type:'select', value:'Orta',      options:['Kiçi','Orta','Uly'] },
      { id:'font',     label:'Goşgynuň fonty',  desc:'Goşgynyň fontlary', type:'select', value:'Cormorant', options:['Cormorant','Georgia','Palatino'] },
    ]
  },
  {
    title:'Howply bölüm', icon:'mdi-alert-outline',
    items:[
      { id:'delete', label:'Hasabyňyzy pozuň',          desc:'Bu ýagdagda maglumatlaryňyzyň ählisi pozular we yzyna gaýtaryp bolmaz', type:'button', btnLabel:'Hasaby poz', danger:true },
    ]
  },
])
</script>