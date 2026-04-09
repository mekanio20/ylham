<template>
    <router-link :to="category.route || '#'" class="block no-underline">
        <v-card
            class="overflow-hidden transition-all duration-300 hover:shadow-xl hover:-translate-y-1 group h-full min-h-[140px]"
            elevation="0"
            rounded="xl"
            :class="cardClasses"
        >
            <div class="relative h-full pa-6 flex flex-col justify-between">
                <!-- Decorative large icon (background) -->
                <div
                    class="absolute right-4 top-4 opacity-10 group-hover:opacity-20 transition-opacity"
                    :class="iconBgClasses"
                >
                    <v-icon :icon="category.icon || 'mdi-book-open-page-variant'" size="80" />
                </div>
                <!-- Accent bar -->
                <div class="absolute left-0 top-0 bottom-0 w-1 rounded-l-xl" :class="accentClasses" />
                <div class="relative z-10">
                    <v-icon
                        :icon="category.icon || 'mdi-book-open-page-variant'"
                        size="32"
                        class="mb-3 opacity-90"
                        :class="iconClasses"
                    />
                    <h3 class="text-lg md:text-xl font-semibold text-[#2d2d2d] dark:text-[#f5f5dc] mb-1">
                        {{ category.name }}
                    </h3>
                    <p class="text-sm text-gray-600 dark:text-gray-400">
                        {{ category.count }} goşgy
                    </p>
                </div>
                <div class="relative z-10 mt-4 flex items-center text-sm font-medium opacity-0 group-hover:opacity-100 transition-opacity" :class="linkClasses">
                    <span>Kəşf et</span>
                    <v-icon icon="mdi-arrow-right" size="18" class="ml-1" />
                </div>
            </div>
        </v-card>
    </router-link>
</template>
<script setup>
const props = defineProps({
    category: {
        type: Object,
        required: true,
    },
})

const colorMap = {
    error: {
        card: 'bg-red-50 dark:bg-red-950/30 border border-red-100 dark:border-red-900/50',
        accent: 'bg-red-500',
        icon: 'text-red-600 dark:text-red-400',
        iconBg: 'text-red-500',
        link: 'text-red-600 dark:text-red-400',
    },
    pink: {
        card: 'bg-pink-50 dark:bg-pink-950/30 border border-pink-100 dark:border-pink-900/50',
        accent: 'bg-pink-500',
        icon: 'text-pink-600 dark:text-pink-400',
        iconBg: 'text-pink-500',
        link: 'text-pink-600 dark:text-pink-400',
    },
    success: {
        card: 'bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-100 dark:border-emerald-900/50',
        accent: 'bg-emerald-500',
        icon: 'text-emerald-600 dark:text-emerald-400',
        iconBg: 'text-emerald-500',
        link: 'text-emerald-600 dark:text-emerald-400',
    },
    amber: {
        card: 'bg-amber-50 dark:bg-amber-950/30 border border-amber-100 dark:border-amber-900/50',
        accent: 'bg-amber-500',
        icon: 'text-amber-600 dark:text-amber-400',
        iconBg: 'text-amber-500',
        link: 'text-amber-600 dark:text-amber-400',
    },
    blue: {
        card: 'bg-blue-50 dark:bg-blue-950/30 border border-blue-100 dark:border-blue-900/50',
        accent: 'bg-blue-500',
        icon: 'text-blue-600 dark:text-blue-400',
        iconBg: 'text-blue-500',
        link: 'text-blue-600 dark:text-blue-400',
    },
    purple: {
        card: 'bg-purple-50 dark:bg-purple-950/30 border border-purple-100 dark:border-purple-900/50',
        accent: 'bg-purple-500',
        icon: 'text-purple-600 dark:text-purple-400',
        iconBg: 'text-purple-500',
        link: 'text-purple-600 dark:text-purple-400',
    },
}

const theme = computed(() => colorMap[props.category.color] || colorMap.blue)

const cardClasses = computed(() => theme.value.card)
const accentClasses = computed(() => theme.value.accent)
const iconClasses = computed(() => theme.value.icon)
const iconBgClasses = computed(() => theme.value.iconBg)
const linkClasses = computed(() => theme.value.link)
</script>
