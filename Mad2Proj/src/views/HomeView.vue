<template>
    <div class="home">
        <h1>Home</h1>
    </div>
</template>

<style scoped>
</style>

<script>
    import { ref, onMounted } from "vue";
    import axios from "axios";
    export default {
        data() {
        },
        setup() {
            
            onMounted(async () => {
                console.log("Test")
            });
        },
        components: {
        },
        methods: {
        },
    };
</script>
