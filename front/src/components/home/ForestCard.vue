<template>
  <div>
    <h5>휴양림 정보</h5>
    <p>{{ cardName }}</p>
  </div>
</template>

<script>
export default {
  name: 'ForestCard',
  props: {
    card: {
      type: Object
    }
  },
  computed: {
    cardContext: function() {
      const context = this.card.fields
      return context
    },
  }
}
</script>

<style>

</style>