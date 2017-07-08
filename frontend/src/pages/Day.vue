<template>
  <div>
    <day :year="year" :month="month" :day="day"></day>
  </div>
</template>

<script>
import Day from '../components/Day.vue'
export default {
  data () {
    return {
      year: '2015',
      month: '3',
      day: '23'
    }
  },
  components: {
    'day': Day
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
