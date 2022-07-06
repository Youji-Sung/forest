<template>
  <div>
    <b-card class="col mb-3">
      <h4 class="mt-3" style="color: rgb(0, 128, 0);">{{ forest.id }}</h4>
      <img :src="forestImgURL" alt="휴양림 사진" img-left class="mb-3" style="height: 200px; width: 350px">
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
        <div>
          좋아요{{ forest.like }} 도장{{ forest.stamp}}
        </div>
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
  computed: {
    forestImgURL() {
      var imageUrl = `${this.forest.image}`
      var slicedUrl = imageUrl.slice(2, -2)
      return slicedUrl
    }
  }
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