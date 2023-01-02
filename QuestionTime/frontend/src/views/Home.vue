<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="question in questions" :key="question.uuid">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0 ">
              Posted by :
              <span class="question-author">{{question.author}}</span>
            </p>
            <h2>{{question.content}}</h2>
            <p class="mb-0">
              Answers : {{question.answers_count}}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import {axios} from "@/common/api.service.js";

export default {
  name: 'HomeView',

  data()
  {
    return{
      questions:[]
    }
  },
  methods:
  {
    async getQuestions(){
      let endpoint = "/api/v1/questions/";
      try {
        const response = await axios.get(endpoint);
        //console.log(response);
        this.questions = response.data;
        console.log(this.questions);
         
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  },
  created(){
    console.log("Created....life cycle hook");
    this.getQuestions();
  }
  
}
</script>

<style>
  .question-author
  {
    font-weight: bold;
    color: #dc3545;
  }
</style>
