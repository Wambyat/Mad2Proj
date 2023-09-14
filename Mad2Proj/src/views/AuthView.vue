<template>
    <div class="auth">
        <h1>Auth page</h1>
        <div v-if="isAuth === 'false'">
            <p>Waiting for flask auth</p>
        </div>
        <div v-else>
            <p>Access token: {{ accessToken }}</p>
        </div>
    </div>
</template>

<style scoped></style>

<script>
    import { ref, onMounted } from "vue";
    import axios from "axios";
    export default {
        data() {
            return {
                isAuth: "false",
                accessToken: "",
            };
        },
        setup() {
            const isAuth = ref("false");
            const accessToken = ref("");
            onMounted(async () => {
                console.log("Test");
                axios.get("http://localhost:5000/auth").then((response) => {
                    console.log(response.data);
                    isAuth.value = "true";
                    accessToken.value = response.data["access_token"];
                });
            });
            return { isAuth, accessToken };
        },
        components: {},
        methods: {},
    };
</script>
