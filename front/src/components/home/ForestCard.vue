<template>
  <div>
    <!-- <h5>{{ forest.name }}</h5> -->
    <!-- <p>{{ forest.pk }}</p> -->
    {{ forest.id }}
    {{ forest.name }}
  </div>
</template>

<script>
export default {
  name: 'ForestCard',
  props: {
    forest: Object,
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