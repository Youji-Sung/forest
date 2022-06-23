<template>
  <div>
    <h5>휴양림리스트</h5>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ForestsListView',
  methods: {
    ...mapActions(['fetchForests'])
  },
}
</script>

<style>

</style>