<template>
  <div>
    <div v-for="Hour in HourList">
      <hour :Hour="Hour"></hour>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Hour from './Hour.vue'
export default {
  data () {
    return {
      HourList: [
        {
          time: 0,
          events: [
            {
              title: 'Take a bath'
            }
          ]
        },
        {
          time: 1
        }
      ],
      Year: this.$route.params.year,
      Month: this.$route.params.month,
      Day: this.$route.params.day
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
        Year: this.Year,
        Month: this.Month,
        Day: this.Day
      })
    }).then(function (response) {
      if (response.data.message === 'success') {
        this.HourList = JSON.parse(response.data.data)
        console.log('success')
      } else {
        console.log('error')
      }
    }.bind(this))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
