<template>
<div>
  <!--新闻显示-->
  <van-notice-bar color="#1989fa" background="#ecf9ff" left-icon="info-o">
    {{list[0].newsTitle}}
  </van-notice-bar>
  <van-list
    v-model="loading"
    :finished="finished"
    finished-text="没有更多了"
    @load="onLoad"
  >
    <van-cell v-for="item in list" class="list-item" >
      <van-panel v-on:click="tonewsdl(item.nid)">
        <van-row>
          <van-col  style="text-align: left;font-size: 18px">
            {{item.title}}
          </van-col>

        </van-row>
        <van-row>
          <van-col span="16" style="text-align: left;font-size: 12px">
            <br><br>{{item.mname}}<br>
            {{item.publisher}}
          </van-col>
          <van-col span="8">
            <img :src=item.nimg[0] style="width:100%;height:80px;" />
          </van-col>
        </van-row>

      </van-panel>
    </van-cell>
  </van-list>

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
        name: "newview",
      data(){
          return {
            loading: false,
            finished: false,

            list: [{"pubisher": "21:13发布时间：04-03","mname": "中国人民抗日战争纪念馆","title": "“清明节的铭记”主题教育系列活动在抗战馆启动",
              "nimg": [
                "https://pics3.baidu.com/feed/0ff41bd5ad6eddc443c5e665d32ec2fb5366330d.jpeg?token=00f90ac60ee178e943ccedb68cc15a4f"
           ]
            },
                  {  "pubisher": "09:43发布时间：19-11-14","mname": "中国地质博物馆","title": "科学家或将揭开火山喷发之谜，火山爆发后的威力有多厉害？",
                    "nimg": [
                      "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3493135802,624957787&fm=173&app=25&f=JPEG?w=529&h=294&s=F281D80302C30CEC34913CB00300C020"
                    ]}]
          }
      },
      created(){
        this.getlist()
      },
      methods:{
        /*setdata:function () {
          var _self=this;
          this.$http.get("/static/news_info.json").then((response) => {
            _self.list=response.data

          })
        },*/
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
          console.log("所有新闻")
          this.$http.get("http://localhost:8989/imsub/News/findAll").then((response) => {
            _self.list=response.data.result
            console.log(_self.list)

          })
        },
        tonewsdl(id){
          this.$router.push({name: 'newsdl', params: { id: id,list:this.list}})

        }
      }

    }
</script>

<style scoped>

</style>
