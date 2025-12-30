import { createApp } from "vue";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import VueApexCharts from "vue3-apexcharts";
import App from "./App.vue";
import './assets/global.css'

// i18n tuonti 8.12.2025
import { i18n } from "./i18n";

const app = createApp(App);
const pinia = createPinia();


pinia.use(piniaPluginPersistedstate);

app.use(VueApexCharts);
app.use(pinia);
app.use(i18n);
app.mount("#app");
