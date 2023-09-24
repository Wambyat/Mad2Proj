<template lang="">
    <div>
        <h1>
            {{ dets[1] }}
        </h1>
        <p>{{ dets[2] }}</p>
        <p>{{ dets[3] }}</p>
        <div v-if="isAdmin == true">
            <p @click="goShowEdit(dets[0])" class="clickable">
                Click me to edit or delete
            </p>
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
            const sessionStorage = window.sessionStorage;
            isLogin.value = sessionStorage.getItem("isLogin");
            isAdmin.value = sessionStorage.getItem("admin");
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
            return { dets, goVenueEdit, isLogin, isAdmin };
        },
    };
</script>
<style scoped>
    .clickable {
        cursor: pointer;
    }
</style>
