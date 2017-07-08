import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/components/EventForm'
import Calendar from '@/pages/Calendar'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/',
      name: 'Calendar',
      component: Calendar
    }
  ]
})
