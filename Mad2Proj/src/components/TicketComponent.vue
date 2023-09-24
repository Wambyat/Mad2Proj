<template>
    <div>
        <h1>This is tickets</h1>
        <div v-if="isLogin !== 'true'">
        <h3>Please login first.</h3>
        </div>
        <div v-else v-for="ticket in tickets" :key="ticket.id">
            <p style="text-decoration-line: underline;">Ticket ID: {{ ticket[0] }}</p>
            <p>Seats: {{ ticket[2] }}</p>
            <p>Show: {{ ticket[3] }}</p>
            <p>Venue: {{ ticket[1] }}</p>
            <p>Date: {{ ticket[4] }}</p>
            <p>Details: {{ ticket[5] }}</p>
        </div>
    </div>
</template>
<script>
    import axios from "axios";
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    export default {
        data() {
            return {
                tickets: [],
                isAdmin: false,
                isLogin: "",
            };
        },
        setup() {
            const tickets = ref([]);
            const isAdmin = ref("false");
            const isLogin = ref("");
            const router = useRouter();
            const sessionStorage = window.sessionStorage;
            isAdmin.value = sessionStorage.getItem("admin");
            isLogin.value = sessionStorage.getItem("isLogin");
            
            if (sessionStorage.getItem("accessToken") !== "") {
                const yourConfig = {
                    headers: {
                        Authorization:
                            "Bearer " + sessionStorage.getItem("accessToken"),
                    },
                };
                axios
                    .get("http://localhost:5000/ticket/", yourConfig)
                    .catch((error) => {
                        console.log(error);
                    })
                    .then((response) => {
                        const res = response.data;
                        tickets.value = res["data"];
                    });
            }
            function goTicket(query) {
                console.log("sad");
            }
            return { tickets, goTicket, isAdmin, isLogin };
        },
    };
</script>

<style scoped>
    .title {
        cursor: pointer;
    }
</style>
