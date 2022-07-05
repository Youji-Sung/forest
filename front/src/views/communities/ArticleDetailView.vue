<template>
  <div>
    <!-- 정보 확인 -->
    {{ article.user.username }}
    {{ article.title }}
    {{ article.content }}
    <div class="d-flex justify-content-center mx-5 mb-5">
      <div class="d-flex box justify-content-center">
        <img :src="imgUrl" alt="article_image">
      </div>
    </div>

    <div v-if="isArticleAuthor">
      <!-- 수정하기 -->
      <router-link :to="{ name: 'articleEdit', params: {articlePk} }">
        <button>수정하기</button>
      </router-link>
      <!-- 삭제하기 -->
      <button @click="deleteArticle(articlePk)">삭제하기</button>
    </div>

    <!-- 댓글 -->
    <article-comment-list :articleComments="article.comments"></article-comment-list>


  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '@/components/communities/CommentList.vue'

export default {
  name: 'ArticleDetail',
  components: { CommentList },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed: {
    ...mapGetters(['isArticleAuthor', 'article']),
    imgUrl(){
      return `http://127.0.0.1:8000${this.article.article_image}`
    }
  },
  methods: {
    ...mapActions([
      'fetchArticle',
      'deleteArticle',
    ])
  },
  created() {
    this.fetchArticle(this.articlePk)
  }
}
</script>

<style>

</style>