<template>
  <div id="app">
    <el-input
      placeholder="请输入内容"
      v-model="input"
      clearable>
    </el-input>

    <el-carousel :interval="4000" type="card" height="100px">
              <el-carousel-item v-for="item in imgs" :key="item.id">
                 <img :src="item.url" class="image">
              </el-carousel-item>
            </el-carousel>

    <first></first>

  </div>
</template>


<script>
  import "mint-ui/lib/style.css"
import First from "@/components/firstpage.vue"
export default {
  name: 'App',
  components: {First},
  data(){
    return{
      input: "12565",
      value: "",
      result: [],

      imgs:[

        {url:require("@/assets/test4.jpg")},

        {url:require("@/assets/test5.jpg")},

        {url:require("@/assets/test6.jpg")}

      ]

    }

  },
  methods:{


  }

}
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 100px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
