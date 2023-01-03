<template>
    <div class="container mt-3">
        <div v-if="question">
            <h1>{{question.content}}</h1>
            <p class="mb-0 ">
              Posted by :
              <span class="question-author">{{  question.author  }}</span>
            </p>
            <p>
                {{question.created_at}}
            </p>
        </div>
        <div v-else class="error text-center h3">
            404 - Question Not Found
        </div>
    </div>
</template>


<script>

import { axios } from "@/common/api.service.js";

export default{
    name:"QuesTion",
    props:
    {
        slug:{
            type:String,
            required:true,
        }
    },
    data()
    {
        return{
            question: null,
        }
    },
    methods:
    {
        setPageTitle(title){
            document.title = title;
        },
        async getQuestionData(){
            const endpoint = `/api/v1/questions/${this.slug}/`;
            try {
                const response = await axios.get(endpoint);
                this.question = response.data;
                this.setPageTitle(response.data.content);
            } catch (error) {
                console.log(error.response);
                const title = "404 - Not Found!";
                this.setPageTitle(title);
                alert(error.response.statusText);     
            }
        }
    },
    created()
    {
        this.getQuestionData();
    }
}
</script>



<style>
.question-author{
    font-weight: bold;
    color: #dc3545;
}
.error{
    color: #dc3545;
}
</style>