<template>
  <div>
    <router-link :to="{ name: 'articleNew' }">
      <button>새 글 쓰기</button>
    </router-link>

    <ul v-for="article in articles" :key="article.pk">
      <li v-if="article.user">
        {{ article.user.username }}
        <div>
          <router-link :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }}
          </router-link>
        </div>
      </li>
    </ul>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleList',
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>