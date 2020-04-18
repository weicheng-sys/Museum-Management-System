<template>
    <div>
      <van-tabbar route>
        <van-tabbar-item replace to="/mapview" icon="search">
          地图导览
        </van-tabbar-item>
        <van-tabbar-item replace to="/" icon="home-o">
          主页
        </van-tabbar-item>
        <van-tabbar-item replace to="/tosearch" icon="search">
          个人
        </van-tabbar-item>
      </van-tabbar>
    </div>
</template>

<script>
    export default {
        name: "mapview",
      data(){
          return {
            active: 'mapview',
          }

      }
    }
</script>

<style scoped>

</style>
