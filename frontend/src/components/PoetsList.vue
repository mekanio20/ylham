<template>
  <!-- Şahyrlar -->
  <div>
    <h3 class="text-xs font-semibold text-[#1C1C1E] mb-4 tracking-widest uppercase flex items-center gap-1.5 font-dm">
      <v-icon size="13" icon="mdi-star-four-points" class="text-[#A8896C]" />
      Şahyrlar
    </h3>
    
    <!-- Poets Grid -->
    <div class="space-y-3">
      <!-- Visible Poets (first 10) -->
      <div class="grid lg:grid-cols-5 md:grid-cols-12 sm:grid-cols-10 grid-cols-5 gap-3">
        <div 
          v-for="poet in visiblePoets" 
          :key="poet.id"
          class="flex flex-col items-center gap-2 group cursor-pointer"
        >
          <div class="relative">
            <img 
              :src="poet.avatar" 
              :alt="poet.name" 
              class="w-12 h-12 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#FAFAF7] object-cover transition-transform group-hover:scale-105" 
            />
            <!-- Online indicator (optional) -->
            <div 
              v-if="poet.isOnline" 
              class="absolute bottom-0 right-0 w-2 h-2 bg-green-500 rounded-full ring-2 ring-[#FAFAF7]"
            ></div>
          </div>
          <span class="text-[10px] text-[#6B6B5A] text-center font-dm truncate w-full">
            {{ poet.name }}
          </span>
        </div>
      </div>

      <!-- Expandable Poets (remaining poets) -->
      <Transition
        enter-active-class="transition-all duration-300 ease-out"
        enter-from-class="opacity-0 max-h-0"
        enter-to-class="opacity-100 max-h-96"
        leave-active-class="transition-all duration-200 ease-in"
        leave-from-class="opacity-100 max-h-96"
        leave-to-class="opacity-0 max-h-0"
      >
        <div v-if="showAllPoets && remainingPoets.length > 0" class="overflow-hidden pt-1">
          <div class="grid lg:grid-cols-5 md:grid-cols-12 sm:grid-cols-10 grid-cols-5 gap-3">
            <div 
              v-for="poet in remainingPoets" 
              :key="poet.id"
              class="flex flex-col items-center gap-2 group cursor-pointer"
            >
              <div class="relative">
                <img 
                  :src="poet.avatar" 
                  :alt="poet.name" 
                  class="w-11 h-11 rounded-full ring-1 ring-[#A8896C] ring-offset-2 ring-offset-[#FAFAF7] object-cover transition-transform group-hover:scale-105" 
                />
                <div 
                  v-if="poet.isOnline" 
                  class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full ring-2 ring-[#FAFAF7]"
                ></div>
              </div>
              <span class="text-[10px] text-[#6B6B5A] text-center font-dm truncate w-full">
                {{ poet.name }}
              </span>
            </div>
          </div>
        </div>
      </Transition>

      <!-- Show More/Less Button -->
      <button 
        v-if="poets.length > 10"
        @click="showAllPoets = !showAllPoets"
        class="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl bg-[#F0EBE1] hover:bg-[#E0D9CE] transition-colors text-xs font-medium text-[#6B6B5A] font-dm"
      >
        <v-icon 
          size="14" 
          :icon="showAllPoets ? 'mdi-chevron-up' : 'mdi-chevron-down'" 
          class="transition-transform"
        />
        {{ showAllPoets ? 'Gizle' : `+${remainingPoets.length} şahyry görkez` }}
      </button>
    </div>
  </div>
</template>

<script setup>
// Props
const props = defineProps({
  poets: {
    type: Array,
    required: true,
    default: () => []
  }
})

// State
const showAllPoets = ref(false)

// Computed
const visiblePoets = computed(() => {
  return props.poets.slice(0, 10)
})

const remainingPoets = computed(() => {
  return props.poets.slice(10)
})
</script>