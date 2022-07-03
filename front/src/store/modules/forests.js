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
    },
    fetchDetail({commit},{forest_id}){
      axios({
        method: 'get',
        url: drf.forests.forestDetail(forest_id),
      })
      .then(res =>{
        console.log(res.data)
        console.log('test_choi')
        commit('FETCH_DETAIL', res.data)
      })
    }
  },
  modules: {},
})
