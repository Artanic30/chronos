<template>
  <div class="hour">
    <h1>{{ Hour.time }}</h1>
    <div v-for="event in Hour.events">
      <h2>{{ event.title }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  props: {
    Hour: {}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .hour{
    border:1px solid #000;
    padding: 5px;
  }
</style>
