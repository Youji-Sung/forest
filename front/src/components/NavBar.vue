<template>
  <nav class="navbar navbar-expand-sm navbar-light bg-white">
    <div class="collapse navbar-collapse m-3">
      <router-link to="/" class="navbar-brand">
        <img src="../assets/forests.jpg" alt="logo" class="logo" style="height:80px;" />
      </router-link>
      <ul class="navbar-nav">
        <!-- <li class="nav-item m-md-3">
          <router-link :to="{ name: 'home' }" class="nav-link" style="color: gray;">홈</router-link>
        </li> -->
        <li class="nav-item m-md-3" >
          <router-link :to="{ name: 'forests' }" class="nav-link" style="color: gray;">휴양림</router-link>
        </li>
        <li class="nav-item m-md-3" >
          <router-link :to="{ name: 'articles' }" class="nav-link" style="color: gray;">커뮤니티</router-link>
        </li>
        <li class="nav-item m-md-3">
          <router-link v-if="isLoggedIn" :to="{ name: 'logout' }" class="nav-link " style="color: gray;">Logout</router-link>
        </li>
        <li class="nav-item m-md-3">
          <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: { username } }" class="nav-link">
          {{ currentUser.username }}님의 프로필</router-link>
        </li>
        <li class="nav-item m-md-3">
          <router-link v-if="!isLoggedIn" :to="{ name: 'login' }" class="nav-link" style="color: gray;">Login</router-link>
        </li>
        <li class="nav-item m-md-3">
          <router-link v-if="!isLoggedIn" :to="{ name: 'signup' }" class="nav-link" style="color: gray;">Signup</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username: 'guest'
      }

  }
}
</script>

<style>
header {
  width: 80%;      
  margin: 0 auto;   
  padding: 1rem 0; 
}

.profile {
    height:60px;
    width:60px;
    object-fit: cover;
    border-radius: 100%;
}
</style>