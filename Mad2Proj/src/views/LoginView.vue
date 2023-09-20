<template>
    <div class="login">
        <h1>Auth page</h1>
        <div v-if="isLogin === 'false'">
            <form>
                <label for="username">Username: </label>
                <input type="text" id="username" v-model="input.username" />
                <label for="password">Password: </label>
                <input type="password" id="password" v-model="input.password" />
                <button
                    id="submitButton"
                    type="submit"
                    v-on:click.prevent="login()">
                    Login
                </button>
            </form>
            <p id="error"></p>
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
                input: {
                    username: "",
                    password: "",
                },
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
                console.log("Login mounted");
            });
            return { isLogin, accessToken };
        },
        components: {},
        methods: {
            login() {
                const username = this.input.username;
                const password = this.input.password;
                const params = {
                    username: username,
                    password: password,
                };
                axios
                    .post("http://localhost:5000/login", params)
                    .then((responce) => {
                        const res = responce.data;
                        console.log(res);
                        if (res["error"]) {
                            document.getElementById("error").innerHTML =
                                res["error"];
                        } else {
                            const sessionStorage = window.sessionStorage;
                            sessionStorage.setItem("isLogin", "true");
                            sessionStorage.setItem(
                                "accessToken",
                                res["access_token"]
                            );
                            if (res["admin"])
                            {
                                sessionStorage.setItem("admin", "true");
                            }
                            this.isLogin = sessionStorage.getItem("isLogin");
                            this.accessToken =
                                sessionStorage.getItem("accessToken");
                            for (let i = 0; i < 6; i++) {
                                setTimeout(() => {
                                    document.getElementById(
                                        "redirP"
                                    ).innerHTML =
                                        "Redirecting you to home in " +
                                        (5 - i) +
                                        " seconds";
                                    if (i == 5) {
                                        sessionStorage.setItem(
                                            "justReload",
                                            "true"
                                        );
                                        window.location.reload();
                                    }
                                }, i * 1000);
                            }
                        }
                    });
            },
        },
    };
</script>
