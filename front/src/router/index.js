import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ForestslistView from '@/views/forests/ForestslistView.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import NotFound404 from '@/views/accounts/NotFound404.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import ProfileEditView from '@/views/accounts/ProfileEditView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/forests',
    name: 'forests',
    component: ForestslistView
  },
  // accounts 시작
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/:username/edit',
    name: 'profileEdit',
    component: ProfileEditView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  // accounts 끝
  // NotFound404 시작
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }, 
  // NotFound404 끝
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
