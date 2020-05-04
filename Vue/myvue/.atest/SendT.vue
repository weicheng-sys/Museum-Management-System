<template>
  <section>
    <div id="hello">
      <h1>Hello World ~</h1>
    </div>
    <button @click="get">点击</button>
  </section>
</template>
<script>
  export default {
    name:"SendT",
    methods: {
      get() {
       console.log(this.$refs['hello']);
        console.log(this.$refs.hello); 
      }
    },

  }
</script>
