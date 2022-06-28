<template>
  <div>
    <h5>{{ forest.name }}</h5>
    <p>{{ forest.id }}</p>
  </div>
</template>

<script>
export default {
  name: 'ForestCard',
  props: {
    forest: Array,
  },
  // computed: {
  //   cardContext: function() {
  //     const context = this.card.fields
  //     return context
  //   },
  // }
}
</script>

<style>

</style>