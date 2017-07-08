<template>
  <div class="container">
    <el-row :gutter="20" class="tac">
      <el-col :span="leftWidth" :offset="2">
        <el-row class="main">
          <el-col :span="3" v-for="index in week" class="card" :key="index">{{ index }}</el-col>
        </el-row>
        <el-row class="main" v-for="weekIndex in month" :key="weekIndex">
          <el-col :span="3" v-for="dayIndex in weekIndex" :key="dayIndex">
            <div class="card" @click="editOrBrowse">{{ dayIndex }}</div>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="rightWidth" v-if="state === 'edit' ">
        <event-form></event-form>
      </el-col>
    </el-row>
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
          ['', '1', '2', '3', '4', '5', '6'],
          ['7', '8']
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
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card {
    background-color: #72f1ff;
    border: 1px solid #fff;
    height: 150px;
  }
</style>
