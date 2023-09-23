import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {Tabs, Tab} from 'vue3-tabs-component';

const app = createApp(App).component('tabs', Tabs).component('tab', Tab);

app.use(router);
app.mount("#app");
