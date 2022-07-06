const HOST = 'http://localhost:8000/api/v1/'

const FORESTS = 'forests/'
const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const REVIEW = 'review/'
const COMMENTS = 'comments/'

export default {
  forests: {
    forestsList: () => HOST + FORESTS,
    forestDetail: forest_id => HOST + FORESTS + `${forest_id}/`,
  },
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
  },
  forestcommunity: {
    communities: forestId => HOST + FORESTS + `${forestId}/` + COMMUNITY,
    community: (forestId, communityPk) => HOST + FORESTS + `${forestId}/` + COMMUNITY + `${communityPk}/`
  },
  forestreview: {
    reviews: forestId => HOST + FORESTS + `${forestId}/` + REVIEW,
    review: (forestId, reviewPk) => HOST + FORESTS + `${forestId}/` + REVIEW + `${reviewPk}/`
  },
  community: {
    articles: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    articleComments: articlePk => HOST + COMMUNITY + `${articlePk}/` + COMMENTS,
    articleComment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/` + COMMENTS + `${commentPk}/`
  },
}