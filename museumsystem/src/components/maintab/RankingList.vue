<template>
<div>
  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[0].url" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.国家博物馆<br><br>2.军事博物馆<br><br>3.天文博物馆</div>
      </van-col>
    </van-row>
  </van-panel>
  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[1].url" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.国家博物馆<br><br>2.军事博物馆<br><br>3.天文博物馆</div>
      </van-col>
    </van-row>
  </van-panel>
  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[2].url" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.国家博物馆<br><br>2.军事博物馆<br><br>3.天文博物馆</div>
      </van-col>
    </van-row>
  </van-panel>




</div>
</template>

<script>
    export default {
        name: "RankingList",
      data(){
          return{
            imgs:[

              {url:require("@/assets/rank1.png")},

              {url:require("@/assets/rank2.png")},

              {url:require("@/assets/rank3.png")},

              {url:require("@/assets/test7.png")}
            ]
          }
      }
    }
</script>

<style scoped>

</style>
