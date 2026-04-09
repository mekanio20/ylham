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
          Gizlinlik<br /><span class="text-[#A8896C]">Syýasaty</span>
        </h1>
        <p class="text-[#6B6B6B] text-sm" style="font-family: 'DM Sans', sans-serif;">
          Soňky täzelenme: 9-njy Mart 2026
        </p>
      </div>
    </div>

    <!-- İçerik -->
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
      <div class="flex flex-col lg:flex-row gap-10 lg:gap-16">

        <!-- İçindekiler (sidebar) -->
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

            <!-- Geri bildirim kutusu -->
            <div class="mt-8 p-4 bg-[#F0EBE1] rounded-2xl border border-[#E5DFD5]">
              <p class="text-xs text-[#6B6B5A] leading-relaxed mb-3"
                style="font-family: 'DM Sans', sans-serif;">
                Soraglaryňyz barmy?
              </p>
              <a href="mailto:gizlinlik@siirkoridoru.com"
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
              Şiir Koridoru hökmünde ulanyjylarymyzyň gizlinligini goramak biziň esasy borjumyzdyr. Bu syýasat siziň maglumatyňyzyň nädip ýygnalandygyny, ulanylýandygyny we goralandygyny düşündirýär.
            </p>
          </div>

          <div class="space-y-12">

            <!-- 1 -->
            <section :id="sections[0].id" class="scroll-mt-24">
              <SectionHeader :section="sections[0]" />
              <div class="prose-content">
                <p>Şiir Koridoru platformyna gireniňizde, aşakdaky maglumatlary ýygnaýarys:</p>
                <InfoBlock>
                  <InfoItem icon="mdi-account-outline"    title="Hasap maglumaty"    desc="At-familiýaňyz, ulanyjy adyňyz, e-poçta salgyňyz we parolyňyz (şifrlenip saklanýar)." />
                  <InfoItem icon="mdi-file-document-outline" title="Mazmun maglumaty" desc="Ýükleýän şiirler, teswirler we beýleki döredilen materiallar." />
                  <InfoItem icon="mdi-gesture-tap"        title="Ulanyjy hereketleri" desc="Saýtdaky işjeňligiňiz: haýsy şiirleri okaýandygyňyz, halanýandygyňyz we ýazdyklaryny yzarlaýandygyňyz." />
                  <InfoItem icon="mdi-devices"            title="Enjam maglumaty"    desc="IP salgy, brauzer görnüşi, operasion ulgam we çözünürlik barada tehniki maglumatlar." />
                  <InfoItem icon="mdi-cookie-outline"     title="Kukiler"            desc="Saýty has amatly etmek üçin kukiler we meňzeş tehnologiýalar ulanylýar." />
                </InfoBlock>
              </div>
            </section>

            <Divider />

            <!-- 2 -->
            <section :id="sections[1].id" class="scroll-mt-24">
              <SectionHeader :section="sections[1]" />
              <div class="prose-content space-y-4">
                <p>Ýygnalan maglumatlar aşakdaky maksatlar üçin ulanylýar:</p>
                <ul class="space-y-3">
                  <li v-for="item in useList" :key="item" class="flex items-start gap-3">
                    <div class="w-5 h-5 rounded-full bg-[#A8896C]/15 flex items-center justify-center shrink-0 mt-0.5">
                      <v-icon size="11" icon="mdi-check" class="text-[#A8896C]" />
                    </div>
                    <span>{{ item }}</span>
                  </li>
                </ul>
              </div>
            </section>

            <Divider />

            <!-- 3 -->
            <section :id="sections[2].id" class="scroll-mt-24">
              <SectionHeader :section="sections[2]" />
              <div class="prose-content space-y-4">
                <p>Şiir Koridoru maglumatyňyzy üçünji taraplara <strong>satmaýar</strong>. Şeýle-de bolsa, aşakdaky ýagdaýlarda paýlaşylyp bilner:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div v-for="share in shareList" :key="share.title"
                    class="p-4 bg-white rounded-xl border border-[#EAE5DC]">
                    <div class="flex items-center gap-2 mb-2">
                      <v-icon size="15" :icon="share.icon" class="text-[#A8896C]" />
                      <span class="text-sm font-medium text-[#1C1C1E]" style="font-family: 'DM Sans', sans-serif;">{{ share.title }}</span>
                    </div>
                    <p class="text-[#6B6B5A] text-sm leading-relaxed" style="font-family: 'DM Sans', sans-serif; font-size: 12px;">{{ share.desc }}</p>
                  </div>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 4 -->
            <section :id="sections[3].id" class="scroll-mt-24">
              <SectionHeader :section="sections[3]" />
              <div class="prose-content space-y-4">
                <p>Maglumatyňyzy goramak üçin aşakdaky çäreleri ulanýarys:</p>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div v-for="sec in securityList" :key="sec.title"
                    class="p-4 bg-[#1C1C1E] rounded-xl text-center">
                    <v-icon size="22" :icon="sec.icon" class="text-[#A8896C] mb-2" />
                    <p class="text-sm text-[#F5F0E8] font-medium mb-1" style="font-family: 'DM Sans', sans-serif; font-size: 12px;">{{ sec.title }}</p>
                    <p class="text-xs text-[#6B6B6B]" style="font-family: 'DM Sans', sans-serif;">{{ sec.desc }}</p>
                  </div>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 5 -->
            <section :id="sections[4].id" class="scroll-mt-24">
              <SectionHeader :section="sections[4]" />
              <div class="prose-content space-y-4">
                <p>Siziň aşakdaky hukuklaryňyz bardyr:</p>
                <div class="space-y-3">
                  <div v-for="right in rightsList" :key="right.title"
                    class="flex items-start gap-4 p-4 bg-white rounded-xl border border-[#EAE5DC] hover:border-[#A8896C] transition-colors">
                    <div class="w-8 h-8 rounded-lg bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="16" :icon="right.icon" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-sm font-semibold text-[#1C1C1E] mb-0.5" style="font-family: 'DM Sans', sans-serif;">{{ right.title }}</p>
                      <p class="text-sm text-[#6B6B5A] leading-relaxed" style="font-family: 'DM Sans', sans-serif; font-size: 12px;">{{ right.desc }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </section>

            <Divider />

            <!-- 6 -->
            <section :id="sections[5].id" class="scroll-mt-24">
              <SectionHeader :section="sections[5]" />
              <div class="prose-content">
                <p>Saýtymyzda üçünji tarap hyzmatlaryna baglanyşyklar bolup biler. Bu hyzmatlaryň öz gizlinlik syýasatlaryna görä işleýändigini we biziň olara jogapkärçilik çekmeýändigimizi ýatladýarys.</p>
              </div>
            </section>

            <Divider />

            <!-- 7 -->
            <section :id="sections[6].id" class="scroll-mt-24">
              <SectionHeader :section="sections[6]" />
              <div class="prose-content">
                <p>Şiir Koridoru 18 ýaşdan kiçi ulanyjylaryň maglumatlaryny bilgeşleýin ýygnamaýar. Eger çaganyň hasaby hasaba alnan bolsa, <a href="mailto:gizlinlik@siirkoridoru.com" class="text-[#A8896C] hover:underline">bize habar beriň</a>, derrew çäreler göreris.</p>
              </div>
            </section>

            <Divider />

            <!-- 8 -->
            <section :id="sections[7].id" class="scroll-mt-24">
              <SectionHeader :section="sections[7]" />
              <div class="prose-content">
                <p>Bu syýasat wagtal-wagtal täzelenip bilner. Möhüm üýtgeşmeler barada e-poçta arkaly habardar edileris. Täzelenme senesini yzygiderli barlamagyňyzy maslahat berýäris.</p>
              </div>
            </section>

            <Divider />

            <!-- 9 -->
            <section :id="sections[8].id" class="scroll-mt-24">
              <SectionHeader :section="sections[8]" />
              <div class="prose-content">
                <p>Soraglaryňyz, haýyşlaryňyz ýa-da şikaýatlaryňyz üçin bize ýüz tutup bilersiňiz:</p>
                <div class="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <a href="mailto:gizlinlik@siirkoridoru.com"
                    class="flex items-center gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC] hover:border-[#A8896C] transition-colors group">
                    <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="18" icon="mdi-email-outline" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-xs text-[#9A9A8A] mb-0.5" style="font-family: 'DM Sans', sans-serif;">E-poçta</p>
                      <p class="text-sm text-[#1C1C1E] group-hover:text-[#A8896C] transition-colors" style="font-family: 'DM Sans', sans-serif; font-size: 12px;">gizlinlik@siirkoridoru.com</p>
                    </div>
                  </a>
                  <div class="flex items-center gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC]">
                    <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0">
                      <v-icon size="18" icon="mdi-map-marker-outline" class="text-[#A8896C]" />
                    </div>
                    <div>
                      <p class="text-xs text-[#9A9A8A] mb-0.5" style="font-family: 'DM Sans', sans-serif;">Adres</p>
                      <p class="text-sm text-[#1C1C1E]" style="font-family: 'DM Sans', sans-serif; font-size: 12px;">Aşgabat, Türkmenistan</p>
                    </div>
                  </div>
                </div>
              </div>
            </section>

          </div>

          <!-- Alt imza -->
          <div class="mt-16 pt-8 border-t border-[#EAE5DC] flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
              <p class="text-xs text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">
                Bu syýasat 9-njy Mart 2026-da güýje girdi.
              </p>
            </div>
            <div class="flex items-center gap-3">
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
  </div>
</template>

<script>
import { defineComponent, h } from 'vue'

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

const InfoBlock = defineComponent({
  template: `<div class="mt-4 space-y-3"><slot /></div>`
})

const InfoItem = defineComponent({
  props: { icon: String, title: String, desc: String },
  template: `
    <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-[#EAE5DC]">
      <div class="w-8 h-8 rounded-lg bg-[#F0EBE1] flex items-center justify-center shrink-0">
        <v-icon size="15" :icon="icon" class="text-[#A8896C]" />
      </div>
      <div>
        <p class="text-sm font-semibold text-[#1C1C1E] mb-0.5" style="font-family:'DM Sans',sans-serif;">{{ title }}</p>
        <p class="text-sm text-[#6B6B5A] leading-relaxed" style="font-family:'DM Sans',sans-serif;font-size:12px;">{{ desc }}</p>
      </div>
    </div>
  `
})

export default { components: { SectionHeader, Divider, InfoBlock, InfoItem } }
</script>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('')

const sections = [
  { id: 'ýygnama',    title: 'Ýygnaýan maglumatymyz',      icon: 'mdi-database-outline' },
  { id: 'ulanmak',    title: 'Maglumatlary ulanmak',        icon: 'mdi-cog-outline' },
  { id: 'paýlaşmak',  title: 'Maglumat paýlaşmak',          icon: 'mdi-share-variant-outline' },
  { id: 'goramak',    title: 'Maglumatlary goramak',         icon: 'mdi-shield-check-outline' },
  { id: 'hukuklar',   title: 'Siziň hukuklaryňyz',          icon: 'mdi-account-check-outline' },
  { id: 'baglantylar','title': 'Üçünji tarap baglanyşyklar', icon: 'mdi-link-variant' },
  { id: 'çagalar',    title: 'Çagalaryň gizlinligi',         icon: 'mdi-account-child-outline' },
  { id: 'täzelenme',  title: 'Syýasatyň täzelenmeleri',      icon: 'mdi-update' },
  { id: 'habarlaşmak','title': 'Habarlaşmak',                icon: 'mdi-email-outline' },
]

const useList = [
  'Hasabyňyzy döretmek we dolandyrmak',
  'Şiir we ýazyjy maslahatlaryny kişiselleşdirmek',
  'Platformamyzy gowulaşdyrmak we täze aýratynlyklar goşmak',
  'Tehniki meseleleri çözmek we goldaw bermek',
  'Bikanun hereketlere garşy çäre görmek',
  'Kanuny borçlary ýerine ýetirmek',
]

const shareList = [
  { title: 'Hizmat üpjünçileri', icon: 'mdi-server-outline', desc: 'Hosting, e-poçta we analitika ýaly hyzmatlar üçin ygtybarly hyzmat üpjünçileri.' },
  { title: 'Hukuk borçlary',     icon: 'mdi-gavel',          desc: 'Kanun ýa-da sud karary talap etse, degişli edaralar bilen paýlaşylýar.' },
  { title: 'Ylalaşyk bilen',     icon: 'mdi-handshake-outline', desc: 'Diňe siziň açyk razylyk bilen üçünji taraplarapaýlaşylýar.' },
  { title: 'Howpsuzlyk',         icon: 'mdi-shield-alert-outline', desc: 'Alnyş synanşyklaryny we aldawçylyklary öňüni almak üçin.' },
]

const securityList = [
  { title: 'SSL Şifrlemesi',    icon: 'mdi-lock-outline',          desc: 'Ähli geçirilmeler TLS/SSL bilen goralýar' },
  { title: 'Parol Goramasy',    icon: 'mdi-key-outline',           desc: 'Parollar bcrypt bilen hashlanýar' },
  { title: 'Yzygiderli Audit',  icon: 'mdi-magnify-scan',          desc: 'Ulgam howpsuzlygy düzgünleýji barlanýar' },
]

const rightsList = [
  { title: 'Maglumat almak',        icon: 'mdi-eye-outline',             desc: 'Siziň barada saklaýan maglumatymyzyň nusgasyny talap edip bilersiňiz.' },
  { title: 'Düzetmek',              icon: 'mdi-pencil-outline',          desc: 'Nädogry maglumatyňyzy düzetmegimizi haýyş edip bilersiňiz.' },
  { title: 'Pozmak',                icon: 'mdi-delete-outline',          desc: 'Hasabyňyzy we maglumatyňyzy pozmak hukugyňyz bardyr.' },
  { title: 'Göçürmek',              icon: 'mdi-download-outline',        desc: 'Maglumatlaryňyzy göçürip alyp başga hyzmatyňyza geçirip bilersiňiz.' },
  { title: 'Işlenmegini çäklendirmek', icon: 'mdi-pause-circle-outline', desc: 'Belli maksatlar üçin maglumatlaryňyzyň işlenmegini çäklendirip bilersiňiz.' },
  { title: 'Garşy çykmak',          icon: 'mdi-hand-back-right-outline', desc: 'Belli maglumat işlemelerine garşy çykmak hukugyňyz bar.' },
]

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  activeSection.value = id
}

let observer
onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(e => { if (e.isIntersecting) activeSection.value = e.target.id })
    },
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