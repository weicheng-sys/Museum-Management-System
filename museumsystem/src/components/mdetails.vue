<template>
  <div>

    <van-sticky>
      <van-row class="bgset" style="width:100%;height:50px;" >
        <van-col span="24"  >
          <van-nav-bar
            left-text="返回"
            left-arrow
            @click-left="back">

          </van-nav-bar>
        </van-col>
      </van-row>
    </van-sticky>


          <img :src=list.mimg[0] style="width:100%;height:200px;" />

    <van-panel style="text-align: left;font-size: 15px;height:80px">
      <div>
        <van-row>
          <textarea class="maintext" v-model="list.basic_info" style="height:80px;width: 100%;border: none;outline: none;resize:none;" readonly>
          </textarea>
        </van-row>

      </div>
    </van-panel>
    <van-divider />
    <van-panel title="简述"  style="text-align: left;font-size: 20px">
      <div style="text-align: left;font-size: 13px">
       <textarea class="maintext" v-model="list.other_info" style="height:80px;width: 100%;border: none;outline: none;resize:none;" readonly>
          </textarea>
      </div>
    </van-panel >
    <van-panel style="background: rgba(80,230,225,0.28);margin : 10px 10px 10px 10px;border-radius: 35px;">
      <van-row>
        <van-col span="1">
        </van-col>
        <van-col span="7" style="text-align: left;font-size: 20px" > 综合评分：</van-col>
        <van-col span="3" style="text-align: left;font-size: 15px">{{list.grade}}</van-col>
        <van-col span="12" style="text-align: right;font-size: 20px">
          <van-rate v-model=list.grade allow-half void-icon="star" void-color="#eee" />
        </van-col>
        <van-col span="1">
        </van-col>
      </van-row>
      <!--评分面板-->
      <van-row><br>
        <van-col span="1">
        </van-col>
        <van-col span="8" style="text-align: left;font-size: 20px">展览：</van-col>
        <van-col span="15">
          <van-progress :percentage=list.grade_1 stroke-width="8" />
        </van-col>
      </van-row>
      <van-row><br>
        <van-col span="1">
        </van-col>
        <van-col span="8" style="text-align: left;font-size: 20px">服务：</van-col>
        <van-col span="15">
          <van-progress :percentage=list.grade_2 stroke-width="8" />
        </van-col>
      </van-row>
      <van-row><br>
        <van-col span="1">
        </van-col>
        <van-col span="8" style="text-align: left;font-size: 20px">环境：</van-col>
        <van-col span="15">
          <van-progress :percentage=list.grade_3 stroke-width="8" />
        </van-col>
      </van-row>
      <van-row>

        <van-col span="24" style="text-align: center;font-size: 18px">
          <van-button text="为他打分" type="round" color="#a92e43" v-on:click="toscoring"></van-button>
        </van-col>
      </van-row>
    </van-panel>


    <van-panel>
      <van-row>
        <van-col span="4" style="text-align: left;font-size: 16px">新闻：</van-col>
        <van-col span="20" style="text-align: right;font-size: 16px" v-on:click="tocollection">查看全部</van-col>
      </van-row>
      <van-grid style="height: 100px">
        <van-grid-item  text="文字">
          <img :src=mlist.mimg[0] style="width:100%;height:100%;" />
        </van-grid-item>
        <van-grid-item  text="文字">
          <img :src=mlist.mimg[0] style="width:100%;height:100%;" />
        </van-grid-item>
        <van-grid-item  text="文字">
          <img :src=mlist.mimg[0] style="width:100%;height:100%;" />
        </van-grid-item>
        <van-grid-item  text="文字">
          <img :src=mlist.mimg[0] style="width:100%;height:100%;" />
        </van-grid-item>
      </van-grid>
    </van-panel>

    <van-row>
      <van-col span="4" style="text-align: left;font-size: 18px">
        <van-image
          round
          width="40px"
          height="40px"
          src="https://img.yzcdn.cn/vant/cat.jpeg"
        />
      </van-col>

      <van-col span="16" style="text-align: left;font-size: 18px">
        <van-cell-group>
        <van-field v-model="value" placeholder="请输入评价" />
      </van-cell-group>
      </van-col>

      <van-col span="4" style="text-align: right;font-size: 18px">
        <van-button text="评价" type="info" color="#e33e33"></van-button>
      </van-col>
     </van-row>

    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
    >
      <van-cell v-for="item in list.evaluate"   >

        <van-panel>
          <van-row>
            <van-col span="4" style="text-align: left;font-size: 18px">
              <img :src=mlist.mimg style="width:40px;height:40px;border-radius: 50%;background-repeat: no-repeat"
  />
            </van-col>
            <van-col span="18" style="text-align: left;font-size: 16px">
              用户名
            </van-col>
            <van-col span="2">
              举报
            </van-col>
            </van-row>
          <van-row>
           {{item}}
          </van-row>
        </van-panel>
      </van-cell>
    </van-list>

     </div>
    </template>

<script>
    export default {
        name: "mdetails",
      data() {
        return {
          value: "",
          p1: [60,70,80],
          value1: 2,
          list: [],
          Collection: [],
          user :[],
          mid :0,
          mlist: {
            mid:1,
            mname:"中国航天博物馆",
            maddr:"北京",
            mtype:"科技",
            ticket:10,
            buidtime:"1969",
            opentime:"全天",
            cnum: 650,
            ctype:35,
            enum:8,
            mimg:["https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3493135802,624957787&fm=173&app=25&f=JPEG?w=529&h=294&s=F281D80302C30CEC34913CB00300C020"],
            evaluate:"还不错",
            grade:4.5},
          loading: false,
          finished: false,
          currentPage: 1,
        };
      },
      created() {
          this.getid();
          this.getlist();
      },
      beforeRouteLeave (to, from, next) {
        from.meta.keepAlive = false;
        next();
      },
      methods: {
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
        back(){this.$router.back()},
        tocollection(){
          this.$router.push({name: 'collections', params: {mname: this.list.mname}})
        },
        getid(){
          this.mid = this.$route.params.id
        },
        getlist(){
          var _self=this;
          console.log("博物馆详情页面")

          this.$http.get("http://localhost:8989/imsub/MDL/findByid?id="+this.mid).then((response) => {
            _self.list=response.data
            console.log(_self.list)
          })
        },
        toscoring(){
          this.$router.push({name: 'scoring', params: {id: this.list.mid}})
        },

      },

     }
</script>

<style scoped>
  .maintext{
    text-align: left;
    white-space: pre-wrap;
    text-indent: 2em;
    line-height: 1.8em;


  }
</style>
