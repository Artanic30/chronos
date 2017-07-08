<template>
  <div>
    <calendar :events="demoEvents"></calendar>
  </div>
</template>

<script>
  import calendar from 'vue-event-calendar'
  export default {
    name: 'hello',
    components: {
      'calendar': calendar
    },
    data () {
      return {
        demoEvents: [{
          date: '2016/12/15',
          title: 'Foo',
          desc: 'longlonglong description'
        }, {
          date: '2016/11/12',
          title: 'Bar'
        }
        ]
      }
    },
    methods: {
      hello () {
        console.log('heelo')
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
