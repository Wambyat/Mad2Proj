<template lang="">
    <div>
        <h1>Name: <input :value="dets[1]" id="name" /></h1>
        <p>Address: <input :value="dets[2]" id="address" /></p>
        <p>Style: <input :value="dets[3]" id="style" /></p>
        <button @click="addVenue">Save</button>
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
            dets.value = ["", "", "", ""];
            function addVenue() {
                var name = document.getElementById("name");
                var address = document.getElementById("address");
                var style = document.getElementById("style");
                dets.value[1] = name.value;
                dets.value[2] = address.value;
                dets.value[3] = style.value;
                axios
                    .post("http://localhost:5000/venue/add", {
                        name: dets.value[1],
                        address: dets.value[2],
                        style: dets.value[3],
                    })
                    .then((responce) => {
                        const res = responce.data;
                        console.log(res);
                    });
            }
            return { dets, addVenue };
        },
    };
</script>
<style scoped></style>
