<template>
  <div class="container">
    <div class="item">
      <!-- 휴양림 이미지 -->
      <img :src="forest_images">
    </div>
    <div class="item">
      <weather-inf></weather-inf>
    </div>
    <div class="item">
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
    forest_images () {
      let imgs = this.$store.state.forests.forest.image
      return imgs.slice(1,imgs.length-1).split(',')[0].replaceAll('\'','')
      
    }
  },
}
</script>

<style>
  .contaioner{
    display: grid;
    /* grid-template-columns: 1fr 1fr 1fr; */
  }
  /* .item{
    width: auto;
    height: auto;
  } */
  .item img {
    width: 100rem;
    height: 100rem;
  }
</style>