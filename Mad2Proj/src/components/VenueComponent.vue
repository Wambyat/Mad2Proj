<template>
    <div>
        <h1>This is venue</h1>
        <div v-if="isAdmin === 'true'">
            <router-link to="/venue/new">Add new show</router-link>
        </div>
        <div v-for="venue in venues" :key="venue.id">
            <h3 @click="goVenue(venue[0])" class="title" style="text-decoration-line: underline;">{{ venue[1] }}</h3>
            <p>{{ venue[2] }}</p>
            <p>{{ venue[3] }}</p>
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
                venues: [],
                isAdmin: false,
            };
        },
        setup()
        {
            const venues = ref([]);
            const isAdmin = ref("false");
            const router = useRouter();
            const sessionStorage = window.sessionStorage;
            isAdmin.value = sessionStorage.getItem("admin");
            console.log("isAdmin: "+isAdmin.value);
            axios.get("http://localhost:5000/venue").then((responce) => {
                const res = responce.data;
                venues.value = res["data"];
            });
            function goVenue(query) {
                
                router.push("/venue/" + query);
            }
            return { venues, goVenue, isAdmin };
        },
    };
</script>

<style scoped>
    .title {
        cursor: pointer;
    }
</style>
