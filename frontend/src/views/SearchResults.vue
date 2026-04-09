<template>
  <main class="min-h-screen bg-[#FAFAF7]" style="font-family: 'Cormorant Garamond', Georgia, serif;">

    <component :is="'link'" rel="preconnect" href="https://fonts.googleapis.com" />
    <component :is="'link'" rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500&display=swap" />

    <!-- Search Header -->
    <div class="border-b border-[#EAE5DC] bg-[#FAFAF7] px-4 sm:px-6 lg:px-8 py-5 sm:py-7">
      <div class="max-w-4xl mx-auto">

        <!-- Arama Kutusu -->
        <div class="relative mb-5 sm:mb-6">
          <span class="absolute left-4 top-1/2 -translate-y-1/2 text-[#B0A898]">
            <v-icon size="20" icon="mdi-magnify" />
          </span>
          <input
            v-model="query"
            type="text"
            placeholder="Goşgy, şair, tema ara..."
            class="w-full pl-12 pr-12 py-3 sm:py-3.5 bg-[#F0EBE1] rounded-2xl text-[#1C1C1E] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C] transition-all text-base"
            style="font-family: 'DM Sans', sans-serif; font-size: 15px;"
            @input="onSearch"
          />
          <button v-if="query" @click="query = ''; onSearch()"
            class="absolute right-4 top-1/2 -translate-y-1/2 text-[#B0A898] hover:text-[#1C1C1E] transition-colors">
            <v-icon size="18" icon="mdi-close" />
          </button>
        </div>

        <!-- Tabs -->
        <div class="flex items-center gap-0 border-b border-[#EAE5DC] -mb-px">
          <button
            v-for="tab in tabs"
            :key="tab.id"
            @click="activeTab = tab.id"
            :class="[
              'flex items-center gap-2 px-4 py-2.5 text-xs border-b-2 -mb-px transition-all duration-200',
              activeTab === tab.id
                ? 'border-[#1C1C1E] text-[#1C1C1E]'
                : 'border-transparent text-[#9A9A8A] hover:text-[#1C1C1E]'
            ]"
            style="font-family: 'DM Sans', sans-serif; letter-spacing: 0.1em; text-transform: uppercase; font-size: 11px; font-weight: 500;"
          >
            <v-icon size="14" :icon="tab.icon" />
            {{ tab.label }}
            <span v-if="tab.count !== null"
              class="px-1.5 py-0.5 rounded-full text-xs font-semibold"
              :class="activeTab === tab.id ? 'bg-[#1C1C1E] text-[#F5F0E8]' : 'bg-[#EDE8E0] text-[#6B5E4E]'"
              style="font-size: 10px;">
              {{ tab.count }}
            </span>
          </button>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">

      <!-- Boş sorgu hali -->
      <div v-if="!query.trim()" class="text-center py-20">
        <div class="w-16 h-16 rounded-full bg-[#F0EBE1] flex items-center justify-center mx-auto mb-5">
          <v-icon size="30" icon="mdi-magnify" class="text-[#C8B89A]" />
        </div>
        <p class="text-xl text-[#1C1C1E] mb-2" style="font-family: 'Cormorant Garamond', serif; font-style: italic;">
          Ne aramak istersin?
        </p>
        <p class="text-sm text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">
          Goşgy başlığı, şair adı veya tema yazabilirsin
        </p>

        <!-- Popüler temalar -->
        <div class="mt-8">
          <p class="text-xs tracking-widest uppercase text-[#A8896C] mb-4" style="font-family: 'DM Sans', sans-serif;">Popüler Temalar</p>
          <div class="flex flex-wrap justify-center gap-2">
            <button
              v-for="tag in popularTags"
              :key="tag"
              @click="query = tag; onSearch()"
              class="px-4 py-2 rounded-full border border-[#D9D0C4] text-[#6B6B5A] text-sm hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-all"
              style="font-family: 'DM Sans', sans-serif; font-size: 12px;">
              {{ tag }}
            </button>
          </div>
        </div>
      </div>

      <!-- Yükleniyor -->
      <div v-else-if="loading" class="space-y-4 py-4">
        <div v-for="i in 4" :key="i" class="bg-white rounded-2xl border border-[#EAE5DC] p-5 animate-pulse">
          <div class="flex gap-4">
            <div class="w-10 h-10 rounded-full bg-[#F0EBE1] shrink-0"></div>
            <div class="flex-1 space-y-2.5">
              <div class="h-4 bg-[#F0EBE1] rounded-full w-2/3"></div>
              <div class="h-3 bg-[#F0EBE1] rounded-full w-1/2"></div>
              <div class="h-3 bg-[#F0EBE1] rounded-full w-3/4"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sonuç yok -->
      <div v-else-if="activeTab === 'all' && filteredPoems.length === 0 && filteredUsers.length === 0" class="text-center py-20">
        <div class="w-16 h-16 rounded-full bg-[#F0EBE1] flex items-center justify-center mx-auto mb-5">
          <v-icon size="28" icon="mdi-text-search" class="text-[#C8B89A]" />
        </div>
        <p class="text-xl text-[#1C1C1E] mb-2" style="font-family: 'Cormorant Garamond', serif; font-style: italic;">
          "{{ query }}" için sonuç bulunamadı
        </p>
        <p class="text-sm text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">Farklı anahtar kelimeler deneyebilirsin</p>
      </div>

      <!-- ══ TÜMÜ ══ -->
      <div v-else-if="activeTab === 'all'" class="space-y-8">

        <!-- Kullanıcı Sonuçları (max 3) -->
        <div v-if="filteredUsers.length > 0">
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-xs tracking-widest uppercase text-[#A8896C]"
              style="font-family: 'DM Sans', sans-serif;">Şairler</h2>
            <button v-if="filteredUsers.length > 3" @click="activeTab = 'users'"
              class="text-xs text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors flex items-center gap-1"
              style="font-family: 'DM Sans', sans-serif;">
              Tümünü gör <v-icon size="13" icon="mdi-arrow-right" />
            </button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <UserCard
              v-for="user in filteredUsers.slice(0,3)"
              :key="user.id"
              :user="user"
              @follow="toggleFollow(user)"
            />
          </div>
        </div>

        <!-- Goşgy Sonuçları -->
        <div v-if="filteredPoems.length > 0">
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-xs tracking-widest uppercase text-[#A8896C]"
              style="font-family: 'DM Sans', sans-serif;">Goşgyler</h2>
            <button v-if="filteredPoems.length > 4" @click="activeTab = 'poems'"
              class="text-xs text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors flex items-center gap-1"
              style="font-family: 'DM Sans', sans-serif;">
              Tümünü gör <v-icon size="13" icon="mdi-arrow-right" />
            </button>
          </div>
          <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden divide-y divide-[#F0EBE1]">
            <PoemRow
              v-for="poem in filteredPoems.slice(0,4)"
              :key="poem.id"
              :poem="poem"
              :query="query"
            />
          </div>
        </div>
      </div>

      <!-- ══ ŞİİRLER ══ -->
      <div v-else-if="activeTab === 'poems'">
        <!-- Sıralama -->
        <div class="flex items-center justify-between mb-4">
          <p class="text-sm text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">
            <span class="text-[#1C1C1E] font-medium">{{ filteredPoems.length }}</span> Goşgy bulundu
          </p>
          <div class="flex items-center gap-2">
            <span class="text-xs text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">Sırala:</span>
            <button
              v-for="s in sortOptions"
              :key="s.id"
              @click="sortBy = s.id"
              :class="[
                'px-3 py-1 rounded-full text-xs border transition-all',
                sortBy === s.id ? 'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]' : 'border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E]'
              ]"
              style="font-family: 'DM Sans', sans-serif;">{{ s.label }}</button>
          </div>
        </div>

        <div v-if="filteredPoems.length === 0" class="text-center py-16">
          <v-icon size="36" icon="mdi-book-off-outline" class="text-[#D9D0C4] mb-3" />
          <p class="text-sm text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">Goşgy bulunamadı</p>
        </div>
        <div v-else class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden divide-y divide-[#F0EBE1]">
          <PoemRow
            v-for="poem in sortedPoems"
            :key="poem.id"
            :poem="poem"
            :query="query"
          />
        </div>
      </div>

      <!-- ══ KULLANICILAR ══ -->
      <div v-else-if="activeTab === 'users'">
        <p class="text-sm text-[#9A9A8A] mb-4" style="font-family: 'DM Sans', sans-serif;">
          <span class="text-[#1C1C1E] font-medium">{{ filteredUsers.length }}</span> şair bulundu
        </p>

        <div v-if="filteredUsers.length === 0" class="text-center py-16">
          <v-icon size="36" icon="mdi-account-off-outline" class="text-[#D9D0C4] mb-3" />
          <p class="text-sm text-[#9A9A8A]" style="font-family: 'DM Sans', sans-serif;">Kullanıcı bulunamadı</p>
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <UserCard
            v-for="user in filteredUsers"
            :key="user.id"
            :user="user"
            @follow="toggleFollow(user)"
          />
        </div>
      </div>

    </div>
  </main>
</template>

<!-- ══════════════════════════════════════════════
     PoemRow Alt Bileşeni
══════════════════════════════════════════════ -->
<script>
import { defineComponent, h, computed } from 'vue'

const PoemRow = defineComponent({
  name: 'PoemRow',
  props: {
    poem: Object,
    query: String,
  },
  setup(props) {
    const highlight = (text) => {
      if (!props.query || !text) return text
      const escaped = props.query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
      const regex = new RegExp(`(${escaped})`, 'gi')
      return text.replace(regex, '<mark style="background:#FFF3CD;color:#1C1C1E;border-radius:2px;padding:0 1px;">$1</mark>')
    }
    return { highlight }
  },
  template: `
    <router-link :to="{ name: 'PoemDetail', params: { id: poem.id } }"
      class="flex items-start gap-3 sm:gap-4 px-4 sm:px-6 py-4 sm:py-5 hover:bg-[#FAFAF7] transition-colors group block">
      <div class="w-9 h-9 rounded-xl bg-[#F0EBE1] flex items-center justify-center text-[#C8B89A] shrink-0 text-xl"
        style="font-family:'Cormorant Garamond',serif;font-style:italic;">"</div>
      <div class="flex-1 min-w-0">
        <h3 class="text-base sm:text-lg text-[#1C1C1E] group-hover:text-[#A8896C] transition-colors mb-1 leading-snug"
          style="font-family:'Cormorant Garamond',serif;font-weight:400;"
          v-html="highlight(poem.title)"></h3>
        <p class="text-sm text-[#7A7060] line-clamp-2 mb-2.5 leading-relaxed"
          style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:14px;"
          v-html="highlight(poem.preview)"></p>
        <div class="flex items-center gap-2 flex-wrap">
          <img :src="poem.authorAvatar" class="w-5 h-5 rounded-full" />
          <span class="text-xs text-[#6B6B5A]" style="font-family:'DM Sans',sans-serif;"
            v-html="highlight(poem.author)"></span>
          <span class="text-[#C8C0B0] text-xs">·</span>
          <span class="text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">{{ poem.date }}</span>
          <span class="inline-flex px-2 py-0.5 bg-[#EDE8E0] text-[#6B5E4E] rounded-full text-xs ml-1"
            style="font-family:'DM Sans',sans-serif;font-size:10px;">{{ poem.category }}</span>
          <div class="ml-auto flex items-center gap-3 text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">
            <span class="flex items-center gap-1"><v-icon size="12" icon="mdi-heart-outline"/>{{ poem.likes }}</span>
            <span class="hidden sm:flex items-center gap-1"><v-icon size="12" icon="mdi-comment-outline"/>{{ poem.comments }}</span>
          </div>
        </div>
      </div>
    </router-link>
  `
})

const UserCard = defineComponent({
  name: 'UserCard',
  props: {
    user: Object,
  },
  emits: ['follow'],
  template: `
    <div class="bg-white rounded-2xl border border-[#EAE5DC] p-4 sm:p-5 flex items-start gap-3 hover:shadow-sm transition-shadow">
      <router-link :to="{ name: 'UserProfile', params: { username: user.username } }" class="shrink-0">
        <img :src="user.avatar" :alt="user.name" class="w-11 h-11 rounded-full ring-1 ring-[#EAE5DC] hover:ring-[#A8896C] transition-all" />
      </router-link>
      <div class="flex-1 min-w-0">
        <router-link :to="{ name: 'UserProfile', params: { username: user.username } }">
          <p class="text-sm font-medium text-[#1C1C1E] truncate hover:text-[#A8896C] transition-colors"
            style="font-family:'DM Sans',sans-serif;">{{ user.name }}</p>
          <p class="text-xs text-[#9A9A8A] mb-1.5" style="font-family:'DM Sans',sans-serif;">@{{ user.username }}</p>
        </router-link>
        <p class="text-xs text-[#7A7060] line-clamp-2 mb-2.5 leading-relaxed italic"
          style="font-family:'Cormorant Garamond',serif;font-size:13px;">{{ user.bio }}</p>
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3 text-xs text-[#9A9A8A]" style="font-family:'DM Sans',sans-serif;">
            <span><span class="font-medium text-[#1C1C1E]">{{ user.poems }}</span> Goşgy</span>
            <span><span class="font-medium text-[#1C1C1E]">{{ user.followers }}</span> takipçi</span>
          </div>
          <button @click="$emit('follow', user)"
            :class="[
              'px-3 py-1 rounded-full text-xs border transition-all shrink-0',
              user.following
                ? 'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]'
                : 'border-[#D9D0C4] text-[#6B6B5A] hover:border-[#1C1C1E] hover:text-[#1C1C1E]'
            ]"
            style="font-family:'DM Sans',sans-serif;font-size:11px;">
            {{ user.following ? '✓ Takip' : 'Takip Et' }}
          </button>
        </div>
      </div>
    </div>
  `
})

export default { components: { PoemRow, UserCard } }
</script>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const query = ref(route.query?.q || '')
const activeTab = ref('all')
const sortBy = ref('relevant')
const loading = ref(false)

const sortOptions = [
  { id: 'relevant', label: 'İlgili' },
  { id: 'newest',   label: 'Yeni'   },
  { id: 'popular',  label: 'Popüler'},
]

const popularTags = ['Aşk', 'Melankoli', 'Doğa', 'Şehir', 'Özgürlük', 'Hüzün', 'İç Dünya', 'Umut']

// ── Mock veri ──
const allPoems = ref([
  { id:1,  title:'Gece Yarısı Şehri',       preview:'Işıklar sönmez bu şehirde hiç, her köşede bir yalnızlık bekler seni.',     author:'Leyla Narin',  authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99', date:'8 Mar',  category:'Şehir',    likes:248, comments:34, },
  { id:2,  title:'Sonbaharda Kaybolmak',     preview:'Yapraklar düşer, ben de seninle... Rüzgar taşır adını uzaklara.',            author:'Mete Aydın',   authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=mete1',   date:'5 Mar',  category:'Aşk',      likes:189, comments:21, },
  { id:3,  title:'Hafıza Kırıkları',         preview:'Hatırlamak acıtır bazen, unutmak daha da fazla. İkisi arasında gidip gelirim.', author:'Can Demirci',  authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=can3',    date:'1 Mar',  category:'İç Dünya', likes:201, comments:45, },
  { id:4,  title:'Deniz Kenarında Bir Öğle', preview:'Martılar bağırır gökyüzüne, tuzlu rüzgar yüzümü yakar.',                     author:'Selin Çelik',  authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=selin2',  date:'28 Şub', category:'Doğa',     likes:134, comments:18, },
  { id:5,  title:'Kıyıda Bekleyiş',          preview:'Umut bir gemi gibi, ufukta gözüküp kaybolan.',                               author:'Naz Kaya',     authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=naz4',    date:'22 Şub', category:'Melankoli',likes:97,  comments:12, },
  { id:6,  title:'Beyaz Sessizlik',          preview:'Kar yağar üstüme, sesimi yutar. Yalnız kalır ayak izlerim.',                  author:'Leyla Narin',  authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99', date:'14 Şub', category:'Doğa',     likes:156, comments:29, },
  { id:7,  title:'Aşkın Geometrisi',         preview:'İki paralel çizgi hiç kesişmez dediler, biz yine de denedik.',               author:'Ali Kara',     authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=ali5',    date:'10 Şub', category:'Aşk',      likes:312, comments:56, },
  { id:8,  title:'Şehrin Gürültüsü',         preview:'Milyonların arasında yürürüm, ses yok içimde. Sadece şehir bağırır.',        author:'Cem Yılmaz',   authorAvatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=cem7',    date:'3 Şub',  category:'Şehir',    likes:78,  comments:9,  },
])

const allUsers = ref([
  { id:1, name:'Leyla Narin',  username:'leylanarin', bio:'Kelimeler ruhun bıraktığı izlerdir. İstanbul gecelerinde Goşgy yazarım.', poems:43, followers:'1.2B', following:false, avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=leyla99' },
  { id:2, name:'Mete Aydın',   username:'meteaydin',  bio:'Aşk ve doğa üzerine Goşgyler. Bazen melankoli, bazen umut.',              poems:28, followers:384,   following:true,  avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=mete1'   },
  { id:3, name:'Selin Çelik',  username:'selincelik', bio:'Deniz kıyısında yaşıyorum, Goşgylerim de orada.',                          poems:17, followers:215,   following:false, avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=selin2'  },
  { id:4, name:'Can Demirci',  username:'candomirci', bio:'İç dünya şairi. Sessizliğin sesini yazıyorum.',                          poems:35, followers:612,   following:false, avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=can3'    },
  { id:5, name:'Naz Kaya',     username:'nazkaya',    bio:'Melankoli ve umut arasındaki ince çizgide.',                             poems:22, followers:298,   following:true,  avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=naz4'    },
  { id:6, name:'Ali Kara',     username:'alikara',    bio:'Geometrik Goşgyler yazan matematikçi bir şair.',                         poems:11, followers:145,   following:false, avatar:'https://api.dicebear.com/7.x/avataaars/svg?seed=ali5'    },
])

// ── Arama filtresi ──
const filteredPoems = computed(() => {
  if (!query.value.trim()) return allPoems.value
  const q = query.value.toLowerCase()
  return allPoems.value.filter(p =>
    p.title.toLowerCase().includes(q) ||
    p.preview.toLowerCase().includes(q) ||
    p.author.toLowerCase().includes(q) ||
    p.category.toLowerCase().includes(q)
  )
})

const filteredUsers = computed(() => {
  if (!query.value.trim()) return allUsers.value
  const q = query.value.toLowerCase()
  return allUsers.value.filter(u =>
    u.name.toLowerCase().includes(q) ||
    u.username.toLowerCase().includes(q) ||
    u.bio.toLowerCase().includes(q)
  )
})

const sortedPoems = computed(() => {
  const list = [...filteredPoems.value]
  if (sortBy.value === 'newest')  return list.sort((a, b) => b.id - a.id)
  if (sortBy.value === 'popular') return list.sort((a, b) => b.likes - a.likes)
  return list
})

// ── Tab sayaçları ──
const tabs = computed(() => [
  { id:'all',   label:'Tümü',     icon:'mdi-magnify',                 count: filteredPoems.value.length + filteredUsers.value.length },
  { id:'poems', label:'Goşgyler',  icon:'mdi-book-open-page-variant-outline', count: filteredPoems.value.length },
  { id:'users', label:'Şairler',  icon:'mdi-account-multiple-outline', count: filteredUsers.value.length },
])

// ── Arama tetikleyici ──
let searchTimer = null
const onSearch = () => {
  loading.value = true
  clearTimeout(searchTimer)
  searchTimer = setTimeout(() => { loading.value = false }, 300)
}

const toggleFollow = (user) => { user.following = !user.following }

// Route'dan sorgu değişirse güncelle
watch(() => route.query?.q, (val) => {
  if (val) { query.value = val; onSearch() }
})
</script>