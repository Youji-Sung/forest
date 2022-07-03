const HOST = 'http://localhost:8000/api/v1/'

const FORESTS = 'forests/'
const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const REVIEW = 'review/'

export default {
  forests: {
    forestsList: () => HOST + FORESTS,
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
    community: (forestId, communityPk) => HOST + FORESTS + `${forestId}/` + COMMUNITY + `${communityPk}`
  },
  forestreview: {
    reviews: forestId => HOST + FORESTS + `${forestId}/` + REVIEW,
    review: (forestId, reviewPk) => HOST + FORESTS + `${forestId}/` + REVIEW + `${reviewPk}`
  }
}