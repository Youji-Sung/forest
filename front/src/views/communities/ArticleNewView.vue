<template>
  <div>
    <h1>새 글 쓰기</h1>
    <article-form :article="article" action='create'>
    </article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'

export default {
  name: 'ArticleNew',
  components: { ArticleForm },
  data() {
    return {
      article: {
        pk: null,
        title: '',
        content: '',
        article_image: '',
      }
    }
  }
}
</script>

<style>

</style>