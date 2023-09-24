<template lang="">
    <div>
        <p>Userame: <input :value="dets[1]" id="username" /></p>
        <p>Password: <input :value="dets[2]" id="password" /></p>
        <p>First Name: <input :value="dets[3]" id="fname" /></p>
        <p>Last Name: <input :value="dets[4]" id="lname" /></p>
        <p>Age: <input :value="dets[5]" id="age" type="number" /></p>
        <p>Email: <input :value="dets[6]" id="email" /></p>
        <button @click="editUser">Save</button>
        <button @click="sendShit">Send alerts to users</button>
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
        setup() {
            const dets = ref([]);
            const sessionStorage = window.sessionStorage;
            const router = useRouter();
            const yourConfig = {
                headers: {
                    Authorization:
                        "Bearer " + sessionStorage.getItem("accessToken"),
                },
            };
            if (sessionStorage.getItem("accessToken") !== "") {
                axios
                    .get("http://localhost:5000/user/", yourConfig)
                    .catch((error) => {
                        console.log(error);
                    })
                    .then((response) => {
                        const res = response.data;
                        console.log(res);
                        if (res["data"].length === 0) {
                            dets.value = [];
                        } else {
                            dets.value = res["data"][0];
                        }
                    });
            } else {
                alert("Login first");
                router.push("/login");
            }
            function editUser() {
                var uname = document.getElementById("username");
                var pass = document.getElementById("password");
                var fname = document.getElementById("fname");
                var lname = document.getElementById("lname");
                var age = document.getElementById("age");
                var email = document.getElementById("email");
                dets.value[1] = uname.value;
                dets.value[2] = pass.value;
                dets.value[3] = fname.value;
                dets.value[4] = lname.value;
                dets.value[5] = age.value;
                dets.value[6] = email.value;
                axios.post(
                    "http://localhost:5000/user/",
                    {
                        username: dets.value[1],
                        password: dets.value[2],
                        fname: dets.value[3],
                        lname: dets.value[4],
                        age: dets.value[5],
                        email: dets.value[6],
                    },
                    yourConfig
                );
            }
            function sendShit() {
                axios
                    .get("http://localhost:5000/alerts/")
                    .then((responce)=>{
                        console.log(responce.data);
                        alert("Alerts sent")
                    });
            }
            return { dets, editUser, sendShit };
        },
    };
</script>
