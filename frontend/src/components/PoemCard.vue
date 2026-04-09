<template>
    <div>
        <article class="flex flex-col md:flex-row gap-5 group">
            <!-- Image (top on mobile, left on desktop) -->
            <router-link v-if="poem.background_image" :to="{ name: 'PoemDetail', params: { id: poem.id } }"
                class="shrink-0 w-full h-[400px] md:w-52 md:h-52 flex items-center justify-center rounded-xl text-[#C8B89A] md:self-start relative">
                <img :src="`/poem_images/${poem.background_image}.webp`" class="w-full h-full rounded-lg">
                <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#1c1c1e] rounded-lg"></div>
                <div
                    class="w-full md:p-1 p-4 flex flex-col md:items-start items-center justify-center absolute left-1/2 -translate-x-1/2 -translate-y-1/2 top-1/2 z-10">
                    <h2 class="md:text-xs text-2xl self-center text-center text-[#F5F0E8] mb-4 font-garamond font-medium">
                        {{ poem.title }}
                    </h2>
                    <div class="md:border-none border-l-2 border-[#A8896C] pl-4">
                        <p v-for="(line, i) in previewLines" :key="i"
                            class="text-[#C8BFB0] md:text-xs leading-loose font-garamond italic">{{ line }}</p>
                    </div>
                </div>
                <!-- <div class="text-xs md:hidden block absolute bottom-3 right-4">
                    Awtory: {{ poem.author.username }}
                </div> -->
            </router-link>
    
            <!-- Content -->
            <div class="flex-1 min-w-0">
                <!-- Author -->
                <div class="flex items-center gap-2 mb-3">
                    <img :src="poem.author.avatar || '/poet_images/default.webp'" class="w-7 h-7 rounded-full object-cover ring-1 ring-[#E0D9CE]" />
                    <span class="text-sm font-medium text-[#3A3A2E] font-dm">{{
                        poem.author.username }}</span>
                    <span class="text-[#B0A898] text-xs font-dm">·</span>
                    <span class="text-[#B0A898] text-xs font-dm">{{ formatDateTk(poem.created_at) }}</span>
                </div>
    
                <!-- Header -->
                <router-link :to="{ name: 'PoemDetail', params: { id: poem.id } }" class="block">
                    <h2
                        class="text-xl md:text-2xl text-[#1C1C1E] mb-2 leading-snug group-hover:text-[#A8896C] transition-colors duration-200 font-garamond">
                        {{ poem.title }}
                    </h2>
                    <div class="mb-3 pl-3 border-l border-[#D9C9B0]">
                        <p v-for="(line, i) in previewLines" :key="i"
                            class="text-[#C8BFB0] md:text-sm leading-loose font-garamond italic">{{ line }}</p>
                    </div>
                </router-link>
    
                <!-- Footer links -->
                <router-link :to="{ name: 'PoemDetail', params: { id: poem.id } }" class="flex items-center gap-3 flex-wrap mt-3">
                    <span
                        class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs bg-[#EDE8E0] text-[#6B5E4E] font-dm">
                        {{ poem.category.name }}
                    </span>
                    <button
                        class="flex items-center gap-1 text-xs text-[#A0988A] hover:text-[#C0392B] transition-colors font-dm">
                        <v-icon size="14" icon="mdi-heart-outline" />
                        {{ poem.like_count }}
                    </button>
                    <button
                        class="flex items-center gap-1 text-xs text-[#A0988A] hover:text-[#1C1C1E] transition-colors font-dm">
                        <v-icon size="14" icon="mdi-comment-outline" />
                        {{ poem.comment_count }}
                    </button>
                </router-link>
            </div>
        </article>
    </div>
</template>

<script setup>
import { formatDateTk } from '@/composables/useFormat'
const previewLines = computed(() => props.poem.content_preview.split('\n').filter(l => l.trim()).slice(0, 4))
const props = defineProps({
    poem: {
        type: Object,
        required: true,
    },
})
</script>