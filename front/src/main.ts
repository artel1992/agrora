import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import './assets/tw.pcss';
import {createPinia} from 'pinia';
import {registerComponents} from "@/core/cms";
import HomePage from '@/pages/HomePage.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import SliderComponent from '@/components/editable-components/slider/index.vue';
import TopProducts from '@/components/editable-components/top-products/index.vue';
import ContentComponent from '@/components/editable-components/content/index.vue';
import RichText from '@/components/RichText.vue';
import 'boxicons/css/boxicons.min.css';
import vfmPlugin from 'vue-final-modal';
// import {quillEditor} from 'vue3-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

import {QuillEditor} from '@vueup/vue-quill'

const app = createApp(App)
registerComponents(app, [DefaultLayout, HomePage, SliderComponent, QuillEditor,
    TopProducts, ContentComponent, RichText])

app.use(vfmPlugin).use(router).use(createPinia()).mount('#app');
