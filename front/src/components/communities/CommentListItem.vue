<template>
  <div>
    <li>
      <router-link :to="{ name: 'profile', params: { username: articleComment.user.username } }">
        {{ articleComment.user.username }}
      </router-link>

      <span v-if="!isEditing">{{ payload.content }}</span>

      <span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button variant="outline-info" @click="onUpdate">업데이트</button> 
        <button variant="outline-info" @click="switchIsEditing">취소</button>
      </span>
      
      <span v-if="currentUser.username === freeComment.user.username && !isEditing">
        <button variant="outline-info" @click="switchIsEditing">수정</button> 
        <button variant="outline-info" @click="deleteFreeComment(payload)">삭제</button>
      </span>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { articleComment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.articleComment.article,
        articleCommentPk: this.articleComment.pk, // pk일까 id일까
        content: this.articleComment.content
      }
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    ...mapActions(['updateArticleComment', 'deleteArticleComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateArticleComment(this.payload)
      this.isEditing = false
    }
  }
}
</script>

<style>

</style>