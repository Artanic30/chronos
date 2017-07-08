import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/components/EventForm'
import Calendar from '@/pages/Calendar'
import Login from '@/components/Login'

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
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
