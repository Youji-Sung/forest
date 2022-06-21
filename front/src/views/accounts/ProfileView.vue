<template>
  <div>
    <div class="row text-center" style="width: 101%">
      <h1 class="my-3 mb-4" >{{ profile.username }}님의 프로필</h1>
      <h5 class="my-3" style="color: rgb(0, 117, 149);">Email address</h5>
      <span class="mb-5">{{ profile.email }}</span>
    </div>

    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex box justify-content-center">
        <img :src="imgUrl" alt="a" class="profile">
      </div>
    </div>

    <div class="d-flex justify-content-center mx-5 mb-5">
      <button type="button" class="btn btn-outline-info" style="color: rgb(0, 117, 149);">수정하기</button>
    </div>

    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex box justify-content-center">
      </div>
    </div>
  </div>
  
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile']),
    imgUrl(){
      // return 값 앞에 장고 서버를 붙여줘야 함/그리고 사이즈 조정
      return `http://127.0.0.1:8000${this.profile.profile_image}`
    }
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
.box {
    width: 300px;
    height: 300px; 
    border-radius: 100%;
    overflow: hidden;
}
.profile {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>