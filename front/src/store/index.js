import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import communities from './modules/communities'
import home from './modules/home'

Vue.use(Vuex)

export default new Vuex.Store({
  // state: {
  // },
  // getters: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  modules: { accounts, communities, home
  }
})
