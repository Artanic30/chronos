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
    Year: '',
    Month: '',
    Day: '',
    LastView: ''
  },
  mutations: {
    Authenticate (state, If) {
      state.Authenticated = If
    },
    ApplyToken (state, Token) {
      state.Token = Token
    },
    ChangeView (state, view) {
      state.LastView = view
    },
    UpdateTime (state, Year, Month, Day) {
      state.Year = Year
      state.Month = Month
      state.Day = Day
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
