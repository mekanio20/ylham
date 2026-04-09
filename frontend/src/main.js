import { createApp } from 'vue'
import { createPinia } from "pinia";
import router from "./router";
import App from './App.vue'
import './assets/main.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

// Icons
import '@mdi/font/css/materialdesignicons.css'
const vuetify = createVuetify()

const app = createApp(App)
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.use(vuetify)

app.mount('#app')