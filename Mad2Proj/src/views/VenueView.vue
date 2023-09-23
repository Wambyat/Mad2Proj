<template lang="">
    <div>
        <h1>
            {{ dets[1] }}
        </h1>
        <p>{{ dets[2] }}</p>
        <p>{{ dets[3] }}</p>
        <p @click="goVenueEdit(dets[0])" class = "clickable">Click me to edit or delete</p>
    </div>
</template>
<script>
    import { ref } from "vue";
    import axios from "axios";
    import { useRouter } from "vue-router";
    export default {
        data() {
            return {
                dets: [],
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            const query = ref(props.query);
            const dets = ref([]);
            const router = useRouter();
            axios
                .get("http://localhost:5000/venue/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                });
                function goVenueEdit(query) {
                
                router.push("/venue/edit/" + query);
            }
            return { dets,goVenueEdit };
        },
    };
</script>
<style scoped>
.clickable{
    cursor: pointer;
}
</style>
