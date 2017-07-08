<template>
  <div>
    <full-calender :events="fcEvents"></full-calender>
  </div>
</template>

<script>
import calendar from '../../self_modules/vue-fullcalendar/src/fullCalendar.vue'
export default {
  name: 'hello',
  data () {
    return {
      fcEvents: [
        {
          title: 'Sunny Out of Office',
          start: '2017-07-15',
          end: '2017-07-27'
        }
      ]
    }
  },
  components: {
    'full-calender': calendar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
