<template>
  <div>
    <full-calendar :events="Events"></full-calendar>
  </div>
</template>

<script>
import calendar from '../../self_modules/vue-fullcalendar/src/fullCalendar.vue'
export default {
  name: 'hello',
  data () {
    return {
      Events: [
        {
          title: 'shit',
          start: '2017-07-02',
          end: '2017-07-03'
        }
      ]
    }
  },
  components: {
    'full-calendar': calendar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
