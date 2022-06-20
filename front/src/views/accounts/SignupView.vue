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
            <label for="first_name" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">이름</label>
            <input v-model="credentials.first_name" type="text" id="first_name" required />
          </div>
          <div>
            <label for="last_name" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">성</label>
            <input v-model="credentials.last_name" type="text" id="last_name" required />
          </div>
          <div>
            <label for="email">email:</label>
            <input v-model="credentials.email" type="email" id="email" required />
          </div>
          <div>
            <label for="file">profile image: </label>
            <input  ref="serveyImage" type="file" id="profile_image" />
          </div>
          <div>
            <label for="date">date_of_birth: </label>
            <input  ref="serveyImage" type="date" id="date_of_birth" />
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
          first_name: '',
          last_name: '',
          date_of_birth: '',
          email: '',
          profile_image: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
</style>