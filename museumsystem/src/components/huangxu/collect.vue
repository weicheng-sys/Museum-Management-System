<template>
  <div>
  <van-cell title="收藏" is-link to="index"style="text-align:left" icon="label"/></van-cell>
  <van-cell title="设置" is-link to="/setting1"style="text-align:left" icon="setting"/></van-cell>
  </div>
</template>
<script>
  export default {
    name: "collect",
    data(){
      return {
        active: 'collect',
      }
    },
  }
</script>
<style scoped>
  .bgset{
  background: #50a1e6;}
</style>
