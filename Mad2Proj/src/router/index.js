import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ModelView from "../views/ModelView.vue";
import LoginView from "../views/LoginView.vue";
import LogoutView from "../views/LogoutView.vue";
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
        path: "/login",
        name: "login",
        component: LoginView,
    },
    {
        path: "/logout",
        name: "logout",
        component: LogoutView,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
