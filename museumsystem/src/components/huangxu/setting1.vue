<template>
  <div>
  <van-cell title="修改密码" is-link to="changepassword"style="text-align:left" /></van-cell>
  <van-cell title="切换账号" is-link to="changeaccount"style="text-align:left" /></van-cell>
  </div>
</template>
<script>
  export default {
    name: "setting1",
    data(){
      return {
        active: 'setting1',
      }
    },
  }
</script>
<style scoped>
  .bgset{
  background: #50a1e6;}
</style>
