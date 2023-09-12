import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ModelView from "../views/ModelView.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/model",
        name: "model",
        component: ModelView,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
