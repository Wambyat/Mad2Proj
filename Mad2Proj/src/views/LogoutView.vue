<template>
    <div class="login">
        <h1>Logout page</h1>
        <button @click="unLogin">unlogin</button>
    </div>
</template>

<style scoped></style>

<script>
    import { ref, onMounted } from "vue";
    import { useRouter } from "vue-router";
    import axios from "axios";
    export default {
        data() {
            return {
                isLogin: "",
                accessToken: "",
            };
        },
        setup() {
            const isLogin = ref("");
            const accessToken = ref("");
            const sessionStorage = window.sessionStorage;
            if(sessionStorage.getItem("justReload")==="true"){
                sessionStorage.setItem("justReload", "false");
                const router = useRouter();
                router.push("/");
            }
            return { isLogin, accessToken };
        },
        components: {},
        methods: {
            unLogin(event) {
                const sessionStorage = window.sessionStorage;
                sessionStorage.setItem("isLogin", "false");
                sessionStorage.setItem("accessToken", "");
                axios.get("http://localhost:5000/logout");
                // redirect to home page and force reload
                sessionStorage.setItem("justReload", "true");
                window.location.reload();
            },
        },
    };
</script>
