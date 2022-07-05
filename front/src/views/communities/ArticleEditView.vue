<template>
  <div>
    <article-form v-if="isArticle" :article="article" action="update">
      <button>수정하기</button>
    </article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'ArticleEdit',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['article', 'isArticle'])
  },
  methods: {
    ...mapActions(['fetchArticle'])
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>

</style>