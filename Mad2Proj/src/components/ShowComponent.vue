<template>
    <div>
        <h1>This is shows</h1>
        <div v-for="show in shows" :key="show.id">
            <h3 @click="goShow(show[0])" class="title">{{ show[1] }}</h3>
            <p>{{ show[6] }}</p>
            <p>{{ show[2] }}</p>
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
                shows: [],
            };
        },
        setup() {
            const shows = ref([]);
            const router = useRouter();
            axios.get("http://localhost:5000/show").then((responce) => {
                const res = responce.data;
                shows.value = res["data"];
            });
            function goShow(query) {
                
                router.push("/show/" + query);
            }
            return { shows, goShow };
        },
    };
</script>

<style scoped>
    .title {
        cursor: pointer;
    }
</style>
