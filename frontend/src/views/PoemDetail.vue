<template>
  <main class="min-h-screen bg-[#FAFAF7] relative">

    <!-- Back Nav -->
    <div class="border-b border-[#EAE5DC] bg-[#FAFAF7]">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center gap-4 py-3.5">
        <button @click="$router.back()"
          class="flex items-center gap-1.5 text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors font-dm text-sm">
          <v-icon size="14" icon="mdi-arrow-left" />
          Yza
        </button>
        <div class="flex-1"></div>
        <button class="rounded-full text-[#9A9A8A] hover:text-[#1C1C1E] transition-all">
          <v-icon size="18" icon="mdi-dots-horizontal" />
        </button>
      </div>
    </div>

    <div class="fixed top-10 left-4">
        <ErrorMessage :errorMsg="errorMsg" />
    </div>

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-14">
      <div class="flex flex-col">
        <!-- Poem Header -->
        <div>
          <!-- Category badge -->
          <div class="mb-5">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs bg-[#EDE8E0] text-[#6B5E4E] font-dm">
              {{ poem_detail.category?.name }}
            </span>
          </div>

          <!-- Poem Title + Music Button -->
          <div class="flex items-start justify-between gap-4 mb-8">
            <h1 class="text-3xl md:text-4xl lg:text-5xl text-[#1C1C1E] leading-tight font-garamond">
              {{ poem_detail.title }}
            </h1>

            <!-- Music Button (only shown if poem_detail.background_music exists) -->
            <button @click="toggleMusic" :title="isMuted ? 'Sazy aç' : 'Sazy ýap'" :class="[
              'shrink-0 mt-2 w-11 h-11 rounded-full flex items-center justify-center transition-all duration-300',
              isMuted
                ? 'bg-[#EDE8E0] text-[#B0A898] hover:bg-[#E0D9CE] hover:text-[#A8896C]'
                : 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] shadow-md'
            ]">
              <span :class="{ 'music-spin': !isMuted }" class="flex items-center justify-center">
                <v-icon size="18" :icon="isMuted ? 'mdi-music-off' : 'mdi-music'" />
              </span>
            </button>
          </div>

          <!-- Hidden audio element -->
          <audio v-if="poem_detail.background_music" ref="audioRef" :src="poem_detail.music" loop></audio>

          <!-- Author Row -->
          <div class="flex items-center gap-3 mb-8 pb-8 border-b border-[#EAE5DC]">
            <img :src="poem_detail.author?.avatar || '/poet_images/default.webp'" :alt="poem_detail.author?.name"
              class="w-11 h-11 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#FAFAF7] object-cover" />
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-[#1C1C1E] font-dm">
                {{ poem_detail.author?.username }}
              </p>
              <p class="text-xs text-[#9A9A8A] font-dm">
                {{ formatDateTk(poem_detail.created_at) }}
              </p>
            </div>
            <button :class="[
              'px-4 py-1.5 rounded-full text-xs border transition-all duration-200 font-dm',
              isFollowing
                ? 'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]'
                : 'bg-transparent text-[#1C1C1E] border-[#1C1C1E] hover:bg-[#1C1C1E] hover:text-[#F5F0E8]'
            ]" @click="isFollowing = !isFollowing">
              {{ isFollowing ? 'Yzarlanýar' : 'Yzarla' }}
            </button>
          </div>
        </div>

        <div class="flex flex-col lg:flex-row gap-12">
          <!-- Poem Main Content -->
          <div class="flex-1 min-w-0 max-w-2xl">

            <!-- The Poem Body -->
            <div class="poem-body relative">

              <div class="whitespace-pre-wrap leading-relaxed font-garamond text-[#2A2418] text-lg">
                {{ poem_detail.content }}
              </div>

              <!-- Closing ornament -->
              <div class="mt-6 flex items-center gap-3">
                <div class="flex-1 h-px bg-[#EAE5DC]"></div>
                <span class="text-[#C8B89A] text-lg font-garamond">❧</span>
                <div class="flex-1 h-px bg-[#EAE5DC]"></div>
              </div>
            </div>

            <!-- Şahyryň Belligi -->
            <div class="bg-[#F0EBE1] rounded-xl p-5 mb-8" v-if="poem_detail.poem_note">
              <p class="text-xs tracking-widest uppercase text-[#A8896C] mb-1.5 font-dm">Şahyryň Belligi</p>
              <p class="text-sm text-[#5A5040] leading-relaxed font-garamond italic">
                {{ poem_detail.poem_note }}
              </p>
            </div>

            <!-- Action Bar -->
            <div class="flex items-center gap-2 mt-2 pb-5 border-b border-[#EAE5DC] mb-6">
              <button @click="toggleLike" :class="[
                'flex items-center gap-2 px-4 py-2 rounded-full text-sm border transition-all duration-200 font-dm',
                isLiked
                  ? 'bg-[#FDF0F0] border-[#E8A0A0] text-[#C0392B]'
                  : 'border-[#E0D9CE] text-[#6B6B5A] hover:border-[#1C1C1E] hover:text-[#1C1C1E]'
              ]">
                <v-icon size="16" :icon="isLiked ? 'mdi-heart' : 'mdi-heart-outline'" />
                {{ likeCount }}
              </button>

              <button @click="showComments = !showComments"
                class="flex items-center gap-2 px-4 py-2 rounded-full text-sm border border-[#E0D9CE] text-[#6B6B5A] hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-all font-dm">
                <v-icon size="16" icon="mdi-comment-outline" />
                {{ poem_detail.comment_count }}
              </button>

              <div class="flex-1"></div>

              <button
                class="flex items-center gap-1.5 px-4 py-2 rounded-full text-sm border border-[#E0D9CE] text-[#6B6B5A] hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-all font-dm">
                <v-icon size="16" icon="mdi-share-variant-outline" />
                Paylaş
              </button>
            </div>

            <!-- Comments Section -->
            <div v-if="showComments">
              <h3 class="text-lg text-[#1C1C1E] mb-6 font-garamond">
                Teswirler <span class="text-[#A0988A] text-sm font-dm">({{ poem_comments_count }})</span>
              </h3>

              <!-- Comment Input -->
              <div class="flex gap-3 mb-8">
                <img :src="poem_detail.author?.avatar || '/poet_images/default.webp'" class="w-9 h-9 rounded-full shrink-0 ring-1 ring-[#E0D9CE]" />
                <div class="flex-1">
                  <textarea v-model="newComment" rows="2" placeholder="Düşünjelerini paylaş..."
                    class="w-full px-4 py-3 bg-[#F0EBE1] rounded-[12px] text-[#2A2418] placeholder-[#B0A898] resize-none outline-none focus:ring-1 focus:ring-[#A8896C] text-sm transition-all font-garamond text-[15px]"></textarea>
                  <div class="flex justify-end mt-2">
                    <button :disabled="!newComment.trim()" @click="submitComment" :class="[
                      'px-5 py-1.5 rounded-full text-xs transition-all duration-200 font-dm',
                      newComment.trim()
                        ? 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E]'
                        : 'bg-[#E0D9CE] text-[#B0A898] cursor-not-allowed'
                    ]">
                      {{ poemStore.loading ? 'Ýüklenýär...' : 'Ugrat' }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- Comment List -->
              <div class="space-y-6">
                <div v-for="comment in poem_comments" :key="comment.id" class="flex gap-3">
                  <img :src="comment.author?.avatar || '/poet_images/default.webp'" class="w-8 h-8 rounded-full shrink-0 ring-1 ring-[#E0D9CE]" />
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2 mb-1">
                      <span class="text-sm font-medium text-[#1C1C1E] font-dm">{{
                        comment.author?.username }}</span>
                      <span class="text-xs text-[#B0A898] font-dm">{{ formatDateTk(comment.created_at)
                        }}</span>
                    </div>
                    <p class="text-[#4A4438] leading-relaxed font-garamond text-[16px]">
                      {{ comment.content }}
                    </p>
                    <div class="flex items-center gap-3 mt-2">
                      <button
                        class="flex items-center gap-1 text-xs text-[#A0988A] hover:text-[#C0392B] transition-colors font-dm">
                        <v-icon size="12" icon="mdi-heart-outline" />
                        {{ comment.like_count }}
                      </button>
                      <button class="text-xs text-[#A0988A] hover:text-[#1C11C1E] transition-colors font-dm">
                        Jogap ber
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
          <!-- Right Sidebar -->
          <aside class="lg:w-64 shrink-0">
            <div class="lg:sticky lg:top-20 space-y-8">
              <h3 class="text-xs font-semibold text-[#1C1C1E] mb-4 tracking-widest uppercase font-dm">Meňzeş Goşgular
              </h3>
              <div class="space-y-4">
                <router-link v-for="p in similar_poems" :key="p.id" :to="{ name: 'PoemDetail', params: { id: p.id } }"
                  class="flex items-start gap-2.5 group">
                  <img :src="p.author?.avatar || '/poet_images/default.webp'" class="w-6 h-6 rounded-full shrink-0 mt-0.5" />
                  <div class="flex-1 min-w-0">
                    <p
                      class="text-sm text-[#2A2418] group-hover:text-[#A8896C] transition-colors leading-snug font-garamond text-[15px]">
                      {{ p.title }}
                    </p>
                    <p class="text-xs text-[#B0A898] font-dm">{{ p.author.username }}</p>
                  </div>
                </router-link>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { formatDateTk } from '@/composables/useFormat'

const route = useRoute();
const poemStore = usePoemStore();
const commentStore = useCommentStore();
const { poem_detail, poem_comments, poem_comments_count } = storeToRefs(poemStore)

const similar_poems = ref([])

const errorMsg = ref('')
const isLiked = ref(false)
const likeCount = ref(248)
const isFollowing = ref(false)
const showComments = ref(true)
const newComment = ref('')

// Music state — starts muted
const isMuted = ref(true)
const audioRef = ref(null)

const toggleMusic = () => {
  if (!audioRef.value) return
  if (isMuted.value) {
    audioRef.value.play()
    isMuted.value = false
  } else {
    audioRef.value.pause()
    audioRef.value.currentTime = 0
    isMuted.value = true
  }
}

const toggleLike = () => {
  isLiked.value = !isLiked.value
  likeCount.value += isLiked.value ? 1 : -1
}

const submitComment = async () => {
  if (!newComment.value.trim()) return
  try {
    const response = await poemStore.createPoemComment(route.params.id, { content: newComment.value.trim() })
    if (response !== true) {
      errorMsg.value = 'Ýalňyşlyk ýüze çykdy';
      return;
    }
    newComment.value = ''
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

watch(
  () => route.params.id,
  async (newId, _) => {
    await poemStore.fetchPoemDetail(newId)
    await poemStore.fetchPoemComments(newId)
    const results = await poemStore.fetchPoems({ category: poemStore.poem_detail.category?.slug })
    similar_poems.value = results
  }, { immediate: true }
);
</script>

<style scoped>
@keyframes music-rotate {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.music-spin {
  animation: music-rotate 3s linear infinite;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content {
  white-space: normal;
  /* pre değil, normal akış */
  line-height: 1.6;
  font-family: 'Garamond', serif;
  color: #2a2418;
  font-size: 1.125rem;
  /* text-lg */
}
</style>