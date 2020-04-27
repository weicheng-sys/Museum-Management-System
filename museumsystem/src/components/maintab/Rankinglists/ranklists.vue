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
    <van-cell v-for="(item,index) in list" >
        <van-panel>
          <van-row>
            <van-col span="0">
             <!-- <img :src="item.newsPicture[0]" style="width:100%;height:60px;" />-->
            </van-col>
            <van-col span="22">
              {{item.museumName}}
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
      methods:
        {
          onLoad() {
            // 异步更新数据
            // setTimeout 仅做示例，真实场景中一般为 ajax 请求
            setTimeout(() => {
              for (let i = 0; i < 10; i++) {
                this.list.push(this.list.length + 1);
              }

              // 加载状态结束
              this.loading = false;

              // 数据全部加载完成
              if (this.list.length >= 40) {
                this.finished = true;
              }
            }, 1000);
          },
          getlist: function () {
            this.list = this.$route.params.list
            this.ranktitle=this.$route.params.ranktitle
          },
          goback(){this.$router.go(-1)}


        }
    }
</script>

<style scoped>

</style>
