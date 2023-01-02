<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="question in questions" :key="question.uuid">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0 ">
              Posted by :
              <span class="question-author">{{  question.author  }}</span>
            </p>
            <h2>{{  question.content  }}</h2>
            <p class="mb-0">
              Answers : {{  question.answers_count  }}
            </p>
          </div>
        </div>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">Loading....</p>
        <button v-show="next" @click="getQuestions" class="btn btn-sm btn-outline-success">
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import { axios } from "@/common/api.service.js";

export default {
  name: 'HomeView',

  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false,

    }
  },
  methods:
  {
    async getQuestions() {
      let endpoint = "/api/v1/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      try {
        const response = await axios.get(endpoint);
        //console.log(response);
        this.questions.push(...response.data.results);
        this.loadingQuestions = false;
        if (response.data.next) {
          this.next = response.data.next;
        }
        else {
          this.next = null;
        }
        console.log(this.questions);

      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  },
  created() {
    console.log("Created....life cycle hook");
    this.getQuestions();
  }

}
</script>

<style>
.question-author {
  font-weight: bold;
  color: #dc3545;
}
</style>
