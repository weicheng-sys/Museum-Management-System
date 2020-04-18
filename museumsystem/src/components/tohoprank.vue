<template>


  <div>
    <van-row class="bgset" style="width:100%;height:50px;" >
      <van-col span="24" v-on:click="back" >
        <van-nav-bar
          title="热度榜"
          left-text="返回"
          left-arrow
          @click-left="back"
        />

      </van-col>

    </van-row>

      <van-card
        num="2"
        price="2.00"
        desc="博物馆"
        title="地址"
        thumb="https://img.yzcdn.cn/vant/ipad.jpeg"
      />
    </div>
</template>

<script>
    export default {
        name: "tohoprank",
      data(){
          return{
            imgs:[

              {url:require("@/assets/test4.jpg")},

              {url:require("@/assets/test5.jpg")},

              {url:require("@/assets/test6.jpg")}

            ]
          }
      },
      methods: {
        back: function () {
          this.$router.push('/')
        }
      }
      }
</script>

<style scoped>
  .bgset{
    background: #50a1e6;
  }
</style>
