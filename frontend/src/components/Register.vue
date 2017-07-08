<template>
  <el-form>
    <el-form-item label="用户名">
      <el-input v-model="RegisterForm.Username"></el-input>
    </el-form-item>
    <el－form－item label="密码">
      <el-input type="password" v-model="RegisterForm.Password"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="small" @click="RegisterSubmit()">注册</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        RegisterForm : {
          Username: '',
          Password: '',
        }
      }
    },
    methods: {
      RegisterSubmit () {
        axios({
          methods: "POST",
          url: '',
          data: JSON.stringify({
            "Username": this.RegisterForm.Username,
            "Password": this.RegisterForm.Password
          })
        }.bind(this)).then(function (response) {
          if (response.data.message === 'Success') {
            this.$notify({
              title: '成功',
              message: '成功注册',
              type: 'success'
            })
          } else if (response.data.message === 'Error') {
            this.$notify.error({
              title: '错误',
              message: '注册失败'
            })
          } else ｛
          this.$notify.error({
            title: '错误',
            message: '服务器出错'
          })
          ｝
        }.bind(this))
    }
  }
</script>
<style>
</style>
