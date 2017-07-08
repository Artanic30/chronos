<template>
  <div>
    <strong v-for="dayIndex in week">{{ dayIndex }}</strong>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        week: [
          '星期日',
          '星期一',
          '星期二',
          '星期三',
          '星期四',
          '星期五',
          '星期六'
        ],
        demoEvents: [{
          date: '2016/12/15',
          title: 'Foo',
          desc: 'longlonglong description'
        },
        {
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
