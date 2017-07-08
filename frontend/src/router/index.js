import Vue from 'vue'
import Router from 'vue-router'
import Calendar from '@/components/Calendar'
import Login from '@/components/Login'
import EventForm from '@/components/EventForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Calendar',
      component: EventForm
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
