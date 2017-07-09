<template>
  <div class="container">
    <div class="col-md-6">
    <div v-for="Hour in HourList" class="list-group day-event" >
      <hour :Hour="Hour"></hour>
    </div>
    </div>
    <div class="col-md-6">
      <ol class="event">
        <li>刷牙</li>
        <li>洗脸</li>
        <li>吃早饭</li>
      </ol>
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
            time: 0,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 1,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 2,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 3,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 4,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 5,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 6,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 7,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 8,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 9,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 10,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 11,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 12,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 13,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 14,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 15,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 16,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 17,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 18,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 19,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 20,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 21,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 22,
            events: [
              {
                title: 'Code!'
              }
            ]
          },
          {
            time: 23,
            events: [
              {
                title: 'Code!'
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
  .day-event {
    text-align: center;
  }
  .event {
    font-size: 30px;
  }
</style>
