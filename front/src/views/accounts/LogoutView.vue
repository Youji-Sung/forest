<template>
  <div>

    <div class="row text-center" style="width: 101%">
      <h1 class="mt-3" style="color: rgb(0, 117, 149);">안녕!</h1>
    </div>

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        alert('잘못된 접근')
        this.$router.back()
      }
    },
  }
</script>

<style></style>