<template lang="">
    <div>
        <h1>
            {{ dets[1] }}
        </h1>
        <p>{{ dets[2] }}</p>
        <p>{{ dets[3] }}</p>
        <div v-if="isAdmin === 'true'">
            <p @click="goVenueEdit(dets[0])" class="clickable">
                Click me to edit or delete
            </p>
            <p @click="exportThingy()" class="clickable">Click me to export</p>
        </div>
    </div>
</template>
<script>
    import { ref } from "vue";
    import axios from "axios";
    import { useRouter } from "vue-router";
    import exportFromJSON from "export-from-json";
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
            function exportDataFromJSON(data, newFileName, fileExportType) {
                if (!data) return;
                try {
                    const fileName = newFileName || "exported-data";
                    const exportType =
                        exportFromJSON.types[fileExportType || "csv"];
                    exportFromJSON({ data, fileName, exportType });
                } catch (e) {
                    throw new Error("Parsing failed!");
                }
            }
            function exportThingy() {
                console.log("here:(");
                axios
                    .get("http://localhost:5000/venue/export/" + query.value)
                    .then((responce) => {
                        const tickets = responce.data["tickets"];
                        exportDataFromJSON(tickets, "tickets"+query.value, "csv");
                        const shows = responce.data["shows"];
                        exportDataFromJSON(shows, "shows"+query.value, "csv");
                        alert("Export Finished. CSVs saved in Downloads folder.")
                    });
            }
            return { dets, goVenueEdit, isLogin, isAdmin, exportThingy };
        },
    };
</script>
<style scoped>
    .clickable {
        cursor: pointer;
    }
</style>
