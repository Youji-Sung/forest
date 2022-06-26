<template>
  <div>
    <h5>휴양림리스트</h5>
    <forest-card
      v-for="forest in forests"
      :key="forest.id"
      :forest="forest"
    >나와라</forest-card>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ForestCard from '@/components/home/ForestCard/vue'

export default {
  name: 'ForestsListView',
  components: {
    ForestCard,
  },
  methods: {
    ...mapActions([
      'fetchForests'
      ])
  },
  computed: {
    ...mapState([
      'forests'
    ]),
  },
}
</script>

<style>

</style>