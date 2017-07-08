<template>
  <div>
    <day></day>
    <router-link :to="{ name: 'Day', params:{ year:'2017',month:'7',day:'8'}}">shit</router-link>
  </div>
</template>

<script>
import Day from '../components/Day.vue'
export default {
  data () {
    return {
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
