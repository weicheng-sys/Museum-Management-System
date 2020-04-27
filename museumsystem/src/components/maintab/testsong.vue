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

    {{lists[0]}}<br>
    {{lists[1]}}
   <!-- <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
    >
      <li v-for="item in lists" class="list-item" >
        <news v-bind:nums="item"></news>
      </li>

    </van-list>-->

  </div>
</template>

<script>
    export default {
        name: "testsong",
      data(){
          return{
            loading: false,
            finished: false,
            lists : []
          }
      },
      created() {
          this.getlists()
      },
      methods: {
          getlists(){
            var _self=this;
            this.$http.get("/static/baidunews.json").then((response) => {
              _self.lists=response.data
              console.log(response.data);

            })
          },
          back(){
            this.$router.push('/')
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
        }



      }
    }
</script>

<style scoped>
  .bgset{
    background: #50a1e6;
  }
</style>
