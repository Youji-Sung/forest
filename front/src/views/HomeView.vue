<template>
  <div class="home">
    <div class="row">
      <forest-card
        class="col-2 col-md-3"
        v-for="forest in forests.forests"
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
