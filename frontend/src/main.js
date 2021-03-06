// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.use(Vuex)

const UserVuexStore = new Vuex.Store({
  state: {
    UserName: '',
    Token: '',
    Authenticated: null,
    Year: new Date().getYear() + 1900,
    Month: new Date().getMonth(),
    Day: new Date().getDate(),
    LastView: '',
    NowView: ''
  },
  mutations: {
    Authenticate (state, If) {
      state.Authenticated = If
    },
    ApplyToken (state, Token) {
      state.Token = Token
    },
    ApplyLastView (state, view) {
      state.LastView = view
    },
    UpdateYear (state, Year) {
      state.Year = Year
    },
    UpdateMonth (state, Month) {
      state.Month = Month
    },
    UpdateDay (state, Day) {
      state.Day = Day
    },
    ApplyNowView (state, view) {
      state.NowView = view
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
