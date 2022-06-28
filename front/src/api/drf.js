const HOST = 'http://localhost:8000/api/v1/'

const FORESTS = 'forests/'
const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'

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
  community: {
    detail: () => HOST + COMMUNITY,
  }
}