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
                <img :src=item.nimg[0] style="width:100%;height:80px;" />
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
        this.getname();
        this.getlist();

      },
      beforeRouteLeave (to, from, next) {
        if (to.path == "/mdetails") {
          to.meta.keepAlive = true;
        } else {
          to.meta.keepAlive = false;
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
        getlist(){
          var _self=this;
          console.log(4);
          console.log(this.mname);
          this.$http.get("http://localhost:8989/imsub/News/findByname?name="+this.name).then((response) => {
            _self.list=response.data
            console.log(_self.list)
          })
        },
        getname(){
          this.name = this.$route.params.mname
        },
        back(){this.$router.back()},

        tonewsdl2(item){
          this.$router.push({name: 'newsdl', params: {id: item}})

        }
      }


    }
</script>

<style scoped>

</style>
