<template>
  <div>
    <form @submit.prevent="onSubmit">
      <input type="text" id="comment" v-model="content" required>
      <button type="submit">댓글 달기</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article'])
  },
  methods: {
    ...mapActions(['createArticleComment']),
    onSubmit() {
      // pk일까 id일까
      this.createArticleComment({ articlePk: this.article.pk, content: this.content })
      this.content = ''
    }
  }
}
</script>

<style>

</style>