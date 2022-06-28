<template>
  <div>
    <h3>휴양림 개요</h3>
    <div>
      <!-- 휴양림 이미지 -->
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
}
</script>

<style>

</style>