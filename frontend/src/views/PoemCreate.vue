<template>
  <main class="min-h-screen bg-[#FAFAF7] font-garamond pb-24">

    <!-- Minimal Top Header (back only) -->
    <div class="border-b border-[#EAE5DC] bg-[#FAFAF7] sticky top-0 z-20">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between py-3.5">
        <button @click="handlePrev"
          class="flex items-center gap-1.5 text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors font-dm text-sm">
          <v-icon size="14" icon="mdi-arrow-left" />
          Yza
        </button>

        <!-- Step dots -->
        <div class="flex items-center gap-1.5">
          <div v-for="s in 4" :key="s" :class="['h-1 rounded-full transition-all duration-500',
            s === step ? 'w-8 bg-[#A8896C]' : s < step ? 'w-4 bg-[#C8B99A]' : 'w-4 bg-[#DDD8CE]']" />
        </div>

        <!-- Step label -->
        <span class="text-xs text-[#9A9A8A] font-dm">{{ step }} / 4</span>
      </div>
    </div>

    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-10">

      <div class="fixed top-14 z-50">
        <ErrorMessage :errorMsg="errorMsg" />
      </div>

      <!-- ───── STEP 1: Ýaz ───── -->
      <div v-if="step === 1">
        <div class="max-w-2xl mx-auto">

          <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-6 text-center font-dm">Ädim 1 · Goşgyny Ýaz</p>

          <!-- Title Input -->
          <div class="mb-2">
            <input v-model="form.title" type="text" placeholder="Goşgynyň ady..." maxlength="100"
              class="w-full bg-transparent text-[#1C1C1E] placeholder-[#C8C0B0] outline-none text-3xl md:text-4xl leading-tight font-garamond" />
          </div>

          <div class="flex justify-between items-center mb-4 pb-4 border-b border-[#EAE5DC]">
            <p class="text-xs text-[#C8C0B0] font-dm">
              {{ form.title.length }} / 100
            </p>
          </div>

          <!-- Poem Textarea -->
          <div class="relative">
            <div
              class="absolute -left-8 top-0 text-6xl text-[#EEE8DC] select-none leading-none pointer-events-none font-garamond">
              "</div>
            <textarea v-model="form.body" :placeholder="placeholderText" rows="9"
              class="w-full bg-transparent text-[#2A2418] placeholder-[#C8C0B0] sm:text-[20px] outline-none resize-none leading-loose"></textarea>
          </div>

          <!-- Word / line count -->
          <div class="flex items-center gap-4 mt-4 pt-4 border-t border-[#EAE5DC]">
            <span class="text-xs text-[#B0A898] font-dm">{{ lineCount }} setir</span>
            <span class="text-xs text-[#B0A898] font-dm">{{ wordCount }} söz</span>
            <span class="text-xs text-[#B0A898] font-dm">takmynan {{ readTimeFormatted }} okalýar</span>
            <div class="flex-1"></div>
          </div>

          <!-- Şygyr belligi -->
          <div class="mt-8">
            <button @click="showNote = !showNote"
              class="flex items-center gap-2 text-sm text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors mb-3 font-dm">
              <v-icon size="16" :icon="showNote ? 'mdi-minus' : 'mdi-plus'" />
              {{ showNote ? 'Goşgy belligini aýyr' : 'Goşgy belligi ýaz' }}
            </button>
            <textarea v-if="showNote" v-model="form.note" rows="3"
              placeholder="Goşgynyň döremegine sebäp bolan waka, pursat ýa-da gysgaça bellik ýazyň..."
              class="w-full px-4 py-3 bg-[#F0EBE1] rounded-xl text-[#2A2418] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C] resize-none transition-all font-garamond italic"></textarea>
          </div>

          <!-- Gosgy Suraty -->
          <div class="mt-10">
            <div class="flex items-center justify-between mb-1">
              <div>
                <p class="text-xs tracking-widest uppercase text-[#6B6B5A] font-dm">Goşgy Suraty</p>
                <p class="text-xs text-[#9A9A8A] mt-0.5 font-dm">Goşgynyň duýgusyny aňladýan suraty saýlaň</p>
              </div>
              <button v-if="form.coverImage" @click="form.coverImage = null"
                class="text-xs text-[#9A9A8A] hover:text-[#C0392B] transition-colors flex items-center gap-1 font-dm">
                <v-icon size="13" icon="mdi-close" /> Aýyr
              </button>
            </div>

            <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 scale-95"
              enter-to-class="opacity-100 scale-100">
              <div v-if="form.coverImage" class="mt-3 mb-4 relative rounded-2xl overflow-hidden group">
                <img :src="form.coverImage.url" :alt="form.coverImage.label" class="w-full h-72 object-cover" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-4">
                  <div>
                    <p class="text-white text-sm font-medium font-dm">{{ form.coverImage.label }}</p>
                    <p class="text-white/60 text-xs font-dm">{{ form.coverImage.mood }}</p>
                  </div>
                </div>
                <button @click="form.coverImage = null"
                  class="absolute top-3 right-3 w-8 h-8 bg-black/40 hover:bg-black/60 rounded-full flex items-center justify-center text-white transition-all opacity-0 group-hover:opacity-100">
                  <v-icon size="16" icon="mdi-close" />
                </button>
              </div>
            </Transition>

            <div class="mt-3 grid grid-cols-3 sm:grid-cols-5 gap-2.5">
              <button @click="form.coverImage = null"
                :class="['relative rounded-xl overflow-hidden border-2 transition-all duration-200 h-20 flex flex-col items-center justify-center gap-1.5',
                  !form.coverImage ? 'border-[#1C1C1E] bg-[#F0EBE1]' : 'border-[#E0D9CE] bg-[#F5F2EC] hover:border-[#9A9A8A]']">
                <v-icon size="20" icon="mdi-image-off-outline"
                  :class="!form.coverImage ? 'text-[#1C1C1E]' : 'text-[#9A9A8A]'" />
                <span class="text-[10px] font-dm"
                  :class="!form.coverImage ? 'text-[#1C1C1E] font-medium' : 'text-[#9A9A8A]'">Suratsyz</span>
                <v-icon v-if="!form.coverImage" size="12" icon="mdi-check-circle"
                  class="absolute top-1.5 right-1.5 text-[#A8896C]" />
              </button>

              <button v-for="img in coverImages" :key="img.id" @click="form.coverImage = img"
                :class="['relative rounded-xl overflow-hidden border-2 transition-all duration-200 h-20 group',
                  form.coverImage?.id === img.id ? 'border-[#A8896C] ring-1 ring-[#A8896C]/30' : 'border-transparent hover:border-[#A8896C]/50']">
                <img :src="img.url" :alt="img.label" class="w-full h-full object-cover" />
                <div
                  class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex flex-col justify-end p-1.5">
                  <p class="text-white leading-tight font-dm text-[9px]">{{ img.label }}</p>
                </div>
                <div v-if="form.coverImage?.id === img.id"
                  class="absolute top-1.5 right-1.5 w-4 h-4 bg-[#A8896C] rounded-full flex items-center justify-center">
                  <v-icon size="10" icon="mdi-check" class="text-white" />
                </div>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- ───── STEP 2: Goşmaçalar ───── -->
      <div v-if="step === 2">
        <div class="max-w-xl mx-auto">
          <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-8 text-center font-dm">Ädim 2 · Goşmaçalar</p>

          <div class="rounded-2xl overflow-hidden mb-8 relative">
            <div v-if="form.coverImage" class="relative h-[400px]">
              <img :src="form.coverImage.url" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#1c1c1e]"></div>
            </div>
            <div
              class="w-full p-4 flex flex-col items-center justify-center absolute left-1/2 -translate-x-1/2 -translate-y-1/2 top-1/2 z-10">
              <h2 class="text-2xl text-center text-[#F5F0E8] mb-4 font-garamond font-medium">
                {{ form.title || 'Atsyz' }}
              </h2>
              <div class="border-l-2 border-[#A8896C] pl-4">
                <p v-for="(line, i) in previewLines" :key="i"
                  class="text-[#C8BFB0] text-sm leading-loose font-garamond italic">{{ line }}</p>
              </div>
            </div>
          </div>

          <div class="mb-7">
            <label class="text-xs tracking-widest uppercase text-[#6B6B5A] mb-3 block font-dm">Kategoriýalar</label>
            <div class="flex flex-wrap gap-2">
              <button v-for="cat in categories" :key="cat" @click="form.category = cat"
                :class="['px-4 py-2 rounded-full border transition-all duration-200 text-sm font-dm',
                  form.category === cat ? 'bg-[#1C1C1E] text-[#F5F0E8] border-[#1C1C1E]' : 'bg-transparent text-[#6B6B5A] border-[#D9D0C4] hover:border-[#1C1C1E] hover:text-[#1C1C1E]']">{{
                    cat }}</button>
            </div>
          </div>

          <div class="mb-7">
            <label class="text-xs tracking-widest uppercase text-[#6B6B5A] mb-3 block font-dm">Heşdekler</label>
            <div class="flex flex-wrap gap-2 mb-3">
              <span v-for="(tag, i) in form.tags" :key="tag"
                class="inline-flex items-center gap-1 px-3 py-1 bg-[#EDE8E0] text-[#4A4030] rounded-full text-xs font-dm">
                #{{ tag }}
                <button @click="removeTag(i)" class="hover:text-[#C0392B] transition-colors"><v-icon size="12"
                    icon="mdi-close" /></button>
              </span>
            </div>
            <div class="flex gap-2">
              <input v-model="tagInput" @keydown.enter.prevent="addTag" @keydown.space.prevent="addTag" type="text"
                placeholder="Heşdek goş..."
                class="flex-1 px-4 py-2.5 bg-[#F0EBE1] rounded-xl text-sm text-[#2A2418] placeholder-[#B0A898] outline-none focus:ring-1 focus:ring-[#A8896C] transition-all font-dm" />
              <button @click="addTag"
                class="px-4 py-2 bg-[#1C1C1E] text-[#F5F0E8] rounded-xl text-xs hover:bg-[#3A3A2E] transition-all font-dm">Goş</button>
            </div>
          </div>

          <div class="mb-7">
            <label class="text-xs tracking-widest uppercase text-[#6B6B5A] mb-3 block font-dm">Kimler görmeli</label>
            <div class="flex gap-3">
              <button v-for="opt in visibilityOptions" :key="opt.id" @click="form.visibility = opt.id"
                :class="['flex-1 flex flex-col items-center gap-1.5 py-4 rounded-xl border transition-all duration-200',
                  form.visibility === opt.id ? 'border-[#1C1C1E] bg-[#F0EBE1]' : 'border-[#E0D9CE] hover:border-[#9A9A8A]']">
                <v-icon size="20" :icon="opt.icon"
                  :class="form.visibility === opt.id ? 'text-[#1C1C1E]' : 'text-[#9A9A8A]'" />
                <span class="text-xs font-medium font-dm"
                  :class="form.visibility === opt.id ? 'text-[#1C1C1E]' : 'text-[#9A9A8A]'">{{ opt.label }}</span>
              </button>
            </div>
          </div>

          <div class="mb-7">
            <div class="flex items-center justify-between mb-1">
              <label class="text-xs tracking-widest uppercase text-[#6B6B5A] font-dm">Arka Plan Müziği</label>
              <button v-if="form.music" @click="stopAndClear"
                class="text-xs text-[#9A9A8A] hover:text-[#C0392B] transition-colors flex items-center gap-1 font-dm">
                <v-icon size="12" icon="mdi-close" /> Kaldır
              </button>
            </div>
            <p class="text-xs text-[#9A9A8A] mb-4 font-dm">Okuyucular şiirini okurken bu müzik arka planda çalacak</p>

            <Transition enter-active-class="transition-all duration-300 ease-out"
              enter-from-class="opacity-0 -translate-y-3 scale-[0.98]"
              enter-to-class="opacity-100 translate-y-0 scale-100"
              leave-active-class="transition-all duration-200 ease-in" leave-from-class="opacity-100 translate-y-0"
              leave-to-class="opacity-0 -translate-y-3">
              <div v-if="form.music && currentTrack" class="mb-4 rounded-2xl overflow-hidden relative bg-[#1C1C1E]">
                <div class="absolute inset-0 opacity-20 pointer-events-none"
                  :style="`background: radial-gradient(ellipse at 20% 50%, ${currentTrack.accentColor} 0%, transparent 65%)`">
                </div>
                <div class="relative flex items-center gap-4 p-4">
                  <div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 relative overflow-hidden"
                    :style="`background: ${currentTrack.accentColor}22`">
                    <v-icon size="24" :icon="currentTrack.icon" :style="`color: ${currentTrack.accentColor}`" />
                    <div v-if="isPlaying" class="absolute inset-0 rounded-xl animate-ping-slow opacity-30"
                      :style="`background: ${currentTrack.accentColor}`"></div>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="text-sm text-[#F5F0E8] font-medium truncate mb-0.5 font-dm">{{ currentTrack.name }}</p>
                    <p class="text-xs mb-2"
                      :style="`color: ${currentTrack.accentColor}; font-family: 'DM Sans', sans-serif;`">{{
                        currentTrack.mood }} · {{ currentTrack.duration }}</p>
                    <div class="h-1.5 bg-[#3A3A3C] rounded-full overflow-hidden cursor-pointer" @click="seekProgress">
                      <div class="h-full rounded-full transition-none"
                        :style="`width: ${playProgress}%; background: ${currentTrack.accentColor}`"></div>
                    </div>
                    <div class="flex justify-between mt-1">
                      <span class="text-[#4A4A4C] font-dm text-[9px]">{{ formatTime(currentTime) }}</span>
                      <span class="text-[#4A4A4C] font-dm text-[9px]">{{ currentTrack.duration }}</span>
                    </div>
                  </div>
                  <button @click="togglePlay" :class="['w-10 h-10 rounded-full flex items-center justify-center transition-all shrink-0',
                    isPlaying ? 'hover:opacity-80' : 'bg-[#2E2E30] hover:bg-[#3A3A3C]']"
                    :style="isPlaying ? `background: ${currentTrack.accentColor}` : ''">
                    <v-icon size="20" :icon="isPlaying ? 'mdi-pause' : 'mdi-play'"
                      :class="isPlaying ? 'text-white' : 'text-[#F5F0E8]'" />
                  </button>
                </div>
              </div>
            </Transition>

            <div class="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
              <button @click="stopAndClear"
                :class="['flex flex-col items-center justify-center gap-2 py-5 px-2 rounded-xl border-2 transition-all duration-200',
                  !form.music ? 'border-[#1C1C1E] bg-[#F0EBE1]' : 'border-[#E0D9CE] hover:border-[#9A9A8A] hover:bg-[#FAFAF7]']">
                <div
                  :class="['w-10 h-10 rounded-xl flex items-center justify-center', !form.music ? 'bg-[#1C1C1E]' : 'bg-[#EDE8E0]']">
                  <v-icon size="18" icon="mdi-music-off" :class="!form.music ? 'text-[#F5F0E8]' : 'text-[#9A9A8A]'" />
                </div>
                <span class="text-center leading-tight font-dm text-[11px]"
                  :class="!form.music ? 'text-[#1C1C1E] font-semibold' : 'text-[#9A9A8A]'">Müziksiz</span>
              </button>

              <button v-for="track in musicTracks" :key="track.id" @click="selectTrack(track)"
                :class="['relative flex flex-col items-center justify-center gap-2 py-5 px-2 rounded-xl border-2 transition-all duration-200 group overflow-hidden',
                  form.music === track.id ? 'border-2' : 'border-[#E0D9CE] hover:border-opacity-60 hover:bg-[#FAFAF7]']" :style="form.music === track.id
                    ? `border-color: ${track.accentColor}; box-shadow: 0 0 0 3px ${track.accentColor}18; background: ${track.accentColor}08`
                    : ''">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center transition-all relative"
                  :style="`background: ${track.accentColor}${form.music === track.id ? '25' : '15'}`">
                  <v-icon size="18" :icon="track.icon" :style="`color: ${track.accentColor}`" />
                  <div v-if="form.music === track.id && isPlaying" class="absolute inset-0 rounded-xl animate-ping-slow"
                    :style="`background: ${track.accentColor}; opacity: 0.2`"></div>
                </div>
                <span class="text-center leading-tight font-dm text-[11px]"
                  :class="form.music === track.id ? 'font-semibold text-[#1C1C1E]' : 'text-[#6B6B5A]'">{{ track.name
                  }}</span>
                <span class="text-center font-dm text-[9px]" :style="`color: ${track.accentColor}; opacity: 0.8`">{{
                  track.mood }}</span>
                <div
                  class="absolute inset-0 rounded-xl flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"
                  v-if="form.music !== track.id">
                  <v-icon size="28" icon="mdi-play-circle-outline"
                    :style="`color: ${track.accentColor}; opacity: 0.35`" />
                </div>
              </button>
            </div>
          </div>

          <div class="flex items-center justify-between py-4 border-t border-[#EAE5DC]">
            <div>
              <p class="text-sm text-[#1C1C1E] font-dm">Teswirlere rugsat bermek</p>
              <p class="text-xs text-[#9A9A8A] font-dm">Saýlanmadyk ýagdaýynda goşga teswir ýazyp bolmaýar</p>
            </div>
            <button @click="form.allowComments = !form.allowComments"
              :class="['w-12 h-6 rounded-full transition-all duration-300 relative', form.allowComments ? 'bg-[#1C1C1E]' : 'bg-[#D9D0C4]']">
              <span
                :class="['absolute top-1 w-4 h-4 bg-white rounded-full shadow transition-all duration-300', form.allowComments ? 'left-7' : 'left-1']"></span>
            </button>
          </div>
        </div>
      </div>

      <!-- ───── STEP 3: Syn etmek ───── -->
      <div v-if="step === 3">
        <div class="max-w-2xl mx-auto">
          <p class="text-xs tracking-[0.3em] uppercase text-[#A8896C] mb-8 text-center font-dm">Ädim 3 · Syn etmek</p>

          <div class="rounded-2xl overflow-hidden mb-8 relative">
            <div v-if="form.coverImage" class="relative h-[400px]">
              <img :src="form.coverImage.url" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#1c1c1e]"></div>
            </div>
            <div
              class="w-full p-4 flex flex-col items-center justify-center absolute left-1/2 -translate-x-1/2 -translate-y-1/2 top-1/2 z-10">
              <h2 class="text-2xl text-center text-[#F5F0E8] mb-4 font-garamond font-medium">
                {{ form.title || 'Atsyz' }}
              </h2>
              <div class="border-l-2 border-[#A8896C] pl-4">
                <p v-for="(line, i) in previewLines" :key="i"
                  class="text-[#C8BFB0] text-sm leading-loose font-garamond italic">{{ line }}</p>
              </div>
            </div>
          </div>

          <span
            class="inline-flex items-center px-3 py-1 rounded-full text-xs bg-[#EDE8E0] text-[#6B5E4E] mb-6 w-fit font-dm">
            {{ form.category || 'Kategoriýalar seçilmedi' }}
          </span>

          <h1 class="text-3xl md:text-4xl text-[#1C1C1E] leading-tight mb-8 font-garamond">
            {{ form.title || 'Atsyz Goşgy' }}
          </h1>

          <div class="flex items-center gap-3 mb-10 pb-8 border-b border-[#EAE5DC]">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=me123" alt="Ben"
              class="w-10 h-10 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#FAFAF7]" />
            <div>
              <p class="text-sm font-medium text-[#1C1C1E] font-dm">Sen</p>
              <p class="text-xs text-[#9A9A8A] font-dm">Bugün · {{ readTimeFormatted }} okalýar</p>
            </div>
            <div v-if="form.music && currentTrack"
              class="ml-auto flex items-center gap-2 px-3 py-1.5 bg-[#1C1C1E] rounded-full">
              <v-icon size="12" icon="mdi-music-note" :style="`color: ${currentTrack.accentColor}`" />
              <span class="text-xs text-[#C8BFB0] font-dm text-[11px]">{{ currentTrack.name }}</span>
            </div>
          </div>

          <div class="relative pl-2">
            <div class="absolute -left-6 -top-3 text-6xl text-[#EEE8DC] select-none leading-none font-garamond">"</div>
            <div class="space-y-0">
              <p v-for="(line, i) in form.body.split('\n')" :key="i"
                class="text-[#2A2418] leading-loose font-serif sm:text-[20px]" :class="line === '' ? 'h-5' : ''">{{ line
                }}
              </p>
            </div>
            <div class="mt-8 flex items-center gap-3">
              <div class="flex-1 h-px bg-[#EAE5DC]"></div>
              <span class="text-[#C8B89A] font-garamond">❧</span>
              <div class="flex-1 h-px bg-[#EAE5DC]"></div>
            </div>
          </div>

          <div v-if="form.note" class="bg-[#F0EBE1] rounded-xl p-5 mb-8 mt-6">
            <p class="text-xs tracking-widest uppercase text-[#A8896C] mb-1.5 font-dm">Şair Notu</p>
            <p class="text-[#5A5040] leading-relaxed font-garamond italic">{{ form.note }}</p>
          </div>

          <div v-if="form.tags.length" class="flex flex-wrap gap-2 my-6">
            <span v-for="tag in form.tags" :key="tag"
              class="px-3 py-1 bg-[#EDE8E0] text-[#6B5E4E] rounded-full text-xs font-dm">#{{ tag }}</span>
          </div>
        </div>
      </div>

      <!-- ───── STEP 4: Success ───── -->
      <div v-if="step === 4">
        <div class="max-w-xl mx-auto text-center">
          <!-- Success Animation Circle -->
          <div class="mb-8 flex justify-center">
            <div class="relative w-32 h-32">
              <!-- Animated Circle -->
              <div
                class="absolute inset-0 rounded-full bg-gradient-to-br from-[#A8896C] to-[#C8B99A] opacity-10 animate-pulse">
              </div>
              <div
                class="absolute inset-4 rounded-full bg-gradient-to-br from-[#A8896C] to-[#C8B99A] opacity-20 animate-ping"
                style="animation-duration: 2s;"></div>

              <!-- Icon Container -->
              <div class="absolute inset-0 flex items-center justify-center">
                <div
                  class="w-20 h-20 rounded-full bg-gradient-to-br from-[#A8896C] to-[#C8B99A] flex items-center justify-center shadow-lg">
                  <v-icon size="40" icon="mdi-check" class="text-white" />
                </div>
              </div>
            </div>
          </div>

          <!-- Success Title -->
          <h2 class="text-3xl md:text-4xl text-[#1C1C1E] font-garamond font-medium mb-4">
            Goşgyňyz Ugradyldy!
          </h2>

          <!-- Success Message -->
          <p class="text-[#6B6B5A] text-base leading-relaxed mb-8 max-w-md mx-auto font-dm">
            Goşgyňyz üstünlikli ugradyldy we admin tarapyndan barlag edilýär. Tassyklanansoň, goşgyňyz görkeziler.
          </p>

          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-3">
            <button @click="router.push('/profile')"
              class="flex-1 flex items-center justify-center gap-2 px-6 py-3 rounded-full border-2 border-[#1C1C1E] text-[#1C1C1E] hover:bg-[#1C1C1E] hover:text-white transition-all duration-200 font-dm">
              <v-icon size="18" icon="mdi-account-outline" />
              Profiliňa git
            </button>
            <button @click="createNewPoem"
              class="flex-1 flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#A8896C] text-white hover:bg-[#C8A87C] transition-all duration-200 shadow-sm font-dm font-semibold">
              <v-icon size="18" icon="mdi-plus" />
              Täze goşgy ýaz
            </button>
          </div>
        </div>
      </div>

    </div>

    <!-- ───── BOTTOM ACTION BAR ───── -->
    <div v-if="step < 4" class="fixed bottom-0 left-0 right-0 z-30">
      <!-- Blur backdrop -->
      <div class="absolute inset-0 bg-[#FAFAF7]/80 backdrop-blur-md border-t border-[#EAE5DC]"></div>

      <div class="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center gap-3">

        <!-- Left: word/line info on step 1 -->
        <div v-if="step === 1" class="flex-1 flex items-center gap-3 min-w-0">
          <div class="flex flex-col">
            <span class="text-xs text-[#1C1C1E] font-medium font-dm">{{ form.title || 'Atsyz Goşgy' }}</span>
            <span class="text-[11px] text-[#B0A898] font-dm">{{ wordCount }} söz · {{ lineCount }} setir</span>
          </div>
        </div>

        <!-- Left: category on step 2 -->
        <div v-else-if="step === 2" class="flex-1 min-w-0">
          <span v-if="form.category"
            class="inline-flex items-center gap-1 text-xs text-[#6B5E4E] bg-[#EDE8E0] px-3 py-1 rounded-full font-dm">
            <v-icon size="11" icon="mdi-tag-outline" />
            {{ form.category }}
          </span>
          <span v-else class="text-xs text-[#C8C0B0] font-dm">Kategoriýa saýlaň</span>
        </div>

        <!-- Left: publish info on step 3 -->
        <div v-else class="flex-1 flex items-center gap-2 min-w-0">
          <v-icon size="14" :icon="visibilityOptions.find(o => o.id === form.visibility)?.icon || 'mdi-earth'"
            class="text-[#9A9A8A] shrink-0" />
          <span class="text-xs text-[#9A9A8A] font-dm truncate">{{visibilityOptions.find(o => o.id ===
            form.visibility)?.label}}</span>
        </div>

        <!-- Right: actions -->
        <div class="flex items-center gap-2 shrink-0">
          <!-- Draft -->
          <button v-if="step > 1" @click="saveDraft" :disabled="draftSaved"
            class="flex items-center gap-1.5 sm:px-3 px-2 py-2 text-xs text-[#9A9A8A] hover:text-[#1C1C1E] transition-colors rounded-full hover:bg-[#F0EBE1] font-dm">
            <v-icon size="15" icon="mdi-content-save-outline" />
            <span class="hidden sm:inline">Garalama</span>
          </button>

          <!-- Next / Publish -->
          <button v-if="step < 3" @click="nextStep" :disabled="!canProceed" :class="[
            'flex items-center gap-2 px-6 py-2.5 rounded-full text-sm font-medium transition-all duration-200 font-dm',
            canProceed
              ? 'bg-[#1C1C1E] text-[#F5F0E8] hover:bg-[#3A3A2E] active:scale-[0.98] shadow-sm'
              : 'bg-[#E0D9CE] text-[#B0A898] cursor-not-allowed'
          ]">
            Dowam et
            <v-icon size="14" icon="mdi-arrow-right" />
          </button>

          <button v-else @click="publishPoem"
            class="flex items-center gap-2 px-6 py-2.5 rounded-full text-sm font-semibold bg-[#A8896C] text-white hover:bg-[#C8A87C] transition-all duration-200 shadow-sm active:scale-[0.98] font-dm">
            <v-icon size="14" icon="mdi-send-outline" />
            {{ poemStore.loading ? 'Ýüklenýär...' : 'Ugrat' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Toast -->
    <div v-if="draftSaved"
      class="fixed bottom-24 left-1/2 -translate-x-1/2 px-5 py-3 bg-[#1C1C1E] text-[#F5F0E8] rounded-full text-sm shadow-lg transition-all font-dm text-[12px] z-40">
      ✓ Garalama goşuldy
    </div>

  </main>
</template>

<script setup>
const router = useRouter()
const poemStore = usePoemStore()

const showNote = ref(true)
const draftSaved = ref(false)
const tagInput = ref('')
const errorMsg = ref('')
const step = ref(Number(sessionStorage.getItem('poem_create_step') || 1))

const form = ref({
  title: '',
  body: '',
  note: '',
  category: '',
  tags: [],
  visibility: 'public',
  allowComments: true,
  coverImage: null,
  music: null,
})

const coverImages = [
  { id: 'night', label: 'Gije şäherde', mood: 'Melanholik', url: '/poem_images/night.webp' },
  { id: 'forest', label: 'Tokaý ümüri', mood: 'Gizlinlik', url: '/poem_images/forest.webp' },
  { id: 'ocean', label: 'Deňiz', mood: 'Asuda', url: '/poem_images/ocean.webp' },
  { id: 'snow', label: 'Gar', mood: 'Ümsüm', url: '/poem_images/snow.webp' },
  { id: 'candle', label: 'Şem', mood: 'Mähir', url: '/poem_images/candle.webp' },
  { id: 'rain', label: 'Ýagyş', mood: 'Romantika', url: '/poem_images/rain.webp' },
  { id: 'books', label: 'Kitaplar', mood: 'Düşünjeli', url: '/poem_images/books.webp' },
  { id: 'hope', label: 'Umyt', mood: 'Umyt', url: '/poem_images/hope.webp' },
  { id: 'dark', label: 'Garaňky', mood: 'Ýalňyzlyk', url: '/poem_images/dark.webp' },
]

const isPlaying = ref(false)
const playProgress = ref(0)
const currentTime = ref(0)
let progressTimer = null

const musicTracks = [
  { id: 'rain', name: 'Yağmur', mood: 'Hüzünlü', duration: '3:24', icon: 'mdi-weather-rainy', accentColor: '#7B6FD4' },
  { id: 'piano', name: 'Piyano', mood: 'Melankolik', duration: '4:10', icon: 'mdi-piano', accentColor: '#A8896C' },
  { id: 'ocean', name: 'Deniz', mood: 'Dingin', duration: '5:02', icon: 'mdi-waves', accentColor: '#2980B9' },
  { id: 'forest', name: 'Orman', mood: 'Huzurlu', duration: '6:15', icon: 'mdi-tree-outline', accentColor: '#27AE60' },
  { id: 'strings', name: 'Yaylılar', mood: 'Duygusal', duration: '3:48', icon: 'mdi-violin', accentColor: '#C0392B' },
  { id: 'wind', name: 'Rüzgâr', mood: 'Şiirsel', duration: '4:33', icon: 'mdi-weather-windy', accentColor: '#8E44AD' },
  { id: 'cafe', name: 'Kafe', mood: 'Sıcak', duration: '7:20', icon: 'mdi-coffee-outline', accentColor: '#D35400' },
  { id: 'midnight', name: 'Gece Yarısı', mood: 'Gizemli', duration: '5:44', icon: 'mdi-weather-night', accentColor: '#5D6D7E' },
  { id: 'cello', name: 'Çello', mood: 'Derin', duration: '4:57', icon: 'mdi-music-clef-bass', accentColor: '#6D4C41' },
]

const currentTrack = computed(() => musicTracks.find(t => t.id === form.value.music) || null)

const selectTrack = (track) => {
  form.value.music = track.id
  playProgress.value = 0
  currentTime.value = 0
  isPlaying.value = true
  startProgress()
}

const stopAndClear = () => {
  form.value.music = null
  isPlaying.value = false
  playProgress.value = 0
  currentTime.value = 0
  clearInterval(progressTimer)
}

const togglePlay = () => {
  isPlaying.value = !isPlaying.value
  isPlaying.value ? startProgress() : clearInterval(progressTimer)
}

const startProgress = () => {
  clearInterval(progressTimer)
  progressTimer = setInterval(() => {
    if (playProgress.value >= 100) {
      playProgress.value = 0
      currentTime.value = 0
    } else {
      playProgress.value += 0.12
      currentTime.value += 0.072
    }
  }, 72)
}

const seekProgress = (e) => {
  const rect = e.currentTarget.getBoundingClientRect()
  const pct = Math.min(100, Math.max(0, ((e.clientX - rect.left) / rect.width) * 100))
  playProgress.value = pct
  currentTime.value = (pct / 100) * 240
}

const formatTime = (secs) => {
  const m = Math.floor(secs / 60)
  const s = Math.floor(secs % 60)
  return `${m}:${s.toString().padStart(2, '0')}`
}

onUnmounted(() => clearInterval(progressTimer))

const placeholderText = `Şygyr sözlerini şu ýere ýaz...
Boş setir taşlap goşgyny bentlere aýyryp bilýäň.`

const lineCount = computed(() => form.value.body.split('\n').filter(l => l.trim()).length)
const wordCount = computed(() => form.value.body.trim() ? form.value.body.trim().split(/\s+/).length : 0)
const readTimeFormatted = computed(() => {
  const wordsPerSecond = 20 / 10;
  const totalSeconds = Math.max(1, Math.ceil(wordCount.value / wordsPerSecond));

  if (totalSeconds < 60) {
    return `${totalSeconds} sekuntda`;
  }

  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;

  return `${minutes} minut ${seconds} sekuntda`;
});
const previewLines = computed(() => form.value.body.split('\n').filter(l => l.trim()).slice(0, 4))

const canProceed = computed(() => {
  if (step.value === 1) return form.value.title.trim().length > 0 && form.value.body.trim().length > 0
  if (step.value === 2) return form.value.category !== ''
  return true
})

const categories = ['Söýgi', 'Tebigat', 'Içki Dünýä', 'Şäher', 'Ölüm', 'Azatlyk', 'Çagalyk', 'Melankoli', 'Umyt', 'Uruş', 'Hasrat']
const visibilityOptions = [
  { id: 'public', label: 'Hemme kişi', icon: 'mdi-earth' },
  { id: 'followers', label: 'Yzarlaýanlar', icon: 'mdi-account-group-outline' },
  { id: 'private', label: 'Gizlin', icon: 'mdi-lock-outline' },
]

const nextStep = () => {
  if (canProceed.value && step.value < 3) {
    step.value++;
    sessionStorage.setItem('poem_create_step', step.value)
    sessionStorage.setItem('temp_form', JSON.stringify(form.value))
  }
}
const addTag = () => {
  const tag = tagInput.value.trim().replace(/^#/, '').toLowerCase()
  if (tag && !form.value.tags.includes(tag) && form.value.tags.length < 5) form.value.tags.push(tag)
  tagInput.value = ''
}
const removeTag = (i) => form.value.tags.splice(i, 1)
const saveDraft = async () => {
  try {
    const poemData = {
      title: form.value.title,
      content: form.value.body,
      category_id: Number(form.value.category) || null,
      tags: form.value.tags,
      background_image: form.value.coverImage?.id || 'none',
      background_music: form.value.music || 'none',
      public_status: form.value.visibility,
      poem_note: form.value.note,
      comment_permission: form.value.allowComments,
      is_draft: true
    };
    const response = await poemStore.createPoem(poemData)
    if (response === true) {
      draftSaved.value = true
      setTimeout(() => {
        draftSaved.value = false;
        sessionStorage.clear()
        window.location.reload()
      }, 2000)
    } else {
      if (response.data?.title) {
        errorMsg.value = 'Goşgynyň ady azyndan 2 harp bolmaly'
      }
      if (response.data?.content) {
        errorMsg.value = 'Goşgy azyndan 20 harp bolmaly'
      }
      setTimeout(() => {
        errorMsg.value = ''
      }, 2000);
    }
  } catch (error) {
    console.log(error);
  }
}
const publishPoem = async () => {
  const poemData = {
    title: form.value.title,
    content: form.value.body,
    category_id: Number(form.value.category) || null,
    tags: form.value.tags,
    background_image: form.value.coverImage?.id || 'none',
    background_music: form.value.music || 'none',
    public_status: form.value.visibility,
    poem_note: form.value.note,
    comment_permission: form.value.allowComments,
    is_draft: false
  };
  try {
    const response = await poemStore.createPoem(poemData)
    if (response === true) {
      step.value = 4;
      sessionStorage.clear()
    }
    return response
  } catch (error) {
    console.log('Poem error', error);
  }
}

const createNewPoem = () => {
  // Clear form and session
  sessionStorage.clear()
  form.value = {
    title: '',
    body: '',
    note: '',
    category: '',
    tags: [],
    visibility: 'public',
    allowComments: true,
    coverImage: null,
    music: null,
  }
  step.value = 1
  sessionStorage.setItem('poem_create_step', 1)
}

const handlePrev = () => {
  if (step.value === 4) {
    router.push('/')
  } else if (step.value > 1) {
    step.value--
    sessionStorage.setItem('poem_create_step', step.value)
  } else {
    router.go(-1)
  }
}

onMounted(() => {
  const temp_form = JSON.parse(sessionStorage.getItem('temp_form'))
  if (temp_form) form.value = temp_form
})
</script>

<style scoped>
@keyframes ping-slow {
  0% {
    transform: scale(1);
    opacity: 0.4;
  }

  70% {
    transform: scale(1.6);
    opacity: 0;
  }

  100% {
    transform: scale(1.6);
    opacity: 0;
  }
}

.animate-ping-slow {
  animation: ping-slow 1.8s ease-out infinite;
}
</style>