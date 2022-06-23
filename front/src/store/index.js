import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import accounts from './modules/accounts'
import communities from './modules/communities'
// import home from './modules/home'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    forests: [],
  },
  getters: {
  },
  mutations: {
    FETCH_FORESTS (state, forests) {
      state.forests = forests
      }
    },
  actions: {
    fetchForests ({ commit }) {
      axios({
        method: 'get',
        url: 
      })
      .then(res => {
        commit('FETCH_FORESTS', res.data.results)
      })
      .catch(err => console.log(err))
    }
  },
  modules: { accounts, communities
  }
})
