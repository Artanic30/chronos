// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
<<<<<<< HEAD
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)
=======
import 'vue-event-calendar/dist/style.css'
import vueEventCalendar from 'vue-event-calendar'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)
Vue.use(vueEventCalendar, {locale: 'zh'})
>>>>>>> ncj
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
