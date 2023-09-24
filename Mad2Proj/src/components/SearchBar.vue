<template>
    <div>
        <input
            v-model="searchQuery"
            @input="genList"
            placeholder="Search for the company"
            :id="searchData"
            style="min-width: 40%; border: none" />
        <div class="search-list">
            <p v-if="filteredData.error">{{ filteredData.error }}</p>
            <!-- This is what makes the dynamic list -->
            <ul v-else v-for="(item, key) in filteredData" :key="key">
                <router-link
                    style="text-decoration: none"
                    :to="{ name: searchData, params: { query: key } }">
                    <li class="st">{{ key }}: {{ item }}</li>
                </router-link>
            </ul>
        </div>
    </div>
</template>

<style scoped>
    .st {
        color: black;
        cursor: pointer;
        /* no underlined */
        text-decoration: none;
    }

    .search-list ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
        border-bottom: 1px solid #ddd;
        padding: 10px;
        cursor: pointer;
    }
    .search-list ul:hover {
        background-color: #f1f1f1;
    }
    .search-list::-webkit-scrollbar {
        width: 20px;
        background-color: #f1f1f1;
        border-bottom-right-radius: 15px;
    }
    .search-list::-webkit-scrollbar-thumb {
        background-color: #888;
        border: 5px solid transparent;
        width: 50px;
        border-radius: 50px;
        background-color: #8070d4;
        background-clip: content-box;
    }

    .search-list::-webkit-scrollbar-track {
        background-color: #e4e4e4;
        border-bottom-right-radius: 15px;
    }
    .search-list {
        max-height: 300px;
        max-width: 40%;
        overflow-y: scroll;
        border-radius: 15px;
        box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25),
            0 10px 10px rgba(0, 0, 0, 0.22);
    }
</style>

<script>
    import { ref, onMounted } from "vue";
    let mainList;
    export default {
        props: ["searchData"],
        data() {
            return {
                searchQuery: "",
                filteredData: {},
            };
        },
        setup(props) {
            const searchData = ref(props.searchData);
            const filteredData = ref({});
            async function getAll() {
                    try {
                        
                        const response = await fetch(
                            "http://localhost:5000/" + searchData.value
                        );
                        const data = await response.json();
                        const columns = [1, 6]; // specify the column indices you want to select
                        let selectedColumns = new Array();
                        selectedColumns.map((row) => {
                            return columns.map(
                                (columnIndex) => row[columnIndex]
                            );
                        });
                        return data;
                    } catch (error) {
                        console.error(error);
                    }
                };
                mainList = getAll();
            function genList() {
                function filterJson(jsonData, input) {
                    const filteredJson = {};
                    if (input.length < 3) {
                        return { error: "Please enter more than 2 characters" };
                    }
                    // console.log("searchData.value: " + searchData.value)
                    if (searchData.value === "venue") {
                        for (const key in jsonData["data"]) {
                            var row = jsonData["data"][key];
                            // console.log("venue: "+row);
                            if (
                                row[1]
                                    .toLowerCase()
                                    .includes(input.toLowerCase()) ||
                                row[2]
                                    .toLowerCase()
                                    .includes(input.toLowerCase()) ||
                                row[3]
                                    .toLowerCase()
                                    .includes(input.toLowerCase())
                            ) {
                                filteredJson[row[0]] = row;
                            }
                        }
                    } else {
                        for (const key in jsonData["data"]) {
                            // console.log("key: " + key)
                            var row = jsonData["data"][key];
                            // console.log("row: "+row[1]);
                            if (
                                row[1]
                                    .toLowerCase()
                                    .includes(input.toLowerCase()) ||
                                row[6]
                                    .toLowerCase()
                                    .includes(input.toLowerCase())
                            ) {
                                filteredJson[row[0]] = row;
                            }
                        }
                    }
                    return filteredJson;
                }
                var id = searchData.value;
                const userInput = document.getElementById(id).value;
                mainList = getAll().then((res) => {
                    mainList = res;
                    filteredData.value = filterJson(mainList, userInput);
                });
                
            }
            return { searchData, genList,filteredData };
        },
    };
</script>
