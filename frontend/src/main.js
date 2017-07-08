// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from 'vuex'
import '../node_modules/bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false
Vue.use(Vuex)

const UserVuexStore = new Vuex.Store({
  state: {
    UserName: '',
    Token: '',
    Authenticated: null
  },
  mutations: {
    Authenticate (state, If) {
      state.Authenticated = If
    },
    ApplyToken (state, Token) {
      state.Token = Token
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: UserVuexStore,
  template: '<App/>',
  components: { App }
})
