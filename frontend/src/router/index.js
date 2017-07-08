import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Day from '@/pages/Day'
import EventForm from '@/components/EventForm'
import Calendar from '@/components/Calendar'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '',
      component: Calendar
    },
    {
      path: '/add',
      name: 'EventForm',
      component: EventForm
    },
    {
      path: '/day/:year/:month/:day',
      name: 'Day',
      component: Day
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
