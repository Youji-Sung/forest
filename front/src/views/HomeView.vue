<template>
  <div class="home">
    <div class="container">
      <forest-card
        v-for="forest in forests"
        :key="forest.id"
        :forest="forest"
      ></forest-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState, mapActions } from 'vuex'
import ForestCard from '@/components/home/ForestCard.vue'

export default {
  name: 'HomeView',
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
    ])
  },
  created() {
    this.fetchForests()
  },
}
</script>
