import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import communities from './modules/communities'
import home from './modules/home'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // forests: [],
    cards: [],
  },
  getters: {
  },
  mutations: {
    GET_FORESTS: function (state, data) {
      state.cards = data
    }
  },
  actions: {
    getForests ({ commit }) {
      axios({
        method: 'get',
      })
      .then(res => {
        commit('GET_FORESTS', res.data.resulsts)
      })
      .catch(err => console.log(err))
    }
  },
  modules: { accounts, communities, home
  }
})
