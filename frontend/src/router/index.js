import Vue from 'vue'
import Router from 'vue-router'
<<<<<<< HEAD
// import Test from '@/components/EventForm'
import Calendar from '@/pages/Calendar'
import Login from '@/components/Login'
import Day from '@/pages/Day'
=======
import Calendar from '@/components/Calendar'
import Login from '@/components/Login'
import EventForm from '@/components/EventForm'
>>>>>>> ncj

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Calendar',
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
