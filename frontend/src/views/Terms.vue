<template>
  <main class="min-h-screen bg-[#FAFAF7]" style="font-family: 'Cormorant Garamond', Georgia, serif;">

    <component :is="'link'" rel="preconnect" href="https://fonts.googleapis.com" />
    <component :is="'link'" rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500&display=swap" />

    <!-- Baş sahypa -->
    <div class="bg-[#1C1C1E] relative overflow-hidden">
      <div class="absolute inset-0 opacity-[0.05]"
        style="background-image: repeating-linear-gradient(0deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px),repeating-linear-gradient(90deg,transparent,transparent 39px,#F5F0E8 39px,#F5F0E8 40px);">
      </div>
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-14 sm:py-20 relative z-10 text-center">
        <p class="text-xs tracking-[0.4em] uppercase text-[#A8896C] mb-4"
          style="font-family: 'DM Sans', sans-serif;">Soňky täzelenme: 1 Mart 2025</p>
        <h1 class="text-4xl sm:text-5xl text-[#F5F0E8] mb-5 leading-tight"
          style="font-weight: 300;">
          Ulanyjy <em class="text-[#A8896C]">Şertleri</em>
        </h1>
        <p class="text-[#8A8A8A] max-w-lg mx-auto leading-relaxed"
          style="font-family: 'DM Sans', sans-serif; font-size: 14px;">
          Şygyr Geçelgesini ulanmazdan ozal bu şertleri ünsli okaň.
          Platforma hasaba durmak bilen bu şertleri kabul eden hasaplanýarsyňyz.
        </p>
      </div>
    </div>

    <!-- Mazmuny -->
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
      <div class="flex flex-col lg:flex-row gap-10">

        <!-- Mazmuny (sticky sidebar) -->
        <aside class="lg:w-52 shrink-0">
          <div class="lg:sticky lg:top-24">
            <p class="text-xs tracking-widest uppercase text-[#A8896C] mb-4"
              style="font-family: 'DM Sans', sans-serif;">Mazmuny</p>
            <nav class="space-y-1">
              <a
                v-for="item in tocItems"
                :key="item.id"
                :href="`#${item.id}`"
                :class="[
                  'block text-sm py-1.5 px-3 rounded-lg transition-colors',
                  activeSection === item.id
                    ? 'text-[#1C1C1E] bg-[#EDE8E0]'
                    : 'text-[#9A9A8A] hover:text-[#1C1C1E]'
                ]"
                style="font-family: 'DM Sans', sans-serif; font-size: 12px;">
                {{ item.label }}
              </a>
            </nav>

            <div class="mt-8 p-4 bg-[#F0EBE1] rounded-2xl">
              <p class="text-xs text-[#A8896C] mb-1 font-medium" style="font-family: 'DM Sans', sans-serif;">Soraglaryňyz barmy?</p>
              <p class="text-xs text-[#6B6B5A] leading-relaxed" style="font-family: 'DM Sans', sans-serif;">
                goldaw@sygyrgecelgesi.com arkaly bize ýüz tutup bilersiňiz.
              </p>
            </div>
          </div>
        </aside>

        <!-- Esasy tekst -->
        <article class="flex-1 min-w-0">
          <div class="space-y-10">

            <section v-for="section in sections" :key="section.id" :id="section.id">
              <!-- Bölüm başlığı -->
              <div class="flex items-start gap-4 mb-5">
                <div class="w-8 h-8 rounded-xl bg-[#F0EBE1] flex items-center justify-center shrink-0 mt-0.5">
                  <v-icon size="16" :icon="section.icon" class="text-[#A8896C]" />
                </div>
                <div>
                  <p class="text-xs tracking-widest uppercase text-[#A8896C] mb-1"
                    style="font-family: 'DM Sans', sans-serif;">Madda {{ section.num }}</p>
                  <h2 class="text-2xl text-[#1C1C1E]"
                    style="font-weight: 400;">{{ section.title }}</h2>
                </div>
              </div>

              <!-- Paragraflar -->
              <div class="pl-12 space-y-4">
                <p v-for="(para, i) in section.content" :key="i"
                  class="text-[#4A4438] leading-loose"
                  style="font-family: 'DM Sans', sans-serif; font-size: 14px; line-height: 1.9;">
                  {{ para }}
                </p>

                <!-- Madde listesi varsa -->
                <ul v-if="section.items" class="space-y-2 mt-2">
                  <li v-for="(item, i) in section.items" :key="i"
                    class="flex items-start gap-3 text-[#4A4438]"
                    style="font-family: 'DM Sans', sans-serif; font-size: 14px; line-height: 1.8;">
                    <span class="text-[#A8896C] mt-1 shrink-0">❧</span>
                    {{ item }}
                  </li>
                </ul>

                <!-- Uyarı kutusu -->
                <div v-if="section.warning"
                  class="flex items-start gap-3 px-4 py-3.5 bg-[#FFF8E8] border border-[#F5DFA0] rounded-xl mt-3">
                  <v-icon size="16" icon="mdi-alert-outline" class="text-[#B8860B] shrink-0 mt-0.5" />
                  <p class="text-sm text-[#7A6020] leading-relaxed"
                    style="font-family: 'DM Sans', sans-serif;">{{ section.warning }}</p>
                </div>
              </div>

              <div class="mt-8 h-px bg-[#EAE5DC]"></div>
            </section>

            <!-- İmza -->
            <div class="text-center py-8">
              <div class="flex items-center gap-3 justify-center mb-4">
                <div class="h-px w-16 bg-[#EAE5DC]"></div>
                <span class="text-[#C8B89A]" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">❧</span>
                <div class="h-px w-16 bg-[#EAE5DC]"></div>
              </div>
              <p class="text-lg text-[#1C1C1E] italic mb-1"
                style="font-family: 'Cormorant Garamond', serif; font-weight: 400;">
                Şygyr Geçelgesi Topary
              </p>
              <p class="text-xs text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">
                Bu şertler 1 Mart 2025 senesinden başlap güýje girýär.
              </p>
            </div>

          </div>
        </article>

      </div>
    </div>

    <!-- Alt gezinme -->
    <div class="border-t border-[#EAE5DC] bg-[#F0EBE1]">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex flex-col sm:flex-row items-center justify-between gap-4">
        <router-link to="/"
          class="flex items-center gap-2 text-sm text-[#6B6B5A] hover:text-[#1C1C1E] transition-colors"
          style="font-family: 'DM Sans', sans-serif;">
          <v-icon size="16" icon="mdi-arrow-left" />
          Baş Sahypä Dolan
        </router-link>
        <router-link to="/privacy"
          class="flex items-center gap-2 text-sm text-[#A8896C] hover:underline"
          style="font-family: 'DM Sans', sans-serif;">
          Gizlinlik Syýasatyny oka
          <v-icon size="16" icon="mdi-arrow-right" />
        </router-link>
      </div>
    </div>

  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('tanim')

