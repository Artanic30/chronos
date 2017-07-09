<template>
  <nav class="navbar navbar-default navbar-static-top">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">Chronos</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li><a @click="BackSubmit()">返回</a></li>
          <li><a @click="">{{ Year }}年</a></li>
          <li><a @click="MonthViewSubmit()">{{ Month+1 }}月</a></li>
          <li><a @click="DayViewSubmit()">{{ Day }}日</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate === true">
          <li><router-link to="/profile">资料修改</router-link></li>
          <li><router-link to="/logout">注销</router-link></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate === false || Authenticate === null">
          <li><router-link to="/login">登陆</router-link></li>
        </ul>
      </div>
  </nav>
</template>

<script>
  export default {
    data () {
      return {
        LastView: ''
      }
    },
    methods: {
      BackSubmit () {
        var lastView = this.$store.state.LastView
        if (lastView === '/login') {
          this.$router.push({'path': lastView})
        } else if (lastView === '/about') {
          this.$router.push({'path': lastView})
        } else if (lastView === '/register') {
          this.$router.push({'path': lastView})
        } else if (lastView === '/profile') {
          this.$router.push({'path': lastView})
        } else {
          // todo:
          console.log('hello...')
        }
        console.log(lastView)
      },
      MonthViewSubmit () {
        var nowView = this.$store.state.NowView
        this.$store.commit('ApplyLastView', nowView)
        console.log(nowView)
      },
      DayViewSubmit () {

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
