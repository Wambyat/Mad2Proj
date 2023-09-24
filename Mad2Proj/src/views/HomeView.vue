<template>
    <div class="home">
        <h1>Choose and browse below!</h1>
        <tabs :options="{ useURLFragment: false }">
            <tab name="Shows">
                <ShowComponent />
            </tab>
            <tab name="Venues">
                <VenueComponent />
            </tab>
            <tab
                v-if="isAdmin != true"
                name="Tickets"
                id="ticket"
                style="display: ">
                <TicketComponent />
            </tab>
        </tabs>
    </div>
</template>

<script>
    import axios from "axios";
    import { ref, onMounted } from "vue";
    import ShowComponent from "@/components/ShowComponent.vue";
    import VenueComponent from "@/components/VenueComponent.vue";
    import TicketComponent from "@/components/TicketComponent.vue";
    export default {
        data() {
            return {
                isAdmin: false,
                isLogin: "",
            };
        },
        setup() {
            const isAdmin = ref("false");
            const isLogin = ref("");
            const testTabs = ref(null);
            function ran() {
                // console.log("ran");
                if (isLogin.value === "false") {
                    // document.getElementById("ticket").style.display = "none";
                } else {
                    // console.log("ran2");
                }
            }
            const sessionStorage = window.sessionStorage;
            isAdmin.value = sessionStorage.getItem("admin");
            isLogin.value = sessionStorage.getItem("isLogin");
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
                setTimeout(ran, 2000);
            });
            return { isAdmin };
        },
        components: {
            ShowComponent,
            VenueComponent,
            TicketComponent,
        },
    };
</script>
