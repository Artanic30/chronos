<template>
  <div id="app" class="container">
    <ChronosNav></ChronosNav>
    <router-view></router-view>
  </div>
</template>

<script>
  import ChronosNav from '@/components/Nav.vue'
  export default {
    name: 'app',
    components: {
      'ChronosNav': ChronosNav
    }
  }
</script>

<style>
</style>
