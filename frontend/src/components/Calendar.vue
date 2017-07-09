<template>
  <div>
    <el-row :gutter="20" class="tac">
      <el-col :span="leftWidth">
        <el-row>
          <el-col :span="3" v-for="index in week" class="card" :key="index">{{ index }}</el-col>
        </el-row>
        <el-row v-for="weekIndex in MonthList" :key="weekIndex">
          <el-col :span="3" v-for="dayIndex in weekIndex" :key="dayIndex">
            <div class="card" @click="editOrBrowse">{{ dayIndex }}</div>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="rightWidth" v-if="state === 'edit' ">
        <event-form></event-form>
      </el-col>
    </el-row>
    <el-button type="primary" @click="prevMonth">上个月</el-button>
    <el-button type="primary" @click="nextMonth">下个月</el-button>
    <h1>{{ typeof Day }}</h1>
  </div>
</template>

<script>
  import EventForm from '@/components/EventForm'
  export default {
    components: {
      'EventForm': EventForm
    },
    data () {
      return {
        leftWidth: 24,
        rightWidth: 10,
        state: 'browse',
        week: [
          '星期日',
          '星期一',
          '星期二',
          '星期三',
          '星期四',
          '星期五',
          '星期六'
        ],
        weekday: [
          'Sun',
          'Mon',
          'Tue',
          'Wed',
          'Thu',
          'Fri',
          'Sat'
        ],
        month: [
          31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
      }
    },
    methods: {
      editOrBrowse () {
        if (this.$data.state === 'edit') {
          this.$data.state = 'browse'
          this.$data.leftWidth = 24
          this.$data.rightWidth = 0
        } else if (this.$data.state === 'browse') {
          this.$data.state = 'edit'
          this.$data.leftWidth = 14
          this.$data.rightWidth = 10
        }
      },
      nextMonth () {
        if (this.Month === 11) {
          this.$store.commit('UpdateYear', this.Year + 1)
          this.$store.commit('UpdateMonth', 0)
        } else {
          this.$store.commit('UpdateMonth', this.Month + 1)
        }
      },
      prevMonth () {
        if (this.Month === 0) {
          this.$store.commit('UpdateYear', this.Year - 1)
          this.$store.commit('UpdateMonth', 11)
        } else {
          this.$store.commit('UpdateMonth', this.Month - 1)
        }
      }
    },
    computed: {
      Year () {
        return this.$store.state.Year
      },
      Month () {
        return this.$store.state.Month
      },
      Day () {
        return this.$store.state.Day
      },
      MonthList () {
        var tmp = []
        var obj = []
        var num = this.month[this.Month]
        var d = new Date()
        d.setFullYear(this.Year, this.Month, 1)
        for (var i = 0; i < d.getDay(); i++) {
          tmp.push('')
          if (tmp.length === 7) {
            obj.push(tmp)
            tmp = []
          }
        }
        for (i = 1; i <= num; i++) {
          tmp.push(i)
          if (tmp.length === 7) {
            obj.push(tmp)
            tmp = []
          }
        }
        if (tmp.length !== 0) {
          obj.push(tmp)
        }
        tmp = []
        return obj
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card {
    background-color: #ff9547;
    border: 1px solid #fff;
    height: 150px;
  }
</style>
