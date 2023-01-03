<template>
    <div class="card shadow p-2 mb-4 bg-body rounded">
        <p class="text-muted">
            <strong>{{answer.author}} &#8901; {{answer.created_at}}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{answer.body}}</p>
        <div v-if="isAnswerAuthor">
            <router-link :to="{name:'answer-editor', params:{uuid:answer.uuid}}" class="btn btn-sm btn-warning">
                Edit
            </router-link>
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
    computed:
    {
        isAnswerAuthor(){
            return this.answer.author === this.requestUser;
        }
    }
    
}
</script>


<style>
.shadow-color{
    box-shadow: lightgreen;
}
</style>