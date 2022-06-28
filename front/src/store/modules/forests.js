import axios from 'axios'
import drf from '@/api/drf'

export default ({
  state: {
    forests: [],
  },
  getters: {
    forests: state => state.forests
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
        url: drf.forests.forestsList(),
      })
      .then(res => {
        console.log('1')
        commit('FETCH_FORESTS', res.data)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {},
})
