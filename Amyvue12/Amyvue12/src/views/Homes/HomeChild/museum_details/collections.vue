<template>
  <div>
    <van-sticky>
      <van-row  style="width:100%;height:50px;" >
        <van-col span="24"  >
          <van-nav-bar
            left-text="返回"
            left-arrow
            @click-left="back"
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
      <van-cell v-for="item in list" :key="item"  >
        <van-panel v-on:click="tonewsdl2(item.nid)">
          <van-row>
            <van-col  style="text-align: left;font-size: 18px">
              {{item.title}}
            </van-col>

          </van-row>
          <van-row>
            <van-col span="16" style="text-align: left;font-size: 12px">
              <br><br>{{item.mname}}<br>
              {{item.pubisher}}
            </van-col>
            <van-col span="8">
              <img :src=sliptsd(item.nimg)[0] style="width:100%;height:80px;" />
            </van-col>
          </van-row>

        </van-panel>
      </van-cell>
    </van-list>

  </div>
</template>

<script>
  export default {
    name: "collections",
    data(){
      return {
        collection:[{
          mid: 1,
          cname:"松",
          cimg:["https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3493135802,624957787&fm=173&app=25&f=JPEG?w=529&h=294&s=F281D80302C30CEC34913CB00300C020"],
          years:"1999.7.15",
          explain:"长得帅",
          size:"182",
          src:"神域"
        }],
        loading: false,
        finished: false,
        list:[],
        id:0,
        name:"",

      }
    },
    created() {
      this.getid();
      this.getlist();

    },
    beforeRouteEnter(to, from, next) {
//判断从index页面进入，将list的isBack设置为true
//这样就可以请求数据了
      if (from.name == 'mdetails') {
        to.meta.isBack = true;
      }
      next();
    },
    activated: function () {
      if (this.$route.meta.isBack || this.isFirstEnter) {
        //清理已有商品列表的数据，重新请求数据，如果不清除的话就会有之前的商品缓存，延迟显示最新的商品
        this.list = [];
        //请求数据
        this.getid();
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
    beforeRouteLeave (to, from, next) {

      if(to.path=="/mdetails"){
        to.meta.keepAlive=false;
      }
      next();
    },
    methods:{
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
      sliptsd(img){
        var img2 = img.split('[')
        var img3 = img2[1].split(']')
        var img4=img3[0].replace(/\'/g,'')
        return img4.split(',')
      },
      getlist(){
        var _self=this;
        console.log(4);
        console.log(this.mname);
        this.$http.get("http://39.98.108.11:8081/News/findByname?name="+this.name).then((response) => {
          _self.list=response.data
          console.log(_self.list)
        })
      },
      getid(){
        this.name = this.$route.params.mname;
        this.id=this.$route.params.mid;
        console.log(this.name)
      },
      back(){this.$router.push({name: 'mdetails', params: {id: this.id}})},

      tonewsdl2(item){
        this.$router.push({name: 'newsdl2', params: {id: item,name:this.name,mid:this.id}})

      }
    }


  }
</script>

<style scoped>

</style>
