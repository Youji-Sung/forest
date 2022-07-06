<template>
    <div id="map"></div>
</template>

<script>
export default {
  data(){
    return {};
  },
  mounted() {
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
  computed:{
    lat(){
      return this.$store.state.forests.forest.latitude
    },
    lon(){
      return this.$store.state.forests.forest.longitude
    }
  },
  methods: {
    
    initMap() {
      setTimeout(() => {console.log("첫 번째 메시지")}, 5000);
      var mapContainer = document.getElementById('map'), // 지도를 표시할 div
          mapOption = {
            center: new kakao.maps.LatLng(this.lat, this.lon), // 지도의 중심좌표
            level: 8, // 지도의 확대 레벨
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
    },
    created() {
      this.initMap()
    }
  },
};
</script>

<style>
#map {
    width: 20vh;
    height: 30rem;
}
</style>