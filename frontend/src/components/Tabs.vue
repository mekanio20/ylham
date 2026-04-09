<template>
  <div class="w-full h-full flex flex-col">
    <!-- Tab Navigation -->
    <div class="flex items-center space-x-3 border-b-[1px] border-gray_tertiary flex-shrink-0">
      <button type="button" v-for="tab in tabs" :key="tab.id" @click="handleTabClick(tab.id)" :class="[
        'px-2 py-3 text-[13px] font-medium transition-colors duration-200 relative flex items-center',
        activeTab === tab.id
          ? 'text-black_primary border-b-[1px] border-black_primary'
          : 'text-black_secondary'
      ]">
        <component v-if="tab.icon" :is="icons[tab?.icon]" :color="activeTab === tab.id ? '#000' : '#666666'"
          class="mr-1" />
        {{ tab.label }}
      </button>
    </div>

    <!-- Tab Content -->
    <div class="w-full flex-1 flex flex-col overflow-hidden">
      <slot :active-tab="activeTab" />
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  tabs: {
    type: Array,
    required: true,
    default: () => []
  },
  defaultTab: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['tab-click'])

const activeTab = ref(props.defaultTab || (props.tabs[0] && props.tabs[0].id))

const handleTabClick = (tabId) => {
  emit('tab-click', tabId)
  activeTab.value = tabId
}

watch(
  () => props.tabs,
  (newTabs) => {
    if (newTabs.length && !newTabs.find((t) => t.id === activeTab.value)) {
      activeTab.value = newTabs[0].id
    }
  }
)
</script>