<template>
  <div>
    <van-tabbar route>
      <van-tabbar-item replace to="/mapview" icon="search">
        地图导览
      </van-tabbar-item>
      <van-tabbar-item replace to="/" icon="home-o">
        主页
      </van-tabbar-item>
      <van-tabbar-item replace to="/personal" icon="contact">
        个人
      </van-tabbar-item>
    </van-tabbar>


	<van-cell title="头像" is-link to="index"style="text-align:left" icon="photo" />
  <van-image round
  width="10rem"
  height="10rem"
  fit="cover"
  src="https://img.yzcdn.cn/vant/cat.jpeg">
    <template v-slot:loading>
      <van-loading type="spinner" size="20" />
    </template>
     <template v-slot:error>加载失败</template>
  </van-image>
  <van-cell title="收藏" is-link to="collect"style="text-align:left" icon="label"/>
  <van-cell title="设置" is-link to="/setting1"style="text-align:left" icon="setting"/>
  </div>
</template>

<script>
  export default {
    name: "personal",
    data(){
      return {
        active: 'personal',
      }
    },
  }
</script>

<style scoped>
  .bgset{
  background: #50a1e6;}
</style>
