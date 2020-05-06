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

      <van-panel style="background: rgba(80,230,225,0.28);margin : 10px 10px 10px 10px;border-radius: 35px;">
        <van-row>
          <van-col span="1">
          </van-col>
          <van-col span="7" style="text-align: left;font-size: 20px" > 综合评分：</van-col>
          <van-col span="3" style="text-align: left;font-size: 15px">{{p2[3]}}</van-col>
          <van-col span="12" style="text-align: right;font-size: 20px">
            <van-rate v-model=p2[3] allow-half void-icon="star" void-color="#eee" />
          </van-col>
          <van-col span="1">
          </van-col>
        </van-row>
        <!--评分面板-->
        <van-row><br>
          <van-col span="1">
          </van-col>
          <van-col span="6" style="text-align: left;font-size: 20px">展览：</van-col>
          <van-col span="15">
            <van-slider v-model="p1[0]" @change="onChange(p1[0])">
              <template #button>
                <div class="custom-button">
                  {{p2[0]}}
                </div>
              </template>
            </van-slider>
          </van-col>
        </van-row>
        <van-row><br>
          <van-col span="1">
          </van-col>
          <van-col span="6" style="text-align: left;font-size: 20px">服务：</van-col>
          <van-col span="15">
            <van-slider v-model="p1[1]" @change="onChange1(p1[1])">
              <template #button>
                <div class="custom-button">
                  {{p2[1]}}
                </div>
              </template>
            </van-slider>
          </van-col>
        </van-row>
        <van-row><br>
          <van-col span="1">
          </van-col>
          <van-col span="6" style="text-align: left;font-size: 20px">环境：</van-col>
          <van-col span="15">
            <van-slider v-model="p1[2]" @change="onChange2(p1[2])">
              <template #button>
                <div class="custom-button">
                  {{p2[2]}}
                </div>
              </template>
            </van-slider>
          </van-col>
        </van-row>
        <van-row>
          <van-button text="提交" type="round" color="#a92e43" v-on:click="setscoring"></van-button>
        </van-row>

      </van-panel>


    </div>
</template>

<script>
  import { Toast } from 'vant';
    export default {
        name: "scoring",
      data(){
          return{
            p1: [0,0,0,0],
            p2: [0,0,0,0],
            id: 0,
            list : {},
            ok:"",

          }
      },
      created() {
          this.getid();
          this.getlist();
        this.p1[0]=this.list.grade_1;
        this.p1[1]=this.list.grade_2;
        this.p1[2]=this.list.grade_3;
        this.p1[3]=this.list.grade;


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
        back(){
          this.$router.back()},
        onChange(value1) {
          this.p2[0]=value1;
          this.p1[3]=(((this.p1[0]+this.p1[1]+this.p1[2])/300)*5).toFixed(2);
          this.p2[3]=this.p1[3];
          Toast('展览：' + value1);
          Toast(this.p2[0])
        },
        onChange1(value1) {
          this.p2[1]=value1;
          this.p1[3]=(((this.p1[0]+this.p1[1]+this.p1[2])/300)*5).toFixed(2);
          this.p2[3]=this.p1[3];
          Toast('服务：' + value1);
        },
        onChange2(value1) {
          this.p2[2]=value1;
          this.p1[3]=(((this.p1[0]+this.p1[1]+this.p1[2])/300)*5).toFixed(2);
          this.p2[3]=this.p1[3];
          Toast('环境：' + value1);
        },
        setscoring(){
          this.list.grade_1=(this.p2[0]+this.p1[0])/2;
          this.list.grade_2=(this.p2[1]+this.p1[1])/2;
          this.list.grade_3=(this.p2[2]+this.p1[2])/2;
          this.list.grade=(this.p2[3]+this.p1[3])/2;
          console.log(235)
          var _self=this;
          this.$http.post("http://localhost:8989/imsub/MDL/update",this.list).then((response) => {
            _self.ok=response.data
            console.log("ok")
          })
        },
        getid(){
          this.id = this.$route.params.id
        },
        getlist(){
          var _self=this;
          console.log(666)
          this.$http.get("http://localhost:8989/imsub/MDL/findByid?id="+this.id).then((response) => {
            _self.list=response.data
            console.log(_self.list)
          })
        },


      },

    }
</script>

<style scoped>
  .custom-button {
    width: 26px;
    color: #ffffff;
    font-size: 10px;
    line-height: 18px;
    text-align: center;
    background-color: #0a84ee;
    border-radius: 100px;
  }
</style>
