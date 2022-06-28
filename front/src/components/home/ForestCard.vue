<template>
  <div>
    <!-- <h5>{{ forest.name }}</h5> -->
    <!-- <p>{{ forest.pk }}</p> -->
    <p>{{ forest }}</p>
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