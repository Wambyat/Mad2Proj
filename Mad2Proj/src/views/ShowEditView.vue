<template lang="">
    <div>
        <h1>Name: <input :value="dets[1]" /></h1>
        <p>Date: <input :value="dets[2]" type="date" /></p>
        <p>Venue ID: <input :value="dets[3]" /></p>
        <p>Seats: <input :value="dets[4]" /></p>
        <p>Details: <input :value="dets[6]" /></p>
    </div>
</template>
<script>
    import { ref } from "vue";
    import axios from "axios";
    export default {
        data() {
            return {
                dets: [],
                reactiveWidth: "fit-content",
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            const query = ref(props.query);
            const dets = ref([]);
            axios
                .get("http://localhost:5000/show/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                });

            return { dets };
        },
    };
</script>
<style scoped>
</style>
