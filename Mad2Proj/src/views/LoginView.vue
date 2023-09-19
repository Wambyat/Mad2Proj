<template>
    <div class="login">
        <h1>Auth page</h1>
        <div v-if="isLogin === 'false'">
            <p>Waiting for flask auth</p>
        </div>
        <div v-else>
            <p>Access token: {{ accessToken }}</p>
            <p id="redirP">Redirecting you to home in 5 seconds</p>
        </div>
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
            isLogin.value = "false";
            const accessToken = ref("");
            const sessionStorage = window.sessionStorage;
            if (sessionStorage.getItem("justReload") === "true") {
                sessionStorage.setItem("justReload", "true");
                const router = useRouter();
                router.push("/");
            }
            onMounted(async () => {
                console.log("wtf")
                axios.get("http://localhost:5000/auth").then((response) => {
                    console.log(response.data);
                    sessionStorage.setItem("isLogin", "true");
                    sessionStorage.setItem(
                        "accessToken",
                        response.data["access_token"]
                    );
                    isLogin.value = sessionStorage.getItem("isLogin");
                    accessToken.value = sessionStorage.getItem("accessToken");
                    for (let i = 0; i < 6; i++) {
                        setTimeout(() => {
                            document.getElementById("redirP").innerHTML =
                                "Redirecting you to home in " +
                                (5 - i) +
                                " seconds";
                            if (i == 5) {
                                console.log("how bitch");
                                sessionStorage.setItem("justReload", "true");
                                window.location.reload();
                            }
                        }, i * 1000);
                    }
                });
            });
            return { isLogin, accessToken };
        },
        components: {},
        methods: {},
    };
</script>
