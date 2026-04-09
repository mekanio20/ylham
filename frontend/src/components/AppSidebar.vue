<template>
  <aside class="w-64 shrink-0 border-r border-gray-200 bg-white min-h-[calc(100vh-4rem)] py-6">
    <div class="px-4 space-y-1">
      <router-link
        to="/blogs"
        class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
        :class="route.path === '/blogs' ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700'"
      >
        Dashboard
      </router-link>
      <router-link
        to="/blogs"
        class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
        :class="route.path === '/blogs' ? 'bg-gray-100 text-gray-900 font-medium border-r-2 border-gray-900' : 'text-gray-700'"
      >
        <v-icon size="18" icon="mdi-file-document-outline" />
        Blogs
      </router-link>
      <router-link
        to="/dashboard/notifications"
        class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
        :class="route.path === '/dashboard/notifications' ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700'"
      >
        <v-icon size="18" icon="mdi-bell-outline" />
        Notifications
      </router-link>
      <router-link
        to="/poem/create"
        class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
        :class="route.path.startsWith('/poem/create') ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700'"
      >
        <v-icon size="18" icon="mdi-pencil" />
        Write
      </router-link>
      <div class="pt-4">
        <p class="px-3 py-1 text-xs font-semibold text-gray-500 uppercase tracking-wider">
          Settings
        </p>
        <router-link
          to="/settings"
          class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
          :class="route.path === '/settings' ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700'"
        >
          <v-icon size="18" icon="mdi-account-edit-outline" />
          Edit Profile
        </router-link>
        <router-link
          to="/settings/password"
          class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm hover:bg-gray-50"
          :class="route.path === '/settings/password' ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700'"
        >
          <v-icon size="18" icon="mdi-lock-outline" />
          Change Password
        </router-link>
      </div>
    </div>
  </aside>
</template>

<script setup>
const route = useRoute()
</script>
