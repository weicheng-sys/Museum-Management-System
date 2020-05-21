<template>
  <div>
    <van-sticky>

      <van-row class="bgset" style="width:100%;height:50px;" >
        <van-col span="24"  >
          <van-nav-bar
            title = "排行"
            left-text="返回"
            left-arrow
            @click-left="goback"
          />
        </van-col>
      </van-row>
    </van-sticky>

    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
    >
      <van-cell v-for="(item,index) in list" :key="index">
        <van-panel v-on:click="tomdetails(item.mid)">
          <van-row>
            <van-col span="0">
              <!-- <img :src="item.newsPicture[0]" style="width:100%;height:60px;" />-->

            </van-col>
            <van-col span="22">
              {{item.mname}}
            </van-col>
            <van-col span="2">
              {{index+1}}
            </van-col>
          </van-row>
        </van-panel>

      </van-cell>
    </van-list>
  </div>
</template>

<script>
  export default {
    name: "ranklists",
    data(){
      return{
        list: [],
        loading: false,
        finished: false,
        ranktitle:'',
      }
    },
    created(){
      this.getlist()
    },
    beforeRouteEnter(to, from, next) {
//判断从index页面进入，将list的isBack设置为true
//这样就可以请求数据了
      if (from.name == 'Home') {
        to.meta.isBack = true;
      }
      next();
    },
    activated: function () {
      if (this.$route.meta.isBack || this.isFirstEnter) {
        //清理已有商品列表的数据，重新请求数据，如果不清除的话就会有之前的商品缓存，延迟显示最新的商品
        this.list= [];
        //请求数据
        this.getlist();
      }
      //重新设置当前路由的isBack
      this.$route.meta.isBack = false;
      //重新设置是否第一次进入
      this.isFirstEnter = false;
    },
    mounted: function () {
      //如果是第一次进入，或者刷新操作的话，也请求数据
      this.isFirstEnter = true;
    },

    methods:
      {
        onLoad() {
          // 异步更新数据
          // // setTimeout 仅做示例，真实场景中一般为 ajax 请求
          let l = this.list.length;
          let s = 0
          setTimeout(() => {
            for (let i = 0; i < l; i++) {
              s = s + 1;
            }
            // 加载状态结束
            this.loading = false;
            // 数据全部加载完成
            if (s >= l) {
              this.finished = true;
            }

          }, 1000);
        },
        getlist: function () {
          this.list = this.$route.params.list
          this.ranktitle=this.$route.params.ranktitle
        },
        beforeRouteLeave (to, from, next){
          if(to.path=="/mdetails"){
            from.meta.keepAlive = true;
          }
          from.meta.keepAlive = false;
          next();
        },
        goback(){this.$router.push("/Home")},

        tomdetails: function (mid) {
          this.$router.push({name: 'mdetails', params: {id: mid}})
        },


      }
  }
</script>

<style scoped>

</style>
