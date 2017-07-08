import Vue from 'vue'
import Router from 'vue-router'
import Calendar from '@/pages/Calendar'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Calendar',
      component: Calendar
    },
    {
      path: '/day',
      name: 'Day',
      component: Calendar
    }
  ]
})
