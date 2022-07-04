<template>
  <div>
    <h1> {{ $store.state.forests.forest.id }}번 휴양림의 DetailView부분 </h1>
    <h2> 이름 : {{ $store.state.forests.forest.name }} </h2>
    <detail-board></detail-board>
    <detail-summary></detail-summary>

  </div>
</template>


<script>

import DetailBoard from './DetailBoard.vue'
import DetailSummary from './DetailSummary.vue'

import { mapActions } from 'vuex'

export default {

  name: 'DetailView',
  components:{
    DetailBoard,
    DetailSummary,
  },
  computed:{
    
  },
  methods:{
    ...mapActions(['fetchDetail'])
  },
  created() {
    const payload = {forest_id: this.$route.params.forest_id}
    this.fetchDetail(payload)
  },
}
</script>

<style>

</style>