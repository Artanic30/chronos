<template>
  <div>
    <full-calendar></full-calendar>
  </div>
</template>

<script>
import calendar from '../../self_modules/vue-fullcalendar/src/fullCalendar.vue'
export default {
  name: 'hello',
  data () {
    return {
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
