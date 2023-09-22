<template lang="">
    <div>
        <h1>
            <input :value="dets[1]" />
        </h1>
        <p><input :value="dets[2]" /></p>
        <p><input :value="dets[3]" /></p>
        <button @click="callSQL">Save</button>
    </div>
</template>
<script>
    import { ref } from "vue";
    import axios from "axios";
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
            axios
                .get("http://localhost:5000/venue/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                });
                
            return { dets };
        },
    };
</script>
<style lang=""></style>
