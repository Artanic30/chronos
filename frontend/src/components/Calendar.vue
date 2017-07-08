<template>
  <div class="container">
    <el-row class="main">
      <el-col :span="3" v-for="index in week" class="card">{{ index }}</el-col>
    </el-row>
    <el-row class="main" v-for="weekIndex in month">
      <el-col :span="3" v-for="dayIndex in weekIndex" class="card">{{ dayIndex }}</el-col>
    </el-row>
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
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card{
    background-color: #72f1ff;
    border: 1px solid #fff;
    height: 150px;
  }
</style>
