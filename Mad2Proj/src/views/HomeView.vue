<template>
    <div class="home">
        <h1>Home</h1>
        <tabs :options="{ useURLFragment: false }">
            <tab name="Shows">
                <ShowComponent />
            </tab>
            <tab name="Venues">
                <VenueComponent />
            </tab>
        </tabs>
    </div>
</template>

<script>
    import axios from "axios";
    import { ref, onMounted } from "vue";
    import ShowComponent from "@/components/ShowComponent.vue";
    import VenueComponent from "@/components/VenueComponent.vue";
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
                if (sessionStorage.getItem("accessToken") !== "") {
                    const yourConfig = {
                        headers: {
                            Authorization:
                                "Bearer " +
                                sessionStorage.getItem("accessToken"),
                        },
                    };
                    axios
                        .get("http://localhost:5000/test/", yourConfig)
                        .catch((error) => {
                            console.log(error);
                        })
                        .then((response) => {
                            console.log(response);
                        });
                }
            });
        },
        components: {
            ShowComponent,
            VenueComponent,
        },
    };
</script>
