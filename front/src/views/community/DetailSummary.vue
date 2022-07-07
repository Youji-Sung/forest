<template>
  <div class="container">
    <div class="item">
      <!-- 휴양림 이미지 -->
      <img id="forest_images" :src="forest_images">
    </div>
    <div class="item" style="background-color: azure;">

    </div>
    <div class="item">
      <div id="map"></div>
    </div>
  </div>
</template>

<script>



export default {
  name: 'DetailSummary',
  data(){
    return {};
  },
  beforeUpdate() {
  if (window.kakao && window.kakao.maps) {
    this.initMap();
  } else {
    const script = document.createElement('script');
    /* global kakao */
    script.onload = () => kakao.maps.load(this.initMap);
    script.src =
      'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=e7b6941550fa586e555a7b13cc4f614a';
    document.head.appendChild(script);
  }
},
  computed: {
    imgUrl(){
      return `http://127.0.0.1:8000${this.$store.state.forests.forest.image}`
    },
    forest_images () {
      let imgs = this.$store.state.forests.forest.image
      return imgs.slice(1,imgs.length-1).split(',')[0].replaceAll('\'','')
    },
    lat(){ // 위도
      return this.$store.state.forests.forest.latitude
    },
    lon(){ // 경도
      return this.$store.state.forests.forest.longitude
    },
  },
  methods: {
  
  initMap() {  // 지도 그리는 함수
    setTimeout(() => {console.log("첫 번째 메시지")}, 5000);
    var mapContainer = document.getElementById('map'), // 지도를 표시할 div
        mapOption = {
          center: new kakao.maps.LatLng(this.lat, this.lon), // 지도의 중심좌표
          level: 7, // 지도의 확대 레벨
        };
    var map = new kakao.maps.Map(mapContainer, mapOption);
    var positions = [
      {
        latlng: new kakao.maps.LatLng(this.lat, this.lon),
      },
    ];

    positions.forEach(function(pos) {
      var marker = new kakao.maps.Marker({
        position: pos.latlng, // 마커의 위치
      });
      marker.setMap(map);
    });
  }
},
}
</script>

<style>
  .contaioner{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    /* flex-wrap: wrap; */
    /* align-content: space-around; */
  }
  .item{
    display: inline-block;
    width: 30rem;
    height: 30rem;
    margin: 0%;
  }
  #forest_images {
    display: inline-block;
    width: 100%;
    height: 100%;
  }
  #map {
    display: inline-block;
    width: 30rem;
    height: 30rem;
}
</style>