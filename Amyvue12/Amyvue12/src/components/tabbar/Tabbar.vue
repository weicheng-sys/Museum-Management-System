<template>
<div>
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
export default {
    name:'Tabbar'
}
</script>