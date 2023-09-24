<template lang="">
    <div>
        <h1>
            {{ dets[1] }}
        </h1>
        <p>{{ dets[2] }}</p>
        <p>{{ dets[3] }}</p>
        <p>{{ dets[4] }}</p>
        <p>{{ dets[5] }}</p>
        <p>{{ dets[6] }}</p>
        <div>
            <p>Tags:</p>
            <div v-for="tag in tags" :key="tag[0]">
                <ul>{{ tag[0] }}</ul>
            </div>
        </div>

        <div v-if="isAdmin === 'true'">
            <p @click="goShowEdit(dets[0])" class="clickable">
                Click me to edit or delete
            </p>
        </div>
        <div v-else-if="isLogin === 'true'">
            <p @click="goTicket(dets[0])" class="clickable">Book a ticket!</p>
        </div>
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
                isLogin: "false",
                isAdmin: "false",
                tags: [],
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            const query = ref(props.query);
            const dets = ref([]);
            const isLogin = ref("false");
            const isAdmin = ref("false");
            const tags = ref([]);
            const sessionStorage = window.sessionStorage;
            isLogin.value = sessionStorage.getItem("isLogin");
            isAdmin.value = sessionStorage.getItem("admin");
            const router = useRouter();
            axios
                .get("http://localhost:5000/show/" + query.value)
                .then((responce) => {
                    const res = responce.data;
                    dets.value = res["data"][0];
                    axios.get("http://localhost:5000/show/tags/" + query.value).then((responce) => {
                        const res = responce.data;
                        tags.value = res["data"];
                    });
                });
            function goShowEdit(query) {
                router.push("/show/edit/" + query);
            }
            function goTicket(query) {
                router.push("/ticket/" + query);
            }
            return { dets, goShowEdit, isLogin, isAdmin, goTicket, tags };
        },
    };
</script>
<style scoped>
    .clickable {
        cursor: pointer;
    }
</style>
