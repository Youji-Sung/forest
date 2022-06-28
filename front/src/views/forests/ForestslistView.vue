<template>
  <div>
    <div class="row">
      <h5>휴~</h5>
      <forest-card
        v-for="forest in forests"
        :key="forest.id"
        :forest="forest"
      ></forest-card>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ForestCard from '@/components/home/ForestCard.vue'

export default {
  name: 'ForestslistView',
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
  created() {
    this.fetchForests()
  }
}
</script>

<style>

</style>