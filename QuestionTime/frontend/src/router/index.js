import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router
