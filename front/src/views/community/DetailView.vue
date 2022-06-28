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

export default {
  name: 'DetailView',
  components:{
    DetailBoard,
    DetailSummary,
  },


}
</script>

<style>

</style>