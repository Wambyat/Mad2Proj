<template lang="">
    <div>
        <h1>Name: <input :value="dets[1]" id="name"/></h1>
        <p>Address: <input :value="dets[2]" id="address"/></p>
        <p>Style: <input :value="dets[3]" id="style"/></p>
        <button @click="updateVenue">Save</button>
        <button @click="delConfirm = !delConfirm">Delete</button>
        <button v-if="delConfirm" @click="deleteVenue">I'm sure I want to delete</button>
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
                reactiveWidth: "fit-content",
                delConfirm : false,
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            const query = ref(props.query);
            const dets = ref([]);
            const delConfirm = ref(false);
            const router = useRouter();
            axios
                .get("http://localhost:5000/venue/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                });
                function updateVenue() {
                    var name = document.getElementById("name");
                    var address = document.getElementById("address");
                    var style = document.getElementById("style");
                    dets.value[1] = name.value;
                    dets.value[2] = address.value;
                    dets.value[3] = style.value;
                    axios
                        .post("http://localhost:5000/venue/edit/"+ query.value, {
                            name: dets.value[1],
                            address: dets.value[2],
                            style: dets.value[3],
                        }).then((responce) => {
                            const res = responce.data;
                            console.log(res);
                        });
            }
            function deleteVenue() {
                axios
                    .get("http://localhost:5000/venue/delete/"+ query.value).then((responce) => {
                        const res = responce.data;
                        console.log(res);
                        router.push("/");
                    });
            }
            return { dets, updateVenue, deleteVenue, delConfirm };
        },
    };
</script>
<style scoped>
</style>
