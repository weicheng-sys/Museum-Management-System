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
      <p class="tle">{{list.title}}</p><br>
      <p style="text-align: right;font-size: 12px;height: 12px">{{list.mname}} </p>
      <van-swipe  :autoplay="3000" indicator-color="white" style="height: 200px;">
        <van-swipe-item v-for="(item, index) in list.nimg" :key="index">
          <img :src=item style="width:100%;height:200px;" />
        </van-swipe-item>
      </van-swipe>
      <div style=" padding: 30px;">
        <div  v-for="item in splittext(this.changeLine(this.list.content))" >
          <p  class="maintext" v-html="item" ></p>
        </div>
      </div>


      <p style="text-align: right;font-size: 14px">{{list.ntime}}<br>{{list.publisher}}<br>{{list.source}}</p>



    </div>
</template>

<script>
    export default {
        name: "newsdl",
      data(){
       return{
         list:{
                },
         id: 1,
         conlist:[],

      }
      },
      created() {
          this.getid();
          this.getlist();

      },

      methods:{
        back(){this.$router.back()},
        changeLine(str){
          return str.replace(/\n|\r\n/g,"<br/>");
        },
        splittext(text){
          return text.split("<br/>");
        },
        getid(){
          this.id = this.$route.params.id;
          console.log(2266)
          console.log(this.id)
        },
        getlist(){
          var _self=this;
          console.log(222)
          this.$http.get("http://localhost:8989/imsub/News/findByid?id="+this.id).then((response) => {
            _self.list=response.data
            console.log(_self.list)

          })
        },
      }

    }
</script>

<style scoped>
  .tle{
      font-weight:bold;
      font-weight:800;
      font-size: 20px;
      height: 15px;
  }
  .maintext{
    text-align: left;
    white-space: pre-wrap;
    text-indent: 2em;
    line-height: 1.8em;


  }

</style>
