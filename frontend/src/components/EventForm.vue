<template>
  <el-form>
    <el-form-item label="事件名称">
    </el-form-item>
    <el-form-item label="开始时间">
    </el-form-item>
    <el-form-item label="结束时间">
    </el-form-item>
    <el-form-item label="地点">
    </el-form-item>
    <el-form-item label="事件内容">
    </el-form-item>
    <el-form-item label="心情" v-if="type === 'past'">
    </el-form-item>
    <el-form-item label="">
      
    </el-form-item>

  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        EventForm: {
          Name: '',
          Type: '',
          Content: '',
          StartDatetime: '',
          EndDatetime: '',
          Emotion: '',
          Place: ''
        }
      }
    }
  }
</script>
<style>
</style>
