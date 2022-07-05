<template>
  <div>
    <b-card class="col mb-3">
      <h4 class="mt-3" style="color: rgb(0, 128, 0);">{{ forest.id }}</h4>
      <img src="https://image.foresttrip.go.kr/ino/tour/f1917803-8713-43a8-acde-6fac6f07a7ca.jpg" alt="공산성">
      <img src="https%3A/image.foresttrip.go.kr/ino/instt/0eff7add-0131-4a9a-bc3f-e9e062e9d4a7.png" alt="test">
      <v-card-text>
        <h5 style="color: rgb(0, 128, 0);">이름</h5>
        <p>{{ forest.name }}</p>
        <h5 style="color: rgb(0, 128, 0);">소유 형태</h5>
        {{ forest.possession }}
        <h5 style="color: rgb(0, 128, 0);">시설물</h5>
        {{ forest.facility }}
        <h5 style="color: rgb(0, 128, 0);">주소</h5>
        {{ forest.address }}
        <h5 style="color: rgb(0, 128, 0);">연락처</h5>
        {{ forest.phone }}
        <h5 style="color: rgb(0, 128, 0);">위도 | 경도</h5>
        {{ forest.latitude }} | {{ forest.longitude }}
        <b>좋아요{{ forest.like }} 도장{{ forest.stamp}}</b>
        <b>{{ forest.image }}</b>
        <router-link :to="{ name : 'detail', params : { 'forest_id' : forest.id } }">[ 디테일 ]</router-link>
      </v-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'ForestCard',
  props: {
    forest: Object,
  },
}
</script>

<style>
.overflow {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4; 
  -webkit-box-orient: vertical;
}
</style>