<template>
    <div class="card shadow p-2 mb-4 bg-body rounded">
        <p class="text-muted">
            <strong>{{answer.author}} &#8901; {{answer.created_at}}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{answer.body}}</p>
        <div v-if="isAnswerAuthor">
            <router-link :to="{name:'answer-editor', params:{uuid:answer.uuid}}" 
            class="btn btn-sm btn-warning">
                Edit
            </router-link>
            <button class="btn btn-sm btn-danger mx-2" 
            @click="showDeleteConfirmationBtn=!showDeleteConfirmationBtn">Delete</button>

            <button v-show="showDeleteConfirmationBtn" class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">Yes, delete my answer!</button>
        </div>
    </div>

</template>


<script>



export default{
    name:"AnsewerComponent",
    props: {
        answer:{
            type:Object,
            required:true
        },
        requestUser:{
            type:String,
            required:true,
        }
    },
    data(){
        return{
            showDeleteConfirmationBtn: false,
        }
    },
    computed:
    {
        isAnswerAuthor(){
            return this.answer.author === this.requestUser;
        }
    },
    methods:
    {
        triggerDeleteAnswer(){
            this.$emit("delete-answer",this.answer);
        }
    }
    
}
</script>


<style>
.shadow-color{
    box-shadow: lightgreen;
}
</style>