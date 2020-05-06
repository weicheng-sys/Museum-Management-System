<template>
<div>
  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[0].url" v-on:click="toranklists" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list[0].mname}}<br><br>2.{{list[1].mname}}<br><br>3.{{list[2].mname}}</div>
      </van-col>
    </van-row>
  </van-panel>


  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[1].url" v-on:click="toranklists1" style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list1[0].mname}}<br><br>2.{{list1[1].mname}}<br><br>3.{{list1[2].mname}}</div>
      </van-col>
    </van-row>
  </van-panel>

  <van-panel >
    <van-row>
      <van-col span="6">
        <img :src="imgs[2].url" v-on:click="toranklists2"  style="width:100%;height:100%;" />
      </van-col>
      <van-col span="18" style="text-align: left;font-size: 13px">
        <div>1.{{list2[0].mname}}<br><br>2.{{list2[1].mname}}<br><br>3.{{list2[2].mname}}</div>
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
            list1: [],
            list2: [],
            list3: [],
            loading: false,
            finished: false,
            ranktitle:'评分',
          }
      },
      created(){
          this.setdata()
      },

      methods:{
        toranklists: function () {
          this.$router.push({name: 'ranklists', params: {list: this.list ,ranktitle: "评分"}})
        },
        toranklists1: function () {
          this.$router.push({name: 'ranklists', params: {list: this.list1 ,ranktitle: "服务"}})

        },
        toranklists2: function () {
          this.$router.push({name: 'ranklists', params: {list: this.list2 ,ranktitle: "展览"}})

        },
        toranklists3: function () {
          this.$router.push({name: 'ranklists', params: {list: this.list3 ,ranktitle: "环境"}})
        },





        setdata:function () {
          var _self=this;

          this.$http.get("http://localhost:8989/imsub/MDL/findBYGrade").then((response) => {
            _self.list=response.data.result
            console.log(_self.list)

          })
          this.$http.get("http://localhost:8989/imsub/MDL/findBYGrade1").then((response) => {
            _self.list1=response.data.result
            console.log(_self.list)

          })
          this.$http.get("http://localhost:8989/imsub/MDL/findBYGrade2").then((response) => {
            _self.list2=response.data.result
            console.log(_self.list)

          })
          this.$http.get("http://localhost:8989/imsub/MDL/findBYGrade2").then((response) => {
            _self.list3=response.data.result
            console.log(_self.list)

          })


        },

      }
    }
</script>

<style scoped>

</style>
