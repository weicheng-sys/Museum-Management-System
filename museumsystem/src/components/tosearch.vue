<template>
  <div>

    <van-row class="bgset" style="width:100%;height:50px;" >
      <van-col span="24" v-on:click="back" >
        <van-nav-bar
          title="热搜榜"
          left-text="返回"
          left-arrow
          @click-left="back"
        />
      </van-col>
    </van-row>
    陈占国负责

    </div>


</template>

<script>
    export default {
        name: "tosearch",
      data(){
          return{
            imgs:[

              {url:require("@/assets/test1.jpg")},

              {url:require("@/assets/test2.jpg")},

              {url:require("@/assets/test3.jpg")},

              {url:require("@/assets/test7.png")}
            ]
          }

      },
       methods: {
       back() {
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
