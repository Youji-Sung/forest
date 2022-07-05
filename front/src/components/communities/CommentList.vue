<template>
  <div>
    <comment-list-item 
    v-for="articleComment in articleComments"
    :articleComment="articleComment"
    :key='articleComment.pk'>
    <!-- pk일까 id일까 -->
    </comment-list-item>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListForm from '@/components/communities/CommentListForm.vue'
import CommentListItem from '@/components/communities/CommentListItem.vue'

export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { articleComments: Array },
}
</script>

<style>

</style>