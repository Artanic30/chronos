<template>
  <div>
    <h1>{{ GetYear }}年</h1>
    <h1>{{ GetMonth }}月</h1>
    <h1>{{ GetDay }}日</h1>
    <div v-for="Hour in HourList">
      <hour :Hour="Hour"></hour>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Hour from './Hour.vue'
export default {
  props: {
    year: {},
    month: {},
    day: {}
  },
  data () {
    return {
      HourList: [
        {
          events: [
            {
              title: 'Take a bath'
            }
          ]
        }
      ],
      Year: this.GetYear,
      Month: this.GetMonth,
      Day: this.GetDay
    }
  },
  components: {
    'hour': Hour
  },
  computed: {
    Authenticate () {
      return this.$store.state.Authenticated
    },
    GetUserName () {
      return this.$store.state.UserName
    },
    GetToken () {
      return this.$store.state.Token
    },
    GetYear () {
      return this.$props.year
    },
    GetMonth () {
      return this.$props.month
    },
    GetDay () {
      return this.$props.day
    }
  },
  mounted: function () {
    axios({
      method: 'POST',
      url: '',
      // TODO: api
      data: JSON.stringify({
        Token: this.GetToken,
        UserName: this.GetUserName,
        Year: this.GetYear,
        Month: this.GetMonth,
        Day: this.GetDay
      })
    }).then(function (response) {
      if (response.data.message === 'success') {
        this.HourList = JSON.parse(response.data.data)
      } else {
        this.$notify.error({
          'title': '错误',
          'message': '获取数据失败'
        })
      }
    }.bind(this))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
