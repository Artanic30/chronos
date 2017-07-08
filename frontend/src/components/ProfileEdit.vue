<template>
  <el-form ref="ProfileForm" :model="ProfileForm">
    <el-form-item label="">
      <el-input v-model="ProfileForm.Nickname"></el-input>
    </el-form-item>
    <el-form-item label="">
      <el-button type="small" @click="ProfileFormSubmit()"></el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ProfileForm: {
          Nickname: ''
        }
      }
    },
    methods: {
      ProfileFormSubmit () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Nickname: this.ProfileForm.Nickname
          })
        }).then(function (response) {
          if (response.data.message === 'Success') {
            this.$notify({
              'title': '成功',
              'message': '成功更改用户信息',
              'type': 'success'
            })
          } else {
            this.$notify.error({
              'title': '失败',
              'message': '更改用户信息失败'
            })
          }
        })
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: '',
        data: JSON.stringify({
          Username: this.GetUserName,
          Token: this.GetToken
        }).then(function (response) {
          if (response.data.message === 'Success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              'title': '失败',
              'message': '获取用户资料失败'
            })
          }
        })
      })
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
    }
  }
</script>
