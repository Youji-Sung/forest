<template>
  <div>
    <h3>휴양림 개요</h3>
    <div>
      <!-- 휴양림 이미지 -->
      {{ $store.state.forests.forest}}
      {{ $store.state.forests.forest.image }}
      <img v-bind:src="imgUrl" alt="">
      {{imgUrl}}
    </div>
    <div>
      <weather-inf></weather-inf>
    </div>
    <div>
      <map-inf></map-inf>
    </div>
  </div>
</template>

<script>

import MapInf from './MapInf.vue'
import WeatherInf from './WeatherInf.vue'

export default {
  name: 'DetailSummary',
  
  components:{
    MapInf,
    WeatherInf,
  },
  computed: {
    imgUrl(){
      return `http://127.0.0.1:8000${this.$store.state.forests.forest.image}`
    },
  },
}
</script>

<style>

</style>