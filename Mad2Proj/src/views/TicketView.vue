<template lang="">
    <div>
        <h1>Name: {{dets[1]}}</h1>
        <p>Date: {{dets[2]}}</p>
        <p>Venue ID: {{dets[3]}}</p>
        <p>Seats Left: {{dets[4]}}</p>
        <p>Details: {{dets[6]}}</p>
        <p>Seats you want to book: <input type="number" id="bookseats" /></p>
        <p>Seats already booked: {{ticBooked}}</p>
        <button @click="delConfirm = !delConfirm">Book</button>
        <button v-if="delConfirm" @click="bookTicket">
            I'm sure I want to Book
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
                ticBooked: 0,
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
            const ticBooked = ref(0);
            axios
                .get("http://localhost:5000/show/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                    const yourConf = {
                        headers: {
                            Authorization:
                                "Bearer " +
                                sessionStorage.getItem("accessToken"),
                        }
                    };
                    axios.get("http://localhost:5000/ticket/", yourConf)
                        .then((responce) => {
                            const res = responce.data;
                            //  check if loop thru res and see if i[3] === dets[1]
                            //  if so, add to ticBooked
                            for (let i = 0; i < res["data"].length; i++) {
                                if (res["data"][i][3] === dets.value[1]) {
                                    ticBooked.value += res["data"][i][2];
                                    console.log(ticBooked.value);
                                }
                            }
                        });
                });
            function bookTicket() {
                const yourConfig = {
                        headers: {
                            Authorization:
                                "Bearer " +
                                sessionStorage.getItem("accessToken"),
                        }
                    };
                axios
                    .post("http://localhost:5000/ticket/" + query.value,
                        {
                            seats: document.getElementById("bookseats").value,
                        }, yourConfig)
                    .then((responce) => {
                        router.push("/");
                    });
                // axios
                //     .post("http://localhost:5000/ticket/" + query.value,
                //         {
                //             seats: document.getElementById("bookseats").value,
                //         })
                //     .then((responce) => {
                //         router.push("/");
                //     });
            }
            return { dets, bookTicket, delConfirm, ticBooked };
        },
    };
</script>
<style scoped></style>
