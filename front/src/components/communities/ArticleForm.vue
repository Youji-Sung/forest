<template>
  <div>
    <form @submit.prevent="onSubmit">
      <p>title</p>
      <input v-model="newArticle.title" type="text" id="title">
      <p>content</p>
      <input v-model="newArticle.content" type="text" id="content">
      <label for="chooseFile">이미지 첨부 </label>
        <input ref="serveyImage" type="file" id="article_image">
      <button>{{ action }}</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ArticleForm',
  props: {
    article: Object,
    action: String,
  },
  data() {
    return {
      newArticle: {
        title: this.article.title,
        content: this.article.content,
        article_image: this.article.article_image,
      }
    }
  },
  
  methods: {
    ...mapActions(['createArticle', 'updateArticle']),
    onSubmit() {
      const image = document.querySelector('#article_image').files[0]
      const payload = new FormData()
      payload.append('article_image', image)
      payload.append('content', this.newArticle.content)
      payload.append('title', this.newArticle.title)

      if (this.action === 'create') {
        this.createArticle(payload)
      } else if (this.action === 'update') {
        this.updateArticle({ articlePk: this.article.id, 
        // pk일까 id일까?
        content: this.newArticle.content,
        title: this.newArticle.title,
        article_image: this.newArticle.article_image})
      }
    }
  }
}
</script>

<style>

</style>