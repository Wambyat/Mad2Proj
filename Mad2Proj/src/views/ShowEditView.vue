<template lang="">
    <div>
        <h1>Name: <input :value="dets[1]" id="name" /></h1>
        <p>Date: <input :value="dets[2]" type="date" id="date" /></p>
        <p>Venue ID: <input :value="dets[3]" id="venueid" /></p>
        <p>Seats: <input :value="dets[4]" id="seats" /></p>
        <p>Details: <input :value="dets[6]" id="details" /></p>
        <button @click="updateShow">Save</button>
        <button @click="delConfirm = !delConfirm">Delete</button>
        <button v-if="delConfirm" @click="deleteShow">
            I'm sure I want to delete
        </button>
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
                delConfirm: false,
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
                .get("http://localhost:5000/show/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                });
            function updateShow() {
                var name = document.getElementById("name");
                var date = document.getElementById("date");
                var venueid = document.getElementById("venueid");
                var seats = document.getElementById("seats");
                var details = document.getElementById("details");
                dets.value[1] = name.value;
                dets.value[2] = date.value;
                dets.value[3] = venueid.value;
                dets.value[4] = seats.value;
                dets.value[6] = details.value;
                // console.log(dets.value)
                axios
                    .post("http://localhost:5000/show/edit/" + query.value, {
                        name: dets.value[1],
                        date: dets.value[2],
                        venue_id: dets.value[3],
                        seats: dets.value[4],
                        details: dets.value[6],
                    })
                    .then((responce) => {
                        const res = responce.data;
                        console.log(res);
                    });
            }
            function deleteShow() {
                axios
                    .get("http://localhost:5000/show/delete/" + query.value)
                    .then((responce) => {
                        const res = responce.data;
                        console.log(res);
                        
                        router.push("/");
                    });
            }
            return { dets, updateShow, deleteShow, delConfirm };
        },
    };
</script>
<style scoped></style>
