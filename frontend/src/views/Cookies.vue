<template>
  <div class="min-h-screen bg-[#FAFAF7]" style="font-family: 'Cormorant Garamond', Georgia, serif;">

    <component :is="'link'" rel="preconnect" href="https://fonts.googleapis.com" />
    <component :is="'link'" rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500;600&display=swap" />
      
        <!-- Hero -->
    <div class="bg-[#1C1C1E] relative overflow-hidden">
      <div class="absolute inset-0 opacity-[0.05]"
        style="background-image: repeating-linear-gradient(0deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px),repeating-linear-gradient(90deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px);">
      </div>
      <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
        <router-link to="/"
          class="inline-flex items-center gap-2 text-[#6B6B6B] hover:text-[#A8896C] transition-colors mb-8"
          style="font-family: 'DM Sans', sans-serif; font-size: 13px;">
          <v-icon size="16" icon="mdi-arrow-left" /> Baş sahypa
        </router-link>
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-xl bg-[#A8896C]/20 flex items-center justify-center">
            <v-icon size="20" icon="mdi-shield-lock-outline" class="text-[#A8896C]" />
          </div>
          <span class="text-xs tracking-[0.3em] uppercase text-[#A8896C]"
            style="font-family: 'DM Sans', sans-serif;">Şiir Koridoru</span>
        </div>
        <h1 class="text-4xl sm:text-5xl text-[#F5F0E8] mb-4" style="font-weight: 300; font-style: italic;">
          Kuki<br /><span class="text-[#A8896C]">Syýasaty</span>
        </h1>
        <p class="text-[#6B6B6B] text-sm" style="font-family: 'DM Sans', sans-serif;">
          Soňky täzelenme: 9-njy Mart 2026
        </p>
      </div>
    </div>

    <!-- İçerik -->
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
      <div class="flex flex-col lg:flex-row gap-10 lg:gap-16">

        <!-- Sidebar -->
        <aside class="lg:w-56 shrink-0">
          <div class="lg:sticky lg:top-24">
            <p class="text-xs tracking-[0.2em] uppercase text-[#A8896C] mb-4"
              style="font-family: 'DM Sans', sans-serif;">Mazmun</p>
            <nav class="space-y-1">
              <a
                v-for="section in sections"
                :key="section.id"
                :href="`#${section.id}`"
                :class="[
                  'flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-all',
                  activeSection === section.id
                    ? 'bg-[#F0EBE1] text-[#1C1C1E] font-medium'
                    : 'text-[#9A9A8A] hover:text-[#1C1C1E] hover:bg-[#F5F2EC]'
                ]"
                style="font-family: 'DM Sans', sans-serif; font-size: 12px;"
                @click.prevent="scrollTo(section.id)"
              >
                <v-icon size="13" :icon="section.icon" class="shrink-0" />
                {{ section.title }}
              </a>
            </nav>

            <!-- Çerez tercihleri butonu -->
            <div class="mt-8 p-4 bg-[#1C1C1E] rounded-2xl">
              <p class="text-xs text-[#6B6B6B] leading-relaxed mb-3"
                style="font-family: 'DM Sans', sans-serif;">
                Kuki saýlawlaryňyzy islän wagtyňyz üýtgedip bilersiňiz.
              </p>
              <button @click="showCookiePanel = true"
                class="w-full flex items-center justify-center gap-2 px-3 py-2 bg-[#A8896C] text-[#1C1C1E] rounded-xl text-xs font-semibold hover:bg-[#C8A87C] transition-all"
                style="font-family: 'DM Sans', sans-serif; letter-spacing: 0.04em;">
                <v-icon size="14" icon="mdi-tune-variant" />
                Saýlawlary dolandyr
              </button>
            </div>

            <!-- İletişim -->
            <div class="mt-4 p-4 bg-[#F0EBE1] rounded-2xl border border-[#E5DFD5]">
              <p class="text-xs text-[#6B6B5A] leading-relaxed mb-3"
                style="font-family: 'DM Sans', sans-serif;">
                Soraglaryňyz barmy?
              </p>
              <a href="mailto:kuki@siirkoridoru.com"
                class="flex items-center gap-1.5 text-xs text-[#A8896C] hover:underline"
                style="font-family: 'DM Sans', sans-serif;">
                <v-icon size="13" icon="mdi-email-outline" />
                Bize ýazyň
              </a>
            </div>
          </div>
        </aside>

        <!-- Ana içerik -->
        <article class="flex-1 min-w-0">

          <!-- Giriş -->
          <div class="mb-10 p-6 bg-[#F0EBE1] rounded-2xl border-l-4 border-[#A8896C]">
            <p class="text-[#3A3020] leading-relaxed" style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 17px; line-height: 1.9;">
              Şiir Koridoru saýtyny ulananyňyzda, size has gowy tejribe bermek üçin kukilerden peýdalanýarys. Bu syýasat kukiler barada giňişleýin maglumat berýär.
            </p>
          </div>

          <div class="space-y-12">

            <!-- 1 — Kuki nedir -->
            <section :id="sections[0].id" class="scroll-mt-24">
              <SectionHeader :section="sections[0]" />
              <div class="prose-content space-y-3">
                <p>Kukiler, saýtymyza gireniňizde enjamyňyzda saklanan kiçijik tekst faýllardyr. Olar saýtyň dogry işlemegini üpjün edýär, saýlawlaryňyzy ýatlaýar we tejribäňizi kişiselleşdirýär.</p>
                <p>Kukiler biziň tarapymyzdan ýa-da ynanylan üçünji tarap hyzmatlar tarapyndan ýerleşdirilip bilner.</p>
              </div>
            </section>

            <Divider />

            <!-- 2 — Kuki türleri -->
            <section :id="sections[1].id" class="scroll-mt-24">
              <SectionHeader :section="sections[1]" />
              <div class="prose-content">
                <p class="mb-5">Platformymyzda dört esasy kuki görnüşi ulanylýar:</p>
                <div class="space-y-3">
                  <div v-for="type in cookieTypes" :key="type.id"
                    class="rounded-2xl border border-[#EAE5DC] overflow-hidden">
                    <button
                      @click="type.open = !type.open"
                      class="w-full flex items-center gap-4 px-5 py-4 hover:bg-[#FAFAF7] transition-colors text-left"
                    >
                      <div class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0"
                        :class="type.bg">
                        <v-icon size="17" :icon="type.icon" :class="type.color" />
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-2 flex-wrap">
                          <p class="text-sm font-semibold text-[#1C1C1E]"
                            style="font-family: 'DM Sans', sans-serif;">{{ type.name }}</p>
                          <span :class="['px-2 py-0.5 rounded-full text-xs font-medium', type.required ? 'bg-[#E8F5E9] text-[#2E7D32]' : 'bg-[#FFF8E1] text-[#B8860B]']"
                            style="font-family: 'DM Sans', sans-serif; font-size: 10px; letter-spacing: 0.04em;">
                            {{ type.required ? 'Zorunlu' : 'Opsiyonel' }}
                          </span>
                        </div>
                        <p class="text-xs text-[#9A9A8A] mt-0.5"
                          style="font-family: 'DM Sans', sans-serif;">{{ type.short }}</p>
                      </div>
                      <div class="flex items-center gap-3 shrink-0">
                        <!-- Toggle (zorunlu olmayanlar için) -->
                        <button v-if="!type.required"
                          @click.stop="type.enabled = !type.enabled"
                          :class="['w-10 h-5 rounded-full transition-all duration-300 relative', type.enabled ? 'bg-[#1C1C1E]' : 'bg-[#D9D0C4]']">
                          <span :class="['absolute top-0.5 w-4 h-4 bg-white rounded-full shadow transition-all duration-300', type.enabled ? 'left-5' : 'left-0.5']"></span>
                        </button>
                        <div v-else class="w-10 h-5 rounded-full bg-[#2E7D32]/20 relative cursor-not-allowed">
                          <span class="absolute top-0.5 left-5 w-4 h-4 bg-[#2E7D32] rounded-full shadow opacity-60"></span>
                        </div>
                        <v-icon size="16" :icon="type.open ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                          class="text-[#9A9A8A]" />
                      </div>
                    </button>

                    <!-- Açılır detay -->
                    <Transition
                      enter-active-class="transition-all duration-200 ease-out"
                      enter-from-class="opacity-0"
                      enter-to-class="opacity-100"
                      leave-active-class="transition-all duration-150"
                      leave-from-class="opacity-100"
                      leave-to-class="opacity-0"
                    >
                      <div v-if="type.open" class="px-5 pb-5 border-t border-[#F0EBE1]">
                        <p class="text-sm text-[#4A4438] leading-relaxed mt-4 mb-4"
                          style="font-family: 'DM Sans', sans-serif; font-size: 13px;">{{ type.desc }}</p>
                        <!-- Kuki tablosu -->
                        <div class="rounded-xl overflow-hidden border border-[#EAE5DC]">
                          <table class="w-full text-xs" style="font-family: 'DM Sans', sans-serif;">
                            <thead>
                              <tr class="bg-[#F5F2EC] border-b border-[#EAE5DC]">
                                <th class="text-left px-4 py-2.5 text-[#6B6B5A] font-medium tracking-wide" style="font-size: 10px; letter-spacing: 0.08em;">KUKİ ADY</th>
                                <th class="text-left px-4 py-2.5 text-[#6B6B5A] font-medium tracking-wide hidden sm:table-cell" style="font-size: 10px; letter-spacing: 0.08em;">MAKSAT</th>
                                <th class="text-left px-4 py-2.5 text-[#6B6B5A] font-medium tracking-wide" style="font-size: 10px; letter-spacing: 0.08em;">MÖHLETI</th>
                              </tr>
                            </thead>
                            <tbody class="divide-y divide-[#F0EBE1] bg-white">
                              <tr v-for="cookie in type.cookies" :key="cookie.name"
                                class="hover:bg-[#FAFAF7] transition-colors">
                                <td class="px-4 py-3 text-[#1C1C1E] font-mono" style="font-size: 11px;">{{ cookie.name }}</td>
                                <td class="px-4 py-3 text-[#6B6B5A] hidden sm:table-cell">{{ cookie.purpose }}</td>
                                <td class="px-4 py-3 text-[#9A9A8A]">{{ cookie.duration }}</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </Transition>
                  </div>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 3 — Üçüncü taraflar -->
            <section :id="sections[2].id" class="scroll-mt-24">
              <SectionHeader :section="sections[2]" />
              <div class="prose-content space-y-4">
                <p>Käbir kukiler biziň tarapymyzdan däl-de, ynanylan üçünji taraf hyzmatlar tarapyndan ýerleşdirilýär:</p>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div v-for="party in thirdParties" :key="party.name"
                    class="p-4 bg-white rounded-xl border border-[#EAE5DC] hover:border-[#A8896C]/40 transition-colors">
                    <div class="flex items-center gap-2 mb-2">
                      <v-icon size="15" :icon="party.icon" class="text-[#A8896C]" />
                      <span class="text-sm font-semibold text-[#1C1C1E]"
                        style="font-family: 'DM Sans', sans-serif; font-size: 13px;">{{ party.name }}</span>
                    </div>
                    <p class="text-xs text-[#6B6B5A] leading-relaxed mb-2"
                      style="font-family: 'DM Sans', sans-serif;">{{ party.desc }}</p>
                    <a :href="party.link" target="_blank" rel="noopener"
                      class="text-xs text-[#A8896C] hover:underline flex items-center gap-1"
                      style="font-family: 'DM Sans', sans-serif;">
                      Syýasaty oka <v-icon size="11" icon="mdi-open-in-new" />
                    </a>
                  </div>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 4 — Yönetim -->
            <section :id="sections[3].id" class="scroll-mt-24">
              <SectionHeader :section="sections[3]" />
              <div class="prose-content space-y-4">
                <p>Kukilerden ýüz öwürmek ýa-da pozmak üçin aşakdaky usullary ulanyp bilersiňiz:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div v-for="method in manageMethods" :key="method.title"
                    class="flex items-start gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC]">
                    <div class="w-8 h-8 rounded-lg bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="15" :icon="method.icon" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-sm font-semibold text-[#1C1C1E] mb-0.5"
                        style="font-family: 'DM Sans', sans-serif;">{{ method.title }}</p>
                      <p class="text-xs text-[#6B6B5A] leading-relaxed"
                        style="font-family: 'DM Sans', sans-serif;">{{ method.desc }}</p>
                    </div>
                  </div>
                </div>
                <div class="p-4 bg-[#FFF8E1] border border-[#F5E6A3] rounded-xl flex items-start gap-3">
                  <v-icon size="16" icon="mdi-alert-outline" class="text-[#B8860B] shrink-0 mt-0.5" />
                  <p class="text-sm text-[#6B5500]" style="font-family: 'DM Sans', sans-serif; font-size: 13px;">
                    Zerury kukilerden ýüz öwürmek saýtyň käbir aýratynlyklaryny bozup biler.
                  </p>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 5 — Güncellemeler -->
            <section :id="sections[4].id" class="scroll-mt-24">
              <SectionHeader :section="sections[4]" />
              <div class="prose-content">
                <p>Bu syýasat wagtal-wagtal täzelenip bilner. Möhüm üýtgeşmeler barada saýtymyzda we e-poçta arkaly habardar edilersiňiz. Täzelenme senesini yzygiderli barlamagyňyzy maslahat berýäris.</p>
              </div>
            </section>

            <Divider />

            <!-- 6 — İletişim -->
            <section :id="sections[5].id" class="scroll-mt-24">
              <SectionHeader :section="sections[5]" />
              <div class="prose-content space-y-4">
                <p>Kuki syýasatymyz barada soraglaryňyz bar bolsa bize ýüz tutup bilersiňiz:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <a href="mailto:kuki@siirkoridoru.com"
                    class="flex items-center gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC] hover:border-[#A8896C] transition-colors group">
                    <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="18" icon="mdi-email-outline" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-xs text-[#9A9A8A] mb-0.5" style="font-family: 'DM Sans', sans-serif;">E-poçta</p>
                      <p class="text-sm text-[#1C1C1E] group-hover:text-[#A8896C] transition-colors"
                        style="font-family: 'DM Sans', sans-serif; font-size: 12px;">kuki@siirkoridoru.com</p>
                    </div>
                  </a>
                  <div class="flex items-center gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC]">
                    <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="18" icon="mdi-map-marker-outline" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-xs text-[#9A9A8A] mb-0.5" style="font-family: 'DM Sans', sans-serif;">Adres</p>
                      <p class="text-sm text-[#1C1C1E]"
                        style="font-family: 'DM Sans', sans-serif; font-size: 12px;">Aşgabat, Türkmenistan</p>
                    </div>
                  </div>
                </div>
              </div>
            </section>

          </div>

          <!-- Alt imza -->
          <div class="mt-16 pt-8 border-t border-[#EAE5DC] flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <p class="text-xs text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">
              Bu syýasat 9-njy Mart 2026-da güýje girdi.
            </p>
            <div class="flex items-center gap-3">
              <router-link to="/privacy"
                class="text-xs text-[#A8896C] hover:underline"
                style="font-family: 'DM Sans', sans-serif;">Gizlinlik Syýasaty</router-link>
              <span class="text-[#D9D0C4]">·</span>
              <router-link to="/terms"
                class="text-xs text-[#A8896C] hover:underline"
                style="font-family: 'DM Sans', sans-serif;">Ulanyjy Şertleri</router-link>
              <span class="text-[#D9D0C4]">·</span>
              <router-link to="/"
                class="text-xs text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors"
                style="font-family: 'DM Sans', sans-serif;">Baş sahypa</router-link>
            </div>
          </div>

        </article>
      </div>
    </div>

    <!-- ── Çerez Tercihleri Paneli (Modal) ── -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="showCookiePanel"
        class="fixed inset-0 bg-black/50 z-50 flex items-end sm:items-center justify-center p-4"
        @click.self="showCookiePanel = false">
        <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden">
          <div class="bg-[#1C1C1E] px-6 py-5 flex items-center justify-between">
            <div class="flex items-center gap-3">
              <v-icon size="20" icon="mdi-cookie-outline" class="text-[#A8896C]" />
              <h2 class="text-lg text-[#F5F0E8]"
                style="font-family: 'Cormorant Garamond', serif; font-weight: 400; font-style: italic;">
                Kuki Saýlawlary
              </h2>
            </div>
            <button @click="showCookiePanel = false"
              class="p-1.5 rounded-lg hover:bg-[#2E2E30] text-[#6B6B6B] hover:text-[#F5F0E8] transition-all">
              <v-icon size="18" icon="mdi-close" />
            </button>
          </div>

          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-[#6B6B5A] leading-relaxed"
              style="font-family: 'DM Sans', sans-serif; font-size: 13px;">
              Isleýän kukilerinizi saýlaň. Zerury kukiler saýtyň işlemegi üçin hemişe açyk galýar.
            </p>

            <div class="space-y-3">
              <div v-for="type in cookieTypes" :key="type.id"
                class="flex items-center justify-between p-3.5 rounded-xl border border-[#EAE5DC] hover:bg-[#FAFAF7] transition-colors">
                <div class="flex items-center gap-3 min-w-0">
                  <div class="w-8 h-8 rounded-lg flex items-center justify-center shrink-0" :class="type.bg">
                    <v-icon size="15" :icon="type.icon" :class="type.color" />
                  </div>
                  <div class="min-w-0">
                    <p class="text-sm text-[#1C1C1E] font-medium truncate"
                      style="font-family: 'DM Sans', sans-serif;">{{ type.name }}</p>
                    <p class="text-xs text-[#9A9A8A] truncate"
                      style="font-family: 'DM Sans', sans-serif;">{{ type.short }}</p>
                  </div>
                </div>
                <button v-if="!type.required"
                  @click="type.enabled = !type.enabled"
                  :class="['w-11 h-6 rounded-full transition-all duration-300 relative shrink-0 ml-3', type.enabled ? 'bg-[#1C1C1E]' : 'bg-[#D9D0C4]']">
                  <span :class="['absolute top-1 w-4 h-4 bg-white rounded-full shadow transition-all duration-300', type.enabled ? 'left-6' : 'left-1']"></span>
                </button>
                <span v-else
                  class="ml-3 text-xs text-[#2E7D32] bg-[#E8F5E9] px-2 py-1 rounded-full shrink-0"
                  style="font-family: 'DM Sans', sans-serif; font-size: 10px;">
                  Hemişe açyk
                </span>
              </div>
            </div>
          </div>

          <div class="px-6 py-4 border-t border-[#EAE5DC] flex gap-3">
            <button @click="rejectAll"
              class="flex-1 py-2.5 border border-[#D9D0C4] text-[#6B6B5A] rounded-xl text-xs hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-all"
              style="font-family: 'DM Sans', sans-serif; letter-spacing: 0.06em;">
              Hemmesini ret et
            </button>
            <button @click="acceptSelected"
              class="flex-1 py-2.5 border border-[#1C1C1E] text-[#1C1C1E] rounded-xl text-xs hover:bg-[#F0EBE1] transition-all"
              style="font-family: 'DM Sans', sans-serif; letter-spacing: 0.06em;">
              Saýlanlary kabul et
            </button>
            <button @click="acceptAll"
              class="flex-1 py-2.5 bg-[#1C1C1E] text-[#F5F0E8] rounded-xl text-xs hover:bg-[#3A3A2E] transition-all font-semibold"
              style="font-family: 'DM Sans', sans-serif; letter-spacing: 0.06em;">
              Hemmesini kabul et
            </button>
          </div>
        </div>
      </div>
    </Transition>

  </div>
</template>

<script>
import { defineComponent } from 'vue'

const SectionHeader = defineComponent({
  props: { section: Object },
  template: `
    <div class="flex items-center gap-3 mb-5">
      <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0">
        <v-icon size="17" :icon="section.icon" class="text-[#A8896C]" />
      </div>
      <h2 class="text-2xl text-[#1C1C1E]"
        style="font-family:'Cormorant Garamond',serif;font-weight:400;">
        {{ section.title }}
      </h2>
    </div>
  `
})

const Divider = defineComponent({
  template: `<div class="border-t border-dashed border-[#E5DFD5]"></div>`
})

export default { components: { SectionHeader, Divider } }
</script>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('')
const showCookiePanel = ref(false)

const sections = [
  { id: 'nedir',      title: 'Kuki näme?',               icon: 'mdi-help-circle-outline' },
  { id: 'gornusleri', title: 'Kuki görnüşleri',           icon: 'mdi-cookie-outline' },
  { id: 'ucucitarap', title: 'Üçünji tarap kukiler',       icon: 'mdi-share-variant-outline' },
  { id: 'dolandyrmak','title': 'Kukiler dolandyrmak',      icon: 'mdi-tune-variant' },
  { id: 'tazelenme',  title: 'Syýasatyň täzelenmeleri',   icon: 'mdi-update' },
  { id: 'habarlasmak','title': 'Habarlaşmak',              icon: 'mdi-email-outline' },
]

const cookieTypes = ref([
  {
    id: 'essential', open: false, required: true, enabled: true,
    name: 'Zerur Kukiler',
    short: 'Saýtyň işlemegi üçin hökmany',
    icon: 'mdi-shield-check-outline', bg: 'bg-[#E8F5E9]', color: 'text-[#2E7D32]',
    desc: 'Bu kukiler saýtyň dogry işlemegi üçin zerurdyr we öçürilip bilinmez. Olar adatça diňe siziň haýyşlaryňyza jogap berýän hereketler üçin, meselem giriş, ulanyjy saýlawy ýa-da gizlinlik tercihleri üçin ýerleşdirilýär.',
    cookies: [
      { name: 'session_id',  purpose: 'Giriş sessiýasyny dolandyrýar',     duration: 'Sesiýa' },
      { name: 'csrf_token',  purpose: 'Howpsuzlyk goragyny üpjün edýär',    duration: 'Sesiýa' },
      { name: 'auth_token',  purpose: 'Ulanyjy kimligini tassyklaýar',      duration: '30 gün' },
      { name: 'lang_pref',   purpose: 'Dil saýlawyny ýatlaýar',            duration: '1 ýyl'  },
    ]
  },
  {
    id: 'functional', open: false, required: false, enabled: true,
    name: 'Işleýiş Kukiler',
    short: 'Saýlawlary we tercihleri ýatlaýar',
    icon: 'mdi-cog-outline', bg: 'bg-[#F0EBE1]', color: 'text-[#A8896C]',
    desc: 'Bu kukiler saýtyň has giňeldilen aýratynlyklaryny we kişiselleşdirmäni üpjün edýär. Tema saýlawy, okyş görnüşi we şuňa meňzeş tercihleri ýatda saklaýar.',
    cookies: [
      { name: 'theme',       purpose: 'Açyk / koyu tema saýlawyny saklaýar', duration: '1 ýyl'  },
      { name: 'font_size',   purpose: 'Okyş ölçeg saýlawyny saklaýar',       duration: '1 ýyl'  },
      { name: 'reading_list','purpose': 'Okyş sanawyny saklaýar',             duration: '90 gün' },
    ]
  },
  {
    id: 'analytics', open: false, required: false, enabled: true,
    name: 'Analitika Kukiler',
    short: 'Saýt ulanylşyny ölçeýär',
    icon: 'mdi-chart-line', bg: 'bg-[#EDE7F6]', color: 'text-[#5E35B1]',
    desc: 'Bu kukiler siziň saýty nädip ulanýandygyňyzy düşünmäge kömek edýär. Ähli maglumatlar jemlenip, hiç kim bilen aýratynlykda paýlaşylmaýar.',
    cookies: [
      { name: '_ga',         purpose: 'Google Analytics ulanyjy tapawutlandyryjy', duration: '2 ýyl'  },
      { name: '_gid',        purpose: 'Google Analytics sesiýa tapawutlandyryjy',  duration: '24 sagat' },
      { name: 'page_views',  purpose: 'Sahypa görüntülemelerini hasaplaýar',        duration: '30 gün' },
    ]
  },
  {
    id: 'marketing', open: false, required: false, enabled: false,
    name: 'Marketing Kukiler',
    short: 'Mahabat we täzeden nişanlama',
    icon: 'mdi-bullhorn-outline', bg: 'bg-[#FFF0F0]', color: 'text-[#C0392B]',
    desc: 'Bu kukiler size has laýyk mahabatlary görkezmek üçin ulanylýar. Şeýle hem siziň platformamyzy nähili ulanýandygyňyzy yzarlamak we kampaniýalaryň netijeliligini ölçemek üçin hem ulanylýar.',
    cookies: [
      { name: 'fbp',         purpose: 'Facebook täzeden nişanlama',          duration: '90 gün' },
      { name: 'ads_session', purpose: 'Mahabat sesiýasyny yzarlaýar',        duration: 'Sesiýa' },
    ]
  },
])

const thirdParties = [
  {
    name: 'Google Analytics',
    icon: 'mdi-google',
    desc: 'Saýt traffigini we ulanyjy hereketlerini yzarlamak üçin ulanylýar.',
    link: 'https://policies.google.com/privacy'
  },
  {
    name: 'Google Fonts',
    icon: 'mdi-format-font',
    desc: 'Saýtyň görnüşini gowulaşdyrmak üçin ýazuw şriftleri ýüklenilýär.',
    link: 'https://policies.google.com/privacy'
  },
  {
    name: 'DiceBear',
    icon: 'mdi-account-circle-outline',
    desc: 'Ulanyjy profil avatarlaryny döretmek üçin ulanylýar.',
    link: 'https://www.dicebear.com/legal/privacy-policy'
  },
]

const manageMethods = [
  {
    title: 'Brauzer sazlamalary',
    icon: 'mdi-web',
    desc: 'Brauzeriňiziň sazlamalaryndan kukilerden doly ýüz öwrüp bilersiňiz.'
  },
  {
    title: 'Platformamyzdaky panel',
    icon: 'mdi-tune-variant',
    desc: 'Saýaldaky "Saýlawlary dolandyr" düwmesini ulanyp kuki saýlawyňyzy üýtgedip bilersiňiz.'
  },
  {
    title: 'Hasap sazlamalary',
    icon: 'mdi-account-cog-outline',
    desc: 'Giriş eden bolsaňyz, hasap sazlamalaryndan kuki saýlawyňyzy dolandyryp bilersiňiz.'
  },
  {
    title: 'Opt-out baglanyşyklary',
    icon: 'mdi-link-variant-off',
    desc: 'Üçünji tarap hyzmatlaryndan çykmak üçin degişli opt-out baglanyşyklaryny ulanyň.'
  },
]

const rejectAll = () => {
  cookieTypes.value.forEach(t => { if (!t.required) t.enabled = false })
  showCookiePanel.value = false
}

const acceptSelected = () => {
  showCookiePanel.value = false
}

const acceptAll = () => {
  cookieTypes.value.forEach(t => t.enabled = true)
  showCookiePanel.value = false
}

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  activeSection.value = id
}

let observer
onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => { entries.forEach(e => { if (e.isIntersecting) activeSection.value = e.target.id }) },
    { rootMargin: '-20% 0px -70% 0px' }
  )
  sections.forEach(s => {
    const el = document.getElementById(s.id)
    if (el) observer.observe(el)
  })
})
onUnmounted(() => observer?.disconnect())
</script>

<style scoped>
.prose-content {
  font-family: 'DM Sans', sans-serif;
  font-size: 14px;
  color: #4A4438;
  line-height: 1.8;
}
.prose-content p { margin-bottom: 0.75rem; }
.prose-content strong { color: #1C1C1E; font-weight: 600; }
.prose-content a { color: #A8896C; }
.prose-content a:hover { text-decoration: underline; }
</style>