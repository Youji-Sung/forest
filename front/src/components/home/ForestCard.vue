<template>
  <div>
    <b-card class="con-com-02">
      <h4 class="mt-3" style="color: rgb(0, 128, 0);">{{ forest.id }}</h4>
      <b-card-text>
        <h5 style="color: rgb(0, 128, 0);">이름</h5>
        <p>{{ forest.name }}</p>
        <h5 style="color: rgb(0, 128, 0);">주소</h5>
        {{ forest.address }}
        <h5 style="color: rgb(0, 128, 0);">연락처</h5>
        {{ forest.address }}
        <router-link to="/:forest_id">[ 디테일 ]</router-link>
      </b-card-text>
    </b-card> |
    <b>forest 속성들</b>
    <p>{{ forest.name }} {{ forest.possession}} {{ forest.facility }} {{ forest.address }} {{ forest.phone }} {{ forest.image }} {{ forest.latitude }} {{ forest.longitude }} {{ forest.like }} {{ forest.stamp }} </p>
  </div>
</template>

<script>
export default {
  name: 'ForestCard',
  props: {
    forest: Object,
  },
}
</script>

<style>

</style>