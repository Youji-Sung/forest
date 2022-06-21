<template>
  <div class="home">
    <div class="container">
      <forest-card
        v-for="card in cards"
        :key="card.pk"
        :card="card"
      ></forest-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex'
import ForestCard from '@/components/home/ForestCard.vue'

export default {
  name: 'HomeView',
  components: {
    ForestCard,
  },
  props: {
    cards: {
      type: Array,
    }
  },
  methods: {
    getForests: function() {
      this.$store.dispatch('getForests')
    }
  },
  created: function() {
    this.getForests()
  },
  computed: {
    ...mapState([
      'cards'
    ])
  },
}
</script>
