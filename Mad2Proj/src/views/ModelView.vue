<template lang="">
    <div>
        <p>Userame: <input :value="dets[1]" id="username" /></p>
        <p>Password: <input :value="dets[2]" id="password" /></p>
        <p>First Name: <input :value="dets[3]" id="fname" /></p>
        <p>Last Name: <input :value="dets[4]" id="lname" /></p>
        <p>Age: <input :value="dets[5]" id="age" type="number" /></p>
        <p>Email: <input :value="dets[6]" id="email" /></p>
        <button @click="editUser">Save</button>
        <button v-if="isAdmin == 'true'" @click="sendShit">Send alerts to users</button>
        <h2 v-if="isAdmin != 'true'">Below is your report</h2>
        <div  v-if="isAdmin != 'true'" id="report">
            <!-- loop thru array report -->
            <div v-for="re in report" :key="re.id">
                <p>TID: {{ re[0] }}</p>
                <p>Show: {{ re[1] }}</p>
                <p>Date: {{ re[2] }}</p>
                <p>Seats: {{ re[3] }}</p>
            </div>
        </div>
        <button @click="saveFile"  v-if="isAdmin != 'true'">Save HTML</button>
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
                report: [],
                isAdmin: false,
            };
        },
        setup() {
            const dets = ref([]);
            const isAdmin = ref(false);
            const report = ref([]);
            const sessionStorage = window.sessionStorage;
            isAdmin.value = sessionStorage.getItem("admin");
            console.log(isAdmin.value)
            const router = useRouter();
            const yourConfig = {
                headers: {
                    Authorization:
                        "Bearer " + sessionStorage.getItem("accessToken"),
                },
            };
            const isLogin = sessionStorage.getItem("isLogin");
            if (isLogin === "true") {
                axios
                    .get("http://localhost:5000/report/", yourConfig)
                    .catch((error) => {
                        console.log(error);
                    })
                    .then((response) => {
                        const res = response.data;
                        console.log(res);
                        if (res["data"].length === 0) {
                            report.value = [];
                        } else {
                            report.value = res["data"];
                        }
                    });
            }

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
                axios.get("http://localhost:5000/alerts/").then((responce) => {
                    console.log(responce.data);
                    alert("Alerts sent");
                });
            }
            function saveFile() {
                const html = document.getElementById("report").innerHTML;
                const blob = new Blob([html], { type: "text/html" });
                const link = document.createElement("a");
                link.href = URL.createObjectURL(blob);
                link.download = "output.html";
                link.click();
            }
            return { dets, editUser, sendShit, isAdmin, saveFile, report };
        },
    };
</script>
