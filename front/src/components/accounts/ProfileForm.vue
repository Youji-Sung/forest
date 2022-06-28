<template>
  <div>
    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex justify-content-center">

        <form @submit.prevent="onSubmit()">

          <p style="color: rgb(0, 117, 149);">nickname</p>
          <input type="text" v-model="newProfile.nickname" id="nickname" required/>
          <!-- <b-input
              v-model="newProfile.nickname"
              placeholder="닉네임을 입력해 주세요."
              type="text"
              id="nickname"></b-input> -->

          <p class="mt-4" style="color: rgb(0, 117, 149);">생년월일</p>
          <input type="date" v-model="newProfile.date_of_birth" id="date_of_birth" required/>
          <!-- <b-input
              v-model="newProfile.date_of_birth"
              placeholder="내용을 입력해 주세요"
              rows="3"
              max-rows="6"
              type="date"
              id="date_of_birth"></b-input> -->

          <br>
          <br>

          <label for="chooseFile" class="mt-4 mb-2" style="color: rgb(0, 117, 149);">프로필 이미지</label> <br>
          <input ref="serveyImage" type="file" id="profile_image" class="mb-5">
          
          <br>
          <br>
          
          <button class="btn btn-outline-info" style="color: rgb(0, 117, 149);">{{ action }}</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ProfileForm',
  props: {
    profile: Object,
    action: String,
  },
  data () {
    return {
      newProfile: {
        username: this.profile.username,
        profile_image: this.profile.profile_image, // 수정가능
        nickname: this.profile.nickname, // 수정가능
        // email: this.profile.email,
        date_of_birth: this.profile.date_of_birth, // 수정가능
      }
    }
  },

  methods: {
    ...mapActions(['updateProfile']),
    onSubmit() {
      // const profile_image = document.querySelector('#profile_image').files[0]
      // const payload = new FormData()
      // payload.append('username', this.$route.params.username)
      // payload.append('profile_image', profile_image)
      // payload.append('nickname', this.newProfile.nickname)
      // payload.append('date_of_birth', this.newProfile.date_of_birth)

      // this.updateProfile(payload)
      console.log(this.newProfile)
      this. updateProfile(this.newProfile)

      // this.updateProfile({ username: this.profile.username, 
      // profile_image: this.newProfile.profile_image, 
      // nickname: this.newProfile.nickname, 
      // date_of_birth: this.newProfile.date_of_birth})
    }
  }

}
</script>

<style>

</style>