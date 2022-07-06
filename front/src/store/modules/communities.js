import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    articles: [],
    article: [],
  },
  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isArticleAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
  },
  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.article_comments = comments),
  },
  actions: {
    // state의 articles 만들기
    fetchArticles({ commit, getters }) { 
      axios({
        url: drf.community.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err.response))
    },

    // state의 article 만들기
    fetchArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.community.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    // article에 새로운 글 쓰기
    createArticle({ commit, getters }, article) {
      axios({
        url: drf.community.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res=> {
          commit('SET_ARTICLE', res.data)
          router.push({ // object로 전달한다는 뜻
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    updateArticle({ commit, getters}, { articlePk, title, content, article_image}) {
      axios({
        url: drf.community.article(articlePk),
        method: 'put',
        data: { title, content, article_image },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    // article 게시글 삭제
    deleteArticle({ commit, getters }, articlePk) {
      if (confirm('게시글을 삭제하시겠습니까?')) {
        axios({
          url: drf.community.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articles'})
          })
          .catch(err => console.error(err.response))
      }
    },

    // 댓글 생성
    createArticleComment({ commit, getters }, {articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.community.articleComments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    // 댓글 수정
    updateArticleComment({ commit, getters }, { articlePk, articleCommentPk, content }) { 
      const comment = { content }

      axios({
        url: drf.community.articleComment(articlePk, articleCommentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    // 댓글 삭제
    deleteArticleComment({ commit, getters }, { articlePk, articleCommentPk }) {
      if (confirm('댓글을 삭제하시겠습니까?')) {
        axios({
          url: drf.community.articleComment(articlePk, articleCommentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    },
  },
}

