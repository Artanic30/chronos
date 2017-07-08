<template>
  <div class="container">
    <h1>Welcome to Chronos!</h1>
    <br>
    <el-form ref="LoginForm" :model="LoginForm">
      <el-form-item label="用户名">
        <el-input v-model="LoginForm.Username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="LoginForm.Password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-row>
          <el-col :span="8" :offset="9">
            <el-button type="primary" @click="LoginSubmit">登陆</el-button>
          </el-col>
        </el-row>
      </el-form-item>
    </el-form>
  </div>
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
          .catch(function () {
            this.$notify.error({
              'title': '错误',
              'message': '服务器出错'
            })
          })
      }
    },
    mounted: function () {
      var NowView = 'Login'
      this.$store.commit('ApplyNowView', NowView)
    },
    destroyed: function () {
      this.$store.commit('ApplyLastView', '/Login')
    }
  }
</script>
<style scoped>
  .container {
    padding-top: 50px;
    padding-left: 400px;
    padding-right: 400px;
  }
</style>
