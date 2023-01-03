<template>
    <div class="card shadow p-2 mb-4 bg-body rounded">
        <p class="text-muted">
            <strong>{{answer.author}} &#8901; {{answer.created_at}}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{answer.body}}</p>
    </div>

</template>


<script>


export default{
    name:"AnsewerComponent",
    props: {
        answer:{
            type:Object,
            required:true
        }
    }
}
</script>


<style>
.shadow-color{
    box-shadow: lightgreen;
}
</style>