import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ModelView from "../views/ModelView.vue";
import AuthView from "../views/AuthView.vue";

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
    {
        path: "/auth",
        name: "auth",
        component: AuthView,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
