<template>
  <div>
    <div class="row text-center" style="width: 101% color: rgb(0, 117, 149);">
      <h1 class="mt-3">회원가입</h1>
      <account-error-list v-if="authError"></account-error-list>
    </div>

    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex justify-content-center">
        <form @submit.prevent="signup(credentials)">
          <div>
            <label for="username" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">아이디 </label>
            <input  v-model="credentials.username" type="text" id="username" required/>
          </div>
          <div>
            <label for="password1" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">비밀번호 </label>
            <input v-model="credentials.password1" type="password" id="password1" required />
          </div>
          <div>
            <label for="password2" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">비밀번호 확인</label>
            <input v-model="credentials.password2" type="password" id="password2" required />
          </div>
          <div>
            <label for="nickname" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">닉네임 </label>
            <input  v-model="credentials.nickname" type="text" id="nickname" required/>
          </div>
          <!-- <div>
            <label for="first_name" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">이름</label>
            <input v-model="credentials.first_name" type="text" id="first_name" required />
          </div>
          <div>
            <label for="last_name" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">성</label>
            <input v-model="credentials.last_name" type="text" id="last_name" required />
          </div> -->
          <div>
            <label for="email">email:</label>
            <input v-model="credentials.email" type="email" id="email" required />
          </div>
          <!-- <div>
            <label for="profile_image">profile image: </label>
            <input ref="profile_image" @change="uploadImg()" type="file" accept="image/*" id="profile_image" name="profile_image" />
          </div> -->
          <div>
            <label for="date">date_of_birth: </label>
            <input  v-model="credentials.date_of_birth" type="date" id="date_of_birth" />
          </div>
          <div class="d-flex justify-content-center mt-3">
            <button class="btn btn-outline-info" style="color: rgb(0, 117, 149);">Signup</button>
          </div>
        </form>
      </div>
    </div>

    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/accounts/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          nickname: '',
          password1: '',
          password2: '',
          email: '',
          date_of_birth: '',
        },
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup']),
      // uploadImg() {
      //   console.log('이미지 처리중')
      //   // console.log(file)
      //   // this.profile_image = file
      //   // const profile_image = document.querySelector("#profile_image").files[0]
      //   this.credentials.profile_image = profile_image

      //   const profile_image = this.$refs.selectFile.files[0]
      //   let fileExt = this.selectFile.name.substring(
      //     this.selectFile.name.lastIndexOf(".") + 1
      //   )
      //   fileExt = fileExt.toLowerCase()

      //   if (
      //       ["jpeg", "png", "gif", "bmp"].includes(fileExt) &&
      //       this.selectFile.size <= 1048576
      //     ) {
      //       const reader = new FileReader()
      //   reader.onload = e => {
      //     this.credentials.profile_image = e.target.result
      //   }
      //   reader.readAsDataURL(this.selectFile)
      //   }

        

        // console.log(this.$refs['profile_image'].files[0])
        // const profile_image = this.$refs['profile_image'].files[0]

        // const url = URL.createObjectURL(profile_image)
        // this.profile_image = url
        // console.log(url)
        // console.log(this.profile_image)
        // console.log('된건가?')
      // },
    },
  }
</script>

<style>
</style>