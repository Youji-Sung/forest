<template>
  <div>
    <div class="row text-center" style="width: 102%">
      <h1 class="my-3 mb-4" >수정하기</h1>
      <profile-form v-if="isProfile" :profile="profile" action="update"></profile-form>
    </div>
  </div>
</template>

<script>
import ProfileForm from '@/components/accounts/ProfileForm.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ProfileEdit',
  components: { ProfileForm },
  computed: {
    ...mapGetters(['profile', 'isProfile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    // this.fetchProfile(this.$route.params.username) // 이걸 사용해서 하니까 안됐다. 아래로 바꾸니까 된다. 왜일까!
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>