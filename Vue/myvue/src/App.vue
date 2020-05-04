<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
 
  <router-view />

<van-tabbar route>
  <van-tabbar-item replace to="/Home" icon="home-o">
    主页
  </van-tabbar-item>
  <van-tabbar-item replace to="/Map" icon="search">
    地图
  </van-tabbar-item>
   <van-tabbar-item replace to="/Mypage" icon="search">
    我的
  </van-tabbar-item>

</van-tabbar>

  </div>
</template>
<script>


  // <router-view />
  //   <router-link to="/">Home</router-link>
  //   <router-link to="/Mypage">Mypage</router-link>
  //    <router-link to="/Map">地图</router-link> 
  //    <router-link to="/Login">登陆与注册</router-link>
  
export default {
  name: "App", 
};
</script>

<style>


</style>


 