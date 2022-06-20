<template>
  <div>

    <div class="row text-center" style="width: 101% color: rgb(0, 117, 149);">
      <h1 class="mt-3">로그인</h1>
      <account-error-list v-if="authError"></account-error-list>
    </div>

    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex justify-content-center">
        <form @submit.prevent="login(credentials)">

          <div>
            <label for="username" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">아이디 </label>
            <input v-model="credentials.username" type="text" id="username" required />
          </div>

          <div>
            <label for="password" class="d-flex justify-content-center mt-3" style="color: rgb(0, 117, 149);">비밀번호 </label>
            <input v-model="credentials.password" type="password" id="password" required />
          </div>
          
          <div class="d-flex justify-content-center mt-3">
            <button class="btn btn-outline-info" style="color: rgb(0, 117, 149);">Login</button>
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
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style></style>