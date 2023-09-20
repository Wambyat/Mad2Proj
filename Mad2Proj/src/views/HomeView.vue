<template>
    <div class="home">
        <h1>Home</h1>
        <p id="access_token">before la change</p>
    </div>
</template>

<style scoped></style>

<script>
    import axios from "axios";
    import { ref, onMounted } from "vue";
    export default {
        data() {
            return {};
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
            onMounted(() => {
                console.log("Home mounted");
                document.getElementById("access_token").innerHTML =
                    "access_token: " + sessionStorage.getItem("accessToken");
                if (sessionStorage.getItem("accessToken") !== "") {
                    const yourConfig = {
                        headers: {
                            Authorization: "Bearer " + sessionStorage.getItem("accessToken"),
                        },
                    };
                    axios
                        .get("http://localhost:5000/test/", yourConfig)
                        .catch((error) => {
                            console.log(error);
                        }).then((response) => {
                            console.log(response);
                        });
                }
            });
        },
    };
</script>
