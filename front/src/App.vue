<template>
  <div id="app">
    <nav-bar></nav-bar>
    <forest-card></forest-card>
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ForestCard from '@/components/home/ForestCard.vue'

  export default {
    name: 'App',
    components: { NavBar, ForestCard },
    methods: {
    fetchForests () {
      this.$store.dispatch('fetchForests')
    },
  },
  created () {
    this.fetchForests()
  },
  }
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>


<!-- <template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view/>
    <detail-view></detail-view>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import DetailView from '@/views/community/DetailView.vue'
  export default {
    name: 'App',
    components: { NavBar, DetailView }
  }
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style> -->
