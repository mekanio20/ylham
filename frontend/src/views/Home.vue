<template>
  <main class="min-h-screen bg-[#FAFAF7] font-garamond">

    <!-- Hero Banner -->
    <div class="bg-[#1C1C1E] text-[#F5F0E8] py-10 px-4 text-center relative overflow-hidden">
      <div class="absolute inset-0 opacity-10"
        style="background-image: repeating-linear-gradient(0deg, transparent, transparent 39px, #F5F0E8 39px, #F5F0E8 40px), repeating-linear-gradient(90deg, transparent, transparent 39px, #F5F0E8 39px, #F5F0E8 40px);">
      </div>
      <h1 class="text-4xl md:text-6xl tracking-tight text-[#A8896C] mb-4 font-garamond font-light italic">
        Ylham
      </h1>
      <p class="text-sm text-[#8A8A8A] max-w-md mx-auto font-dm font-light">
        Ähli zat öz wagtyna garaşar!
      </p>
    </div>

    <!-- Tabs Bar -->
    <div class="border-b border-[#E5E0D8] bg-[#FAFAF7] sticky top-0 z-10">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center gap-x-5 overflow-x-auto no-scrollbar">
        <button
          v-for="tab in tabList"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'py-4 tracking-widest uppercase transition-all duration-200 border-b-2 -mb-px text-nowrap font-dm font-medium text-[12px]',
            activeTab === tab.id
              ? 'border-[#1C1C1E] text-[#1C1C1E]'
              : 'border-transparent text-[#9A9A8A] hover:text-[#1C1C1E]'
          ]"
        >
          {{ tab.label }}
        </button>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex flex-col lg:flex-row gap-10">

        <!-- Poem Feed -->
        <div class="flex-1 min-w-0">

          <!-- Featured Poem (1-nji Goşgy) -->
          <div v-if="activeTab === 'newest' && highlightStore.dailyPoem" class="mb-8">
            <div class="relative bg-[#1C1C1E] rounded-2xl overflow-hidden p-8 md:p-12 group cursor-pointer"
              @click="$router.push({ name: 'PoemDetail', params: { id: highlightStore.dailyPoem.id } })">
              <!-- Decorative lines -->
              <div class="absolute top-0 left-0 w-px h-full bg-gradient-to-b from-transparent via-[#A8896C] to-transparent opacity-40"></div>
              <div class="absolute top-0 right-0 w-px h-full bg-gradient-to-b from-transparent via-[#A8896C] to-transparent opacity-20"></div>

              <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-5 font-dm">Günüň Goşgysy</p>

              <h2 class="text-3xl md:text-4xl font-light text-[#F5F0E8] mb-6 leading-tight group-hover:text-[#A8896C] transition-colors duration-300 font-garamond">
                {{ highlightStore.dailyPoem.title }}
              </h2>

              <!-- Goşgy -->
              <div class="mb-6 space-y-1.5 border-l-2 border-[#A8896C] pl-5">
                <p v-for="(line, i) in previewLines" :key="i"
                  class="text-[#C8BFB0] text-base leading-relaxed font-garamond italic">
                  {{ line }}
                </p>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <img :src="highlightStore.dailyPoem.author?.avatar || '/poet_images/default.webp'" class="w-8 h-8 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#1C1C1E]" />
                  <div>
                    <p class="text-[#F5F0E8] text-sm font-medium font-dm">{{ highlightStore.dailyPoem.author.username }}</p>
                    <p class="text-[#6B6360] text-xs font-dm">{{ formatDateTk(highlightStore.dailyPoem.created_at) }}</p>
                  </div>
                </div>
                <div class="flex items-center gap-4 text-[#6B6360]">
                  <span class="flex items-center gap-1 text-xs font-dm">
                    <v-icon size="14" icon="mdi-heart-outline" class="text-[#A8896C]" />
                    {{ highlightStore.dailyPoem.like_count }}
                  </span>
                  <span class="flex items-center gap-1 text-xs font-dm">
                    <v-icon size="14" icon="mdi-comment-outline" />
                    {{ highlightStore.dailyPoem.comment_count }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Poem Cards List -->
          <div class="flex flex-col space-y-7 pb-10">
            <PoemCard v-for="poem in poemStore.poems" :key="poem.id" :poem="poem" />
          </div>

          <!-- Daha fazla yükle -->
          <div class="text-center">
            <button class="px-8 py-3 border border-[#1C1C1E] text-[#1C1C1E] rounded-full text-sm hover:bg-[#1C1C1E] hover:text-[#F5F0E8] transition-all duration-300 font-dm text-[12px]">
              Dowamyny ýükle
            </button>
          </div>
        </div>

        <!-- Sağ Sidebar -->
        <aside class="lg:w-72 shrink-0">
          <div class="lg:sticky lg:top-20 space-y-8">

            <!-- Kategoriýalar -->
            <div>
              <h3 class="text-xs font-semibold text-[#1C1C1E] mb-4 tracking-widest uppercase font-dm">Kategoriýalar</h3>
              <div class="flex flex-wrap gap-2">
                <button
                  v-for="c in categoryStore.categories"
                  :key="c.id"
                  :class="[
                    'px-3 py-1.5 rounded-full text-xs transition-all duration-200 border font-dm',
                    activeCategory === c
                      ? 'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]'
                      : 'bg-transparent text-[#6B6B5A] border-[#D9D0C4] hover:border-[#1C1C1E] hover:text-[#1C1C1E]'
                  ]"
                  @click="activeCategory = activeCategory === c ? null : c"
                >
                  {{ c.name }}
                </button>
              </div>
            </div>

            <!-- Divider -->
            <div class="border-t border-[#EAE5DC]"></div>

            <!-- Günün Şairi -->
            <div>
              <h3 class="text-xs font-semibold text-[#1C1C1E] mb-4 tracking-widest uppercase flex items-center gap-1.5 font-dm">
                <v-icon size="13" icon="mdi-star-four-points" class="text-[#A8896C]" />
                Günün Şairi
              </h3>
              <div class="flex items-start gap-3">
                <img :src="poetOfDay.avatar" :alt="poetOfDay.name" class="w-11 h-11 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#FAFAF7]" />
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-medium text-[#1C1C1E] font-dm">{{ poetOfDay.name }}</p>
                  <p class="text-xs text-[#9A9A8A] mb-2 font-dm">{{ poetOfDay.poems }} Goşgy</p>
                  <p class="text-sm text-[#6B6050] leading-relaxed font-garamond italic text-[15px]">
                    "{{ poetOfDay.quote }}"
                  </p>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <div class="border-t border-[#EAE5DC]"></div>

            <!-- Trend Goşgyler -->
            <div>
              <h3 class="text-xs font-semibold text-[#1C1C1E] mb-5 tracking-widest uppercase flex items-center gap-1.5 font-dm">
                <v-icon size="13" icon="mdi-fire" class="text-[#A8896C]" />
                Trend
              </h3>
              <div class="space-y-5">
                <div v-for="(item, idx) in trending" :key="item.id" class="flex gap-3 group cursor-pointer">
                  <span class="text-2xl font-bold text-[#E8E3D9] tabular-nums leading-none mt-0.5 shrink-0 w-7 font-garamond">
                    {{ String(idx + 1).padStart(2, '0') }}
                  </span>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-1.5 mb-1">
                      <img :src="item.avatar" :alt="item.author" class="w-4 h-4 rounded-full" />
                      <span class="text-xs text-[#A0988A] font-dm">{{ item.author }} · {{ item.date }}</span>
                    </div>
                    <router-link :to="{ name: 'PoemDetail', params: { id: item.id } }"
                      class="text-sm text-[#2A2A1E] group-hover:text-[#A8896C] transition-colors line-clamp-2 leading-snug font-garamond text-[15px]">
                      {{ item.title }}
                    </router-link>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </aside>
      </div>
    </div>
  </main>
</template>

<script setup>
import { formatDateTk } from '@/composables/useFormat'
const highlightStore = useHighlightsStore()
const categoryStore = useCategoryStore()
const poemStore = usePoemStore()
const activeTab = ref('newest')
const activeCategory = ref(null)

const previewLines = computed(() => highlightStore.dailyPoem.content_preview.split('\n').filter(l => l.trim()).slice(0, 4))

const tabList = ref([
  { id: 'newest', label: 'Täze goşgular' },
  { id: 'top_readed', label: 'Iň köp okalanlar' },
  { id: 'top_liked', label: 'Iň köp halananlar' },
  { id: 'admin_liked', label: 'Adminiň halanlary' },
])

const poetOfDay = ref({
  name: 'Leyla Narin',
  poems: 43,
  avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99',
  quote: 'Kelimeler, ruhun bıraktığı izlerdir.',
})

const trending = ref([
  {
    id: 1,
    title: 'Gece Yarısı Şehri',
    author: 'Leyla Narin',
    date: '8 Mar',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99',
    bg_image: '/poem_images/dag.webp'
  },
  {
    id: 3,
    title: 'Hafıza Kırıkları',
    author: 'Can Demirci',
    date: '5 Mar',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=can3',
    bg_image: '/poem_images/dag.webp'
  },
  {
    id: 2,
    title: 'Deniz Kenarında Bir Öğle',
    author: 'Selin Çelik',
    date: '6 Mar',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=selin2',
    bg_image: '/poem_images/dag.webp'
  },
  {
    id: 4,
    title: 'Sessiz Şehir',
    author: 'Naz Kaya',
    date: '4 Mar',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=naz4',
    bg_image: '/poem_images/dag.webp'
  },
])

onMounted(async () => {
  await poemStore.fetchPoems({ ordering: '-created_at' })
  await categoryStore.fetchCategories()
  await highlightStore.fetchHighlights({ period: 'daily' })
})
</script>