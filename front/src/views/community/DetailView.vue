<template>
  <div>
    <h1>여것은 휴양림 메인 페이지야.</h1>
    <detail-board></detail-board>
    <detail-summary></detail-summary>

  </div>
</template>


<script>

import DetailBoard from './DetailBoard.vue'
import DetailSummary from './DetailSummary.vue'

import {mapGetters, mapActions} from 'vuex'

export default {

  name: 'DetailView',
  components:{
    DetailBoard,
    DetailSummary,
  },
  computed:{
    ...mapGetters([])
  },
  methods:{
    ...mapActions([])
  },
  created() {
    const payload = {forest_id: this.$route.params.forest_id}
    this.fetchDetail(payload)
    },
}
</script>

<style>

</style>