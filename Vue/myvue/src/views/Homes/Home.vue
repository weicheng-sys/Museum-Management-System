<template>
  <div>
    <van-row class="bgset">
      <van-col span="4">
        <img :src="imgs[3].url" style="width:100%;height:50px;" />
      </van-col>
      <van-col span="20" >
        <form action="/">
          <van-search

            v-model="value"
            show-action
            placeholder="请输入搜索关键词"
            @search="onSearch"
            style="height: 50px"
          />
        </form>
      </van-col>
    </van-row>



    <!--轮播图-->
    <van-swipe :autoplay="2500" style="weight: 100% ;height:200px">
      <van-swipe-item><img :src="imgs[0].url" v-on:click="tohop" style="weight: 100% ; height: 150px"><br></van-swipe-item>
      <van-swipe-item><img :src="imgs[1].url" v-on:click="tohop" style="weight: 100% ; height: 150px"><br></van-swipe-item>
      <van-swipe-item><img :src="imgs[2].url" v-on:click="tohop" style="weight: 100% ; height: 150px"><br></van-swipe-item>
    </van-swipe>
   <!-- 标签页，包含（新闻，排行，视频）-->
    <van-tabs v-model="active2" >

      <van-tab title="视频" name="视频">
        <Video></Video>
      </van-tab>

      <van-tab title="新闻"  name="新闻" >
        <News></News>
      </van-tab>

      <van-tab title="排行" name="排行">
        <RankingList></RankingList>
      </van-tab>
    </van-tabs>

  </div>

</template>

<script>

  import News from "./HomeChild/News";
  import Video from "./HomeChild/Video";
  import RankingList from "./HomeChild/RankingList";

  import Axios from "axios";					//axios接口引用
    export default {
        name: "ranking",
      components: {Video, RankingList, News },
      data(){
          return{
            list: [], 
            value:'',
            active2: '新闻',
            active: 'home',
            imgs:[

              {url:require("@/assets/test1.jpg")},

              {url:require("@/assets/test2.jpg")},

              {url:require("@/assets/test3.jpg")},

              {url:require("@/assets/test7.png")}
            ]
          };
        },
      methods: {
        onCancel() {

        },
        onLoad() {
          // 异步更新数据
          // setTimeout 仅做示例，真实场景中一般为 ajax 请求
          setTimeout(() => {
            for (let i = 0; i <0; i++) {
              this.list.push(this.list.length + 1);
            }

            // 加载状态结束
            this.loading = false;

            // 数据全部加载完成
            if (this.list.length >=10) {
              this.finished = true;
            }
          }, 1000);
        },
        tohop(){
       this.$router.push('/tohoprank')
       },   
        onSearch(val) {
          Axios.get('http://localhost:8089/user/findAll').then((results)=>{
           console.log(JSON.stringify(results.data)); 
    //         console.log("findAll"+results.data.results);
    // console.log("findAll"+results.data.msg);
});
          var t = this;
          Axios.get('https://v1.alapi.cn/api/new/toutiao?start=1&num=100').then((res)=>{
            t.list=res.data.data

            this.$router.push({name:'Search',
              params:{
                keyword: this.value,
                list:this.list
              }})
          })


        },

      }
    }
</script>

<style >
.bgset{
  background: #50a1e6;
}
</style>
