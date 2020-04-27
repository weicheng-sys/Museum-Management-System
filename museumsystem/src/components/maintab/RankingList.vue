<template>
<div>
  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[0].url" v-on:click="toranklists" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list[0].museumName}}<br><br>2.{{list[1].museumName}}<br><br>3.{{list[2].museumName}}</div>
      </van-col>
    </van-row>
  </van-panel>


  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[1].url" v-on:click="toranklists" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list[0].museumName}}<br><br>2.{{list[1].museumName}}<br><br>3.{{list[2].museumName}}</div>
      </van-col>
    </van-row>
  </van-panel>

  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[2].url" v-on:click="toranklists"  style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list[0].museumName}}<br><br>2.{{list[1].museumName}}<br><br>3.{{list[2].museumName}}</div>
      </van-col>
    </van-row>
  </van-panel>

  <van-panel >
    <van-row>
     <br>
      <br>
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
            ],
            list: [],
            loading: false,
            finished: false,
            ranktitle:'',
          }
      },
      created(){
          this.setdata()
      },

      methods:{
        toranklists: function () {
          this.$router.push({name: 'ranklists', params: {list: this.list ,ranktitle: this.ranktitle}})

        },
        settitle:function(){
          this.ranktitle='热度'
        },
        setdata:function () {
          var _self=this;
          this.$http.get("/static/baidunews.json").then((response) => {
            _self.list=response.data

          })
        },

      }
    }
</script>

<style scoped>

</style>
