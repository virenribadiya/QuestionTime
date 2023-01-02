<template>
  <div class="home">
    <h1>Home page!!</h1>
    <button v-on:click="getQuestions">Load questions</button>
    <div v-if="questions">
      <li v-for="question in questions" v-bind:key="question.id">{{question}}</li>
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
  }
  
}
</script>
