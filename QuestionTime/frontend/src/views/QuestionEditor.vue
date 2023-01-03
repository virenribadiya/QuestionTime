<template>
    <div class="container mt-2">
      <h1 class="mb-3">Ask a Question</h1>
      <form @submit.prevent="onSubmit">
        <textarea
          v-model="questionBody"
          class="form-control"
          placeholder="What do you want to ask?"
          rows="3"
        ></textarea>
        <button type="submit" class="btn btn-success mt-3">Publish</button>
      </form>
      <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import { axios } from "@/common/api.service.js";

  export default {
    name: "QuestionEditor",
    data() {
      return {
        questionBody: null,
        error: null,
      }
    },
    props:
    {
      slug:{
        type:String,
        requied:false
      }
    },
    methods: {
      async performNetworkRequest() {
        // Tell the REST API to create or update a Question instance;
        let endpoint = "/api/v1/questions/";
        let method = "POST";
        if(this.slug !== undefined && this.slug !== ""){
          endpoint = endpoint+`${this.slug}/`;
          method = "PUT";
        }
        try {
          const response = await axios({
            method: method,
            url: endpoint,
            data: { content: this.questionBody },
          });
          this.$router.push({
            name: "quesTion",
            params: { slug: response.data.slug },
          });
        } catch (error) {
          this.error = error.response.statusText;
        }
      },
      onSubmit() {
        // perform basic validation and eventually call this.performNetworkRequest;
        if (!this.questionBody) {
          this.error = "You can't send an empty question!";
        } else if (this.questionBody.length > 200) {
          this.error = "Ensure this field has no more than 240 characters!";
        } else {
          this.performNetworkRequest();
        }
      },
    },
    created() {
      document.title = "Editor - QuestionTime";
    },
    async beforeRouteEnter(to,from,next){
      if(to.params.slug !== undefined && to.params.slug !== "")
      {
        const endpoint = `/api/v1/questions/${to.params.slug}/`;
        try {
          const response = await axios.get(endpoint);
          return next(vm => vm.questionBody = response.data.content);
        } catch (error) {
          console.log(error);
        }
      }else
      {
        return next();
      }
    }
  };
  </script>