<template>
  <div>
    <van-tabbar route>
      <van-tabbar-item replace to="/mapview" icon="search">
        地图导览
      </van-tabbar-item>
      <van-tabbar-item replace to="/" icon="home-o">
        主页
      </van-tabbar-item>
      <van-tabbar-item replace to="/personal" icon="search">
        个人
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
  export default {
    name: "personal",
    data(){
      return {
        active: 'personal',
      }

    }
  }
</script>

<style scoped>

</style>
