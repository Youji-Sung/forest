<template>
  <div>
    <!-- <h1> {{ $store.state.forests.forest.id }}번 휴양림의 DetailView부분 </h1>
    <h2> 이름 : {{ $store.state.forests.forest.name }} </h2>
    {{ $store.state.forests.forest.image }}
    <h1> {{ $store.state }} </h1> -->
    {{ $store.state.forests.forest }}
    <!-- <h1>{{ forest_images }}</h1> -->
    <!-- <img :src="forest_images" alt="">    -->
    <!-- <img :src="forest_images"> -->
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
    forest () {
      return this.$store.state.forests.forest
    },
    forest_images () {
      let imgs = this.$store.state.forests.forest.image
      return imgs.slice(1,imgs.length-1).split(',')[0].replaceAll('\'','')
      
    }
  },
  methods:{
    ...mapActions(['fetchDetail']),

  },
  created() {
    const payload = {forest_id: this.$route.params.forest_id}
    this.fetchDetail(payload)
  },
}
</script>

<style>

</style>