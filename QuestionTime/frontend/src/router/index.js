import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import QuestionEditor from '../views/QuestionEditor.vue'
import AnswerEditor from '../views/AnswerEditor.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  
  {
    path: '/questions/:slug',
    name: 'quesTion',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "Question-time" */ '../views/Question.vue'),
    props:true,
  },
  {
    path: '/ask/:slug?', // question mark sign makes the slug optional.
    name: 'question-editor',
    component:QuestionEditor, 
    props:true,
  },
  {
    path: '/answer/:uuid', // question mark sign makes the slug optional.
    name: 'answer-editor',
    component:AnswerEditor, 
    props:true,
  }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router
