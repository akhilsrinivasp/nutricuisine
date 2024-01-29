import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/edit/user/:what',
    name: 'edit_user',
    component: ()  => import(/* webpackChunkName: "login" */ '../components/EditUser.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import(/* webpackChunkName: "signup" */ '../views/SignupView.vue')
  },
  { 
    path: '/logout',
    name: 'logout',
    component: () => import(/* webpackChunkName: "logout" */ '../components/LogoutComp.vue')
  }, 
  {
    path: '/user/:username',
    name: 'user',
    component: () => import(/* webpackChunkName: "user" */ '../views/UserView.vue'),
  },
  {
    path: '/recommend/recipe',
    name: 'recommend_recipe',
    component: () => import(/* webpackChunkName: "user" */ '../views/RecommendRecipe.vue'),
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import(/* webpackChunkName: "user" */ '../views/UserView.vue'),
  },
  {
    path: '/consumption/statistics',
    name: 'ConsumptionStats',
    component: () => import(/* webpackChunkName: "user" */ '../views/ComsumptionStats.vue'),
  },
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
