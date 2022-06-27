<template>
  <nav>
    NavBar 자리 입니다
    <router-link to="/">홈</router-link> |
    <router-link to="/login">로그인</router-link> |
    <router-link to="/profile/:username">프로필</router-link> |
    <router-link to="/forests">휴양림</router-link>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style>

</style>