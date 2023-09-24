<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <router-link to="/" class="navbar-brand">Home</router-link>
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup"
                aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <router-link to="/model" class="nav-link active"
                        >Profile</router-link
                    >
                </div>
            </div>
            <div v-if="isLogin === 'false'">
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <router-link to="/login" class="nav-link active"
                            >Auth</router-link
                        >
                    </div>
                </div>
            </div>
            <div v-else>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <router-link to="/logout" class="nav-link active"
                            >Logout</router-link
                        >
                    </div>
                </div>
            </div>
        </div>
    </nav>
    <router-view />
    <footer>
        <div class="container-fluid">
            <div class="row">
                <div class="col-12 text-center">
                    <p>
                        <small>&copy; 2023 Ooga Booga Inc.</small>
                    </p>
                </div>
            </div>
        </div>
    </footer>
</template>

<style>
    /* light grey background to the entire template*/
    #app {
        background-color: #ffffff;
    }
</style>

<script>
    import "@/assets/style.css";
    import { ref, onMounted } from "vue";
    export default {
        data() {
            return {
                isLogin: "false",
            };
        },
        setup() {
            const isLogin = ref("false");
            const sessionStorage = window.sessionStorage;
            onMounted(async () => {
                console.log("Main app mounted");
                isLogin.value = sessionStorage.getItem("isLogin");
            });
            isLogin.value = sessionStorage.getItem("isLogin");
            return { isLogin };
        },
        components: {},
        methods: {},
    };
</script>