const tocItems = [
  { id: 'tanim',       label: '1. Kesgitlemeler' },
  { id: 'kabul',       label: '2. Şertleriň Kabul Edilmegi' },
  { id: 'hesap',       label: '3. Hasap Açmak' },
  { id: 'icerik',      label: '4. Mazmun we Awtorlyk' },
  { id: 'yasaklar',    label: '5. Gadagan Hereketler' },
  { id: 'gizlilik',    label: '6. Gizlinlik' },
  { id: 'sorumluluk',  label: '7. Jogapkärçilik Çägi' },
  { id: 'fesih',       label: '8. Hasaby Ýatyrmak' },
  { id: 'degisiklik',  label: '9. Üýtgetmeler' },
  { id: 'iletisim',    label: '10. Habarlaşmak' },
]

const sections = [
  {
    id: 'tanim', num: '1', icon: 'mdi-book-open-outline', title: 'Kesgitlemeler',
    content: [
      'Bu Ulanyjy Şertlerinde geçýän "Platforma", "Hyzmat" ýa-da "Şygyr Geçelgesi" sözleri; web saýty, mobil goşundy we degişli ähli hyzmatlary öz içine alýar.',
      '"Ulanyjy" sözi platforma hasaba alnan ýa-da alynmadyk görnüşde girýän ähli fiziki şahslary; "Mazmun" bolsa ulanyjylaryň platforma ýükleýän her dürli teksti, şygry, teswiri we profil maglumatlaryny aňladýar.',
    ],
  },
  {
    id: 'kabul', num: '2', icon: 'mdi-handshake-outline', title: 'Şertleriň Kabul Edilmegi',
    content: [
      'Şygyr Geçelgesini ulanmaga başlan pursadyňyzdan bu şertleri okandygyňyzy, düşünendygiňizi we kabul edendygiňizi beýan eden bolýarsyňyz.',
      'Bu şertleri kabul etmeýän bolsaňyz, platformany ulanmagy bes ediň. 18 ýaşdan kiçi ulanyjylaryň platformany diňe ene-atasynyň ýa-da kanuny wekiliniň gözegçiligi astynda ulanmagy hökmandyr.',
    ],
    warning: 'Bu şertler hukuk taýdan baglaýjydyr. Düşünmeýän maddalaňyz üçin goldaw toparymyz bilen habarlaşyp bilersiňiz.',
  },
  {
    id: 'hesap', num: '3', icon: 'mdi-account-circle-outline', title: 'Hasap Açmak we Howpsuzlyk',
    content: [
      'Platforma hasaba durmak üçin azyndan 13 ýaşynda bolmagyňyz gerekdir. Hasaba duran wagtyňyz berýän maglumatyňyzyň dogry we täze bolmagy hökmandyr.',
      'Hasabyňyzyň howpsuzlygy diňe siziň jogapkärçiligiňizdir. Açar sözüňizi hiç kimsä aýtmaly dälsiňiz; hasabyňyza rugsat berilmedik giriş duýsaňyz, derhal bize habar bermelisiniz.',
    ],
    items: [
      'Her ulanyjy diňe bir hasap açyp biler.',
      'Başganyň şahsyýetine girişmek, galp şahsyýet döretmek kesinlikle gadagandyr.',
      'Hasabyňyzy başga birine geçirip ýa-da satyp bilmersiňiz.',
      'Şübheli giriş hereketlerini 48 sagadyň içinde habar bermek gerekdir.',
    ],
  },
  {
    id: 'icerik', num: '4', icon: 'mdi-pencil-outline', title: 'Mazmun we Awtorlyk Hukugy',
    content: [
      'Platforma ýükleýän şygyrlaryňyz we beýleki mazmunyňyz üzerindäki awtorlyk hukugy size degişlidir. Paýlaşmak bilen Şygyr Geçelgesine; mazmuny platforma çäginde görkezmek, paýlamak we mahabat maksatly ulanmak hukugyny mugt berýärsiňiz.',
      'Bu rugsat, mazmunyňyzy platformadan pozanyňyz bilen ýatyrylýar. Üçünji tarap mazmuny rugsat almadan paýlaşmak kesinlikle gadagandyr; bu bozulmadan gelip çykýan ähli jogapkärçilik ulanyjä degişlidir.',
    ],
    items: [
      'Başganyň şygyrlaryny çeşme görkezmezden paýlap bilmersiňiz.',
      'Emeli aň tarapyndan döredilen mazmunyň şeýle belliklenilmegi hökmandyr.',
      'Platforma ýüklenýän mazmunlar, çap edilmezden ozal jemgyýet standartlary barlagyna tabi tutulup bilner.',
      'Awtorlyk hukugynyň bozulmagy ýüze çykarylan mazmunlar, habar berilmezden aýrylyp bilner.',
    ],
  },
  {
    id: 'yasaklar', num: '5', icon: 'mdi-shield-alert-outline', title: 'Gadagan Hereketler',
    content: [
      'Platforma sungatyň we edebiýatyň ösmegine goşant goşmagy maksat edinýär. Bu maksada ters gelýän her dürli hereket kesinlikle gadagandyr.',
    ],
    items: [
      'Ýigrenç sözi, jins, din, jyns ýa-da etnik gelip çykyş esasyndaky kemsidiji mazmun paýlaşmak.',
      'Kemsitmek, haýbat atmak ýa-da zorlamak häsiýetli habarlar ibermek.',
      'Aldawly, galp ýa-da bilkastlaýyn ýalňyş maglumat ýaýratmak.',
      'Spam, awtomatik bot ýa-da zyýanly programma ulanmak.',
      'Platformanyň tehniki düzümine zyýan ýetirmäge synanşmak.',
      'Ulanyjylaryň şahsy maglumatlaryny razylyksyz toplamak ýa-da işlemek.',
      'Seksual ýa-da çagalary ezýet çekdirýän her dürli mazmun paýlaşmak.',
    ],
    warning: 'Bu düzgünleri bozýan ulanyjylaryň hasaplary, öňünden habar berilmezden togtadylyp ýa-da hemişelik ýapylyp bilner.',
  },
  {
    id: 'gizlilik', num: '6', icon: 'mdi-shield-lock-outline', title: 'Gizlinlik',
    content: [
      'Şahsy maglumatlaryňyzyň nähili toplanýandygy, işlenýändigi we goralýandygy barada jikme-jik maglumat Gizlinlik Syýasatymyzda berilýär.',
      'Şygyr Geçelgesi, güýçdäki Şahsy Maglumatlary Goramak Kanuny (KVKK) we Ýewropa Umumy Maglumat Goragy Düzgünnamasy (GDPR) çägindäki borçlaryny ýerine ýetirmegi üstüne alýar.',
    ],
  },
  {
    id: 'sorumluluk', num: '7', icon: 'mdi-scale-balance', title: 'Jogapkärçilik Çägi',
    content: [
      'Şygyr Geçelgesi, platforma üzerindäki ulanyjy mazmunynyň dogrulygy, kanunylygy ýa-da laýyklygy barada hiç hili kepillik bermeýär.',
      'Platforma, tehniki näsazlyklar, maglumat ýitgileri ýa-da üçünji tarap hyzmatlaryndan gelip çykýan kesilmeler sebäpli ýetirilen gytaklaýyn zyýanlar üçin jogapkär tutulmaýar.',
    ],
    items: [
      'Hyzmat kesilmeleri we maglumat ýitgilerinden gelip çykýan zyýanlar.',
      'Ulanyjylar arasyndaky jedel we bozulmalardan gelip çykýan talaplara.',
      'Üçünji tarap baglanyşyk we hyzmatlardan gelip çykýan zyýanlar.',
    ],
  },
  {
    id: 'fesih', num: '8', icon: 'mdi-account-off-outline', title: 'Hasaby Ýatyrmak',
    content: [
      'Hasabyňyzy islän wagtyňyz we hiç hili sebäp görkezmezden pozup bilersiňiz. Hasap pozulmagy bilen ähli mazmunyňyz hemişelik aýrylar.',
      'Şygyr Geçelgesi, bu şertleri bozan diýlip ykrar edilen hasaplary öňünden habar bermezden ýatyryp biler. Agyr bozulma ýagdaýlarynda degişli hukuk edaralaryna habar berip bolar.',
    ],
  },
  {
    id: 'degisiklik', num: '9', icon: 'mdi-refresh', title: 'Şertlerde Üýtgetmeler',
    content: [
      'Şygyr Geçelgesi, bu şertleri öňünden habar bermek bilen üýtgetmek hukugyny özünde saklaýar. Edilen täzelemeler, e-poçta bildirişi ýa-da platforma yglan arkaly ulanyjylara ýetiriler.',
      'Üýtgetme güýje girensoň platformany ulanmaga dowam etmegiňiz, täzelenen şertleri kabul edendgiňiz manysyna gelýär.',
    ],
  },
  {
    id: 'iletisim', num: '10', icon: 'mdi-email-outline', title: 'Habarlaşmak',
    content: [
      'Bu şertler bilen baglanyşykly sorag, pikir ýa-da şikaýatlaryňyz üçin aşakdaky kanallar arkaly bize ýüz tutup bilersiňiz.',
    ],
    items: [
      'E-poçta: goldaw@sygyrgecelgesi.com',
      'Hukuk bildirişleri: hukuk@sygyrgecelgesi.com',
      'Iş sagatlary: Iş günleri 09:00 – 18:00 (TM wagty)',
      'Poçta salgysy: Şygyr Geçelgesi A.Ş., Aşgabat, Türkmenistan',
    ],
  },
]

// Scroll spy
const onScroll = () => {
  for (let i = tocItems.length - 1; i >= 0; i--) {
    const el = document.getElementById(tocItems[i].id)
    if (el && el.getBoundingClientRect().top <= 120) {
      activeSection.value = tocItems[i].id
      break
    }
  }
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>