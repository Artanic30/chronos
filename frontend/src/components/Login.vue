<template>
  <el-form>
    <el-form-item label="用户名">
      <el-input v-model="LoginForm.Username"></el-input>
    </el-form-item>
    <el-form-item label="密码">
      <el-input type="password" v-model="LoginForm.Password"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="small" @click="LoginSubmit">登陆</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        LoginForm: {
          'Username': '',
          'Password': ''
        }
      }
    },
    methods: {
      LoginSubmit () {
        axios({
          methods: 'POST',
          url: '',
          data: JSON.stringify({
            'Username': this.LoginForm.Username,
            'Password': this.LoginForm.Password
          })
        }.bind(this)).then(function (response) {
          if (response.data.message === 'Success') {
            this.$notify({
              title: '成功',
              message: '成功登陆',
              type: 'success'
            })
          } else if (response.data.message === 'Error') {
            this.$notify.error({
              title: '错误',
              message: '登陆失败'
            })
          } else {
            this.$notify.error({
              title: '错误',
              message: '服务器出错'
            })
          }
        }.bind(this))
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>
<style>
</style>
