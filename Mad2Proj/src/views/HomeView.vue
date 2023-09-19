<template>
    <div class="home">
        <h1>Home</h1>
    </div>
</template>

<style scoped>
</style>

<script>
import { ref, onMounted } from "vue";
    import { useRouter } from "vue-router";
    export default {
        data() {
            return {
            };
        },
        setup() {
            const isLogin = ref("");
            isLogin.value = "false";
            const accessToken = ref("");
            const sessionStorage = window.sessionStorage;
            if (sessionStorage.getItem("justReload") === "true") {
                sessionStorage.setItem("justReload", "false");
                window.location.reload();
            }
        }
    };
</script>
