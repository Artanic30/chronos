<template>
  <div class="hour">
    <p>{{ Hour.time }}</p>
    <div v-for="event in Hour.events">
      <h3>{{ event.title }}</h3>
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
  }
</style>
