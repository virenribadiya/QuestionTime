<template>
    <div class="card shadow p-2 mb-4 bg-body rounded">
        <p class="text-muted">
            <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{ answer.body }}</p>
        <div v-if="isAnswerAuthor">
            <router-link :to="{ name: 'answer-editor', params: { uuid: answer.uuid } }" class="btn btn-sm btn-warning">
                Edit
            </router-link>
            <button class="btn btn-sm btn-danger mx-2"
                @click="showDeleteConfirmationBtn = !showDeleteConfirmationBtn">Delete</button>

            <button v-show="showDeleteConfirmationBtn" class="btn btn-sm btn-outline-danger"
                @click="triggerDeleteAnswer">Yes, delete my answer!</button>
        </div>
        <div v-else>
            <button class="btn" 
            @click="toggleLike"
            :class="{'btn-warning':userLikedAnswer, 'btn-outline-danger':!userLikedAnswer}">
                Like Answer &nbsp;<span class="badge bg-danger">{{likesCounter}}</span>
            </button>
        </div>
    </div>

</template>


<script>

import { axios } from "@/common/api.service.js";

export default {
    name: "AnsewerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true,
        }
    },
    data() {
        return {
            showDeleteConfirmationBtn: false,
            userLikedAnswer: this.answer.user_has_liked,
            likesCounter: this.answer.likes_count,
        }
    },
    computed:
    {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods:
    {
        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer);
        },
        toggleLike() {
            this.userLikedAnswer === false ? this.likeAnswer() : this.unLikeAnswer();
        },
        async likeAnswer() {
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            const endpoint = `/api/v1/answers/${this.answer.uuid}/likes/`;
            try {
                await axios.post(endpoint);
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },
        async unLikeAnswer() {
            this.userLikedAnswer = false;
            this.likesCounter -= 1;
            const endpoint = `/api/v1/answers/${this.answer.uuid}/likes/`;
            try {
                await axios.delete(endpoint);
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },
    }

}
</script>


<style>
.shadow-color {
    box-shadow: lightgreen;
}
</style>