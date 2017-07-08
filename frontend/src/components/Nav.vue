<template>
  <nav class="navbar navbar-default navbar-static-top">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">Project name</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li><el-button @click="BackSubmit()">返回</el-button></li>
          <li><el-button @click="YearViewSubmit()">年</el-button></li>
          <li><el-button @click="MonthViewSubmit()">月</el-button></li>
          <li><el-button @click="DayViewSubmit()">日</el-button></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate === false">
          <li><router-link to="/profile">资料修改</router-link></li>
          <li><router-link to="/logout">注销</router-link></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate === true">
          <li><router-link to="/login">登陆</router-link></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'Nav',
    data () {
      return {
        LastView:
      }
    },
    methods: {
      BackSubmit () {

      },
      YearViewSubmit () {

      },
      MonthViewSubmit () {

      },
      DayViewSubmit () {

      }
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
    }
  }
</script>

<style>

  body{margin: 0;}
  #app {
    min-width: 1200px;
    margin: 0 auto;
    font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
  }
  /* 头部导航 */
  header{z-index: 1000;min-width: 1200px;transition: all 0.5s ease;  border-top: solid 4px #3091F2;  background-color: #fff;  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);  }
  header.header-fixed{position: fixed;top: 0;left: 0;right: 0;}
  header .el-menu-demo{padding-left: 300px!important;}

  /* 路由切换动效 */
  .fade-enter-active, .fade-leave-active {
    transition: all .5s;
  }
  .fade-enter, .fade-leave-active {
    opacity: 0;
  }

  .list-enter-active, .list-leave-active {
    transition: all 1s;
  }
  .list-enter, .list-leave-active {
    opacity: 0;
    transform: translateY(30px);
  }

  /* 导航栏菜单选中效果 */
  .isActive{color: #20a0ff!important;}
  #app main .aside .is-active{color: #475669;}

  /* 卡片 */
  .el-card{overflow: visible!important;}
</style>
