<template>
<div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <keep-alive>
        <router-view v-if="$route.meta.keepAlive"></router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive"></router-view>

      <div v-if="$route.meta.keeptabbar">
    <van-tabbar route>
  <van-tabbar-item replace to="/Home" icon="home-o">
    主页
  </van-tabbar-item>
  <van-tabbar-item replace to="/Map" icon="aim">
    地图
  </van-tabbar-item>
   <van-tabbar-item replace to="/Mypage" icon="user-circle-o">
    我的
  </van-tabbar-item>
</van-tabbar>
</div>

</div>
</template>

<script>
import Tabbar from '@/components/tabbar/Tabbar'
export default {
    name: "App",
    comments: {
        Tabbar
    }
};
</script>

<style>
#app {
    text-align: center;
}
</style>
