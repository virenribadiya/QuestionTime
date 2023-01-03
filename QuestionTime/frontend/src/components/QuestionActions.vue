
<template>
    <div class="mt-3 mb-2">
        <router-link :to="{ name: 'question-editor', params: { slug: slug } }"
            class="btn btn-sm btn-warning me-2">Edit</router-link>
        <button class="btn btn-sm btn-danger" @click="(showDeleteConfirmationBtn = !showDeleteConfirmationBtn)">
            Delete
        </button>
        <button v-show="showDeleteConfirmationBtn" class="btn btn-sm btn-outline-danger mx-2" @click="deleteQuestion">
            Yes, delete my question!
        </button>
        <hr>
    </div>
</template>


<script>

import { axios } from "@/common/api.service.js";
export default {
    name: "QuestionActions",
    data() { 
        return{
            showDeleteConfirmationBtn: false
        }
    },
    props: {
        slug: {
            type: String,
            required: true,
        }
    },
    methods:
    {
        async deleteQuestion() {
            const endpoint = `/api/v1/questions/${this.slug}/`;
            try {
                await axios.delete(endpoint);
                this.$router.push({
                    name: "home"
                })
            } catch (error) {
                console.log(error);
            }
        }
    }
};

</script>