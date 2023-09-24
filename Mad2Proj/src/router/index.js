import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ModelView from "../views/ModelView.vue";
import LoginView from "../views/LoginView.vue";
import LogoutView from "../views/LogoutView.vue";
import VenueView from "../views/VenueView.vue";
import ShowView from "../views/ShowView.vue";
import VenueEditView from "../views/VenueEditView.vue";
import ShowEditView from "../views/ShowEditView.vue";
import VenueNewView from "../views/VenueNewView.vue";
import ShowNewView from "../views/ShowNewView.vue";
import TicketView from "../views/TicketView.vue";
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
    {
        path: "/venue/:query",
        name: "venue",
        component: VenueView,
        props: true,
    },
    {
        path: "/show/:query",
        name: "show",
        component: ShowView,
        props: true,
    },
    {
        path: "/venue/edit/:query",
        name: "venueEdit",
        component: VenueEditView,
        props: true,
    },
    {
        path: "/show/edit/:query",
        name: "showEdit",
        component: ShowEditView,
        props: true,
    },
    {
        path: "/venue/new",
        name: "venueNew",
        component: VenueNewView,
    },
    {
        path: "/show/new",
        name: "showNew",
        component: ShowNewView,
    },
    {
        path: "/ticket/:query",
        name: "ticket",
        component: TicketView,
        props: true,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
