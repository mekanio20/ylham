<template>
    <div class="p-4 sm:p-6 max-w-3xl">
        <div class="bg-white rounded-2xl border border-[#EAE5DC] overflow-hidden mb-4 sm:mb-5">
            <div class="h-24 sm:h-32 bg-gradient-to-r from-[#1C1C1E] via-[#3A3020] to-[#2A2010] relative">
            </div>

            <div class="px-4 sm:px-6 pb-5">
                <div class="flex items-end gap-3 -mt-7 sm:-mt-8 mb-4">
                    
                    <div class="relative shrink-0">
                        <img :src="user.avatar"
                            class="w-14 h-14 sm:w-20 sm:h-20 rounded-full ring-4 ring-white bg-[#F0EBE1]" />

                        <button
                            class="absolute bottom-0 right-0 w-6 h-6 bg-[#1C1C1E] text-white rounded-full flex items-center justify-center hover:bg-[#3A3A2E] transition-all">
                            <v-icon size="12" icon="mdi-camera-outline" />
                        </button>
                    </div>

                    <div class="flex-1 min-w-0 mb-1 pt-8">
                        <h2 class="text-lg sm:text-2xl text-[#1C1C1E] truncate font-garamond">
                            {{ user.fullname }}
                        </h2>

                        <p class="text-xs sm:text-sm text-[#9A9A8A] font-dm">
                            @{{ user.username }}
                        </p>
                    </div>
                </div>

                <div class="space-y-3">
                    
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                {{ user.fullname }}
                            </label>

                            <input v-model="profileForm.fullname" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>

                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                {{ user.username }}
                            </label>

                            <input v-model="profileForm.username" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>
                    </div>

                    <div>
                        <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                            Biyografiýa
                        </label>

                        <textarea v-model="profileForm.bio" rows="3"
                            class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] resize-none font-garamond italic text-[15px]">
                        </textarea>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                Instagram
                            </label>

                            <input v-model="profileForm.instagram" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>

                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                Tiktok
                            </label>

                            <input v-model="profileForm.tiktok" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>

                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                Link
                            </label>

                            <input v-model="profileForm.link" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>
                        
                        <div>
                            <label class="text-xs tracking-widest uppercase text-[#9A9A8A] block mb-1.5 font-dm">
                                Imo
                            </label>

                            <input v-model="profileForm.imo" type="text"
                                class="w-full px-3 py-2 bg-[#F0EBE1] rounded-xl text-sm text-[#1C1C1E] outline-none focus:ring-1 focus:ring-[#A8896C] font-dm" />
                        </div>
                    </div>

                    <div class="flex justify-end gap-2 pt-1">
                        <button @click="saveProfile"
                            class="px-4 py-1.5 bg-[#1C1C1E] text-[#F5F0E8] rounded-full text-xs hover:bg-[#3A3A2E] transition-all font-dm">
                            Ýatda sakla
                        </button>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const profileForm = ref({
    fullname: '',
    username: '',
    bio: '',
    instagram: '',
    tiktok: '',
    link: '',
    imo: ''
})
defineProps({
    user: Object
})
</script>