<template>
  <div>
    <van-panel >
      <van-row>
        <van-col span="6">
          <img :src="imgs[0].url" v-on:click="toranklists" style="width:100%;height:100%;" />
        </van-col>
        <van-col span="18" style="text-align: left;font-size: 13px">
          <div>1.{{list[0].mname}}<br><br>2.{{list[1].mname}}<br><br>3.{{list[2].mname}}</div>
        </van-col>
      </van-row>
    </van-panel>


    <van-panel >
      <van-row>
        <van-col span="6">
          <img :src="imgs[1].url" v-on:click="toranklists1" style="width:100%;height:100%;" />
        </van-col>
        <van-col span="18" style="text-align: left;font-size: 13px">
          <div>1.{{list1[0].mname}}<br><br>2.{{list1[1].mname}}<br><br>3.{{list1[2].mname}}</div>
        </van-col>
      </van-row>
    </van-panel>

    <van-panel >
      <van-row>
        <van-col span="6">
          <img :src="imgs[2].url" v-on:click="toranklists2"  style="width:100%;height:100%;" />
        </van-col>
        <van-col span="18" style="text-align: left;font-size: 13px">
          <div>1.{{list2[0].mname}}<br><br>2.{{list2[1].mname}}<br><br>3.{{list2[2].mname}}</div>
        </van-col>
      </van-row>
    </van-panel>

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
    name: "RankingList",
    data(){
      return{
        imgs:[

          {url:require("@/assets/rank1.png")},

          {url:require("@/assets/rank2.png")},

          {url:require("@/assets/rank3.png")},

          {url:require("@/assets/test7.png")}
        ],
        list: [{
          basic_info: "['中文名称', '周口店遗址博物馆', '类别', '古人类遗址博物馆', '地点', '北京城西南房山区周口店龙骨山脚下', '竣工时间', '1953年', '所属国家', '中国', '所属城市', '北京市', '适宜游玩季节', '四季皆宜', '景区级别', 'AAAA级', '门票价格', '30.00元', '建议游玩时长', '2小时', '博物馆级别', '国家一级博物馆']",
          evaluate: "环境优美，馆藏丰富。<-$-><-$->陈小松很帅<-$->馆藏丰富",
          grade: "3.17",
          grade_1: 73,
          grade_2: 62,
          grade_3: 61,
          mid: 10,
          mimg: "['https://bkimg.cdn.bcebos.com/pic/622762d0f703918fa6042f87503d269758eec4a1?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'https://bkimg.cdn.bcebos.com/pic/e850352ac65c1038fd0148bfb2119313b07e8954?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1']",
          mname: "周口店遗址博物馆",
          other_info: "['周口店遗址博物馆坐落在北京城西南房山区周口店龙骨山脚下，是一座古人类遗址博物馆，始建于年。年，中国古人类学家裴文中先主在龙骨山发掘出第一颗完整的“北京猿人”头盖骨化石，震撼了全世界。世界文化遗产、国家AAAA级景区、全国重点文物保护单位、全国百家爱国主义教育示范基地。距北京市区约公里。是世界著名的古人类和古脊椎动物考古遗址，是“北京人”的发原地。']",

        },


        ],
        list1: [
          {
            basic_info: "['中文名称', '周口店遗址博物馆', '类别', '古人类遗址博物馆', '地点', '北京城西南房山区周口店龙骨山脚下', '竣工时间', '1953年', '所属国家', '中国', '所属城市', '北京市', '适宜游玩季节', '四季皆宜', '景区级别', 'AAAA级', '门票价格', '30.00元', '建议游玩时长', '2小时', '博物馆级别', '国家一级博物馆']",
            evaluate: "环境优美，馆藏丰富。<-$-><-$->陈小松很帅<-$->馆藏丰富",
            grade: "3.17",
            grade_1: 73,
            grade_2: 62,
            grade_3: 61,
            mid: 10,
            mimg: "['https://bkimg.cdn.bcebos.com/pic/622762d0f703918fa6042f87503d269758eec4a1?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'https://bkimg.cdn.bcebos.com/pic/e850352ac65c1038fd0148bfb2119313b07e8954?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1']",
            mname: "周口店遗址博物馆",
            other_info: "['周口店遗址博物馆坐落在北京城西南房山区周口店龙骨山脚下，是一座古人类遗址博物馆，始建于年。年，中国古人类学家裴文中先主在龙骨山发掘出第一颗完整的“北京猿人”头盖骨化石，震撼了全世界。世界文化遗产、国家AAAA级景区、全国重点文物保护单位、全国百家爱国主义教育示范基地。距北京市区约公里。是世界著名的古人类和古脊椎动物考古遗址，是“北京人”的发原地。']",

          },
        ],
        list2: [
          {
            basic_info: "['中文名称', '周口店遗址博物馆', '类别', '古人类遗址博物馆', '地点', '北京城西南房山区周口店龙骨山脚下', '竣工时间', '1953年', '所属国家', '中国', '所属城市', '北京市', '适宜游玩季节', '四季皆宜', '景区级别', 'AAAA级', '门票价格', '30.00元', '建议游玩时长', '2小时', '博物馆级别', '国家一级博物馆']",
            evaluate: "环境优美，馆藏丰富。<-$-><-$->陈小松很帅<-$->馆藏丰富",
            grade: "3.17",
            grade_1: 73,
            grade_2: 62,
            grade_3: 61,
            mid: 10,
            mimg: "['https://bkimg.cdn.bcebos.com/pic/622762d0f703918fa6042f87503d269758eec4a1?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'https://bkimg.cdn.bcebos.com/pic/e850352ac65c1038fd0148bfb2119313b07e8954?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1']",
            mname: "周口店遗址博物馆",
            other_info: "['周口店遗址博物馆坐落在北京城西南房山区周口店龙骨山脚下，是一座古人类遗址博物馆，始建于年。年，中国古人类学家裴文中先主在龙骨山发掘出第一颗完整的“北京猿人”头盖骨化石，震撼了全世界。世界文化遗产、国家AAAA级景区、全国重点文物保护单位、全国百家爱国主义教育示范基地。距北京市区约公里。是世界著名的古人类和古脊椎动物考古遗址，是“北京人”的发原地。']",

          },
        ],
        list3: [
          {
            basic_info: "['中文名称', '周口店遗址博物馆', '类别', '古人类遗址博物馆', '地点', '北京城西南房山区周口店龙骨山脚下', '竣工时间', '1953年', '所属国家', '中国', '所属城市', '北京市', '适宜游玩季节', '四季皆宜', '景区级别', 'AAAA级', '门票价格', '30.00元', '建议游玩时长', '2小时', '博物馆级别', '国家一级博物馆']",
            evaluate: "环境优美，馆藏丰富。<-$-><-$->陈小松很帅<-$->馆藏丰富",
            grade: "3.17",
            grade_1: 73,
            grade_2: 62,
            grade_3: 61,
            mid: 10,
            mimg: "['https://bkimg.cdn.bcebos.com/pic/622762d0f703918fa6042f87503d269758eec4a1?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'https://bkimg.cdn.bcebos.com/pic/e850352ac65c1038fd0148bfb2119313b07e8954?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1']",
            mname: "周口店遗址博物馆",
            other_info: "['周口店遗址博物馆坐落在北京城西南房山区周口店龙骨山脚下，是一座古人类遗址博物馆，始建于年。年，中国古人类学家裴文中先主在龙骨山发掘出第一颗完整的“北京猿人”头盖骨化石，震撼了全世界。世界文化遗产、国家AAAA级景区、全国重点文物保护单位、全国百家爱国主义教育示范基地。距北京市区约公里。是世界著名的古人类和古脊椎动物考古遗址，是“北京人”的发原地。']",

          },
        ],
        loading: false,
        finished: false,
        ranktitle:'评分',
      }
    },
    created(){
      this.setdata()
    },

    methods:{
      toranklists: function () {
        this.$router.push({name: 'ranklists', params: {list: this.list ,ranktitle: "评分"}})
      },
      toranklists1: function () {
        this.$router.push({name: 'ranklists', params: {list: this.list1 ,ranktitle: "服务"}})

      },
      toranklists2: function () {
        this.$router.push({name: 'ranklists', params: {list: this.list2 ,ranktitle: "展览"}})

      },
      toranklists3: function () {
        this.$router.push({name: 'ranklists', params: {list: this.list3 ,ranktitle: "环境"}})
      },





      setdata:function () {
        var _self=this;

        this.$http.get("http://39.98.108.11:8081/MDL/findBYGrade").then((response) => {
          _self.list=response.data.result
          console.log(_self.list)

        })
        this.$http.get("http://39.98.108.11:8081/MDL/findBYGrade1").then((response) => {
          _self.list1=response.data.result
          console.log(_self.list)

        })
        this.$http.get("http://39.98.108.11:8081/MDL/findBYGrade2").then((response) => {
          _self.list2=response.data.result
          console.log(_self.list)

        })
        this.$http.get("http://39.98.108.11:8081/MDL/findBYGrade2").then((response) => {
          _self.list3=response.data.result
          console.log(_self.list)

        })


      },

    }
  }
</script>

<style scoped>

</style>
