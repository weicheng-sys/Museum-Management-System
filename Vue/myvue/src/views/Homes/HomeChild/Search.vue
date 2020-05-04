<template>
  <div>
    <van-sticky>
     <van-row>
       <van-col span="24">
         <form action="/">
           <van-search
           v-model="keyword"
             show-action
             placeholder="请输入搜索关键词"
             @search="onSearch"
             @cancel="onCancel"
           />
         </form>
       </van-col>
     </van-row>
    </van-sticky>
     <van-list
       v-model="loading"
       :finished="finished"
       finished-text="没有更多了"
       @load="onLoad"
     >
       <van-cell v-for="(item,index) in list" :key="item">
         <van-panel style="position: relative;"  >
           <template #footer>
             <van-image width="100" height="100" :src="list[index].imgsrc"/>
             <span style="position: absolute;top: 5px; font-size: 15px;">
               标题：{{list[index].title| ellipsis}}
             </span>
             <span style="position: absolute;top: 30px; font-size: 15px;">
               来源：{{list[index].source}}
             </span>
             <span style="position: absolute;top: 55px; font-size: 15px;">
               详情：{{list[index].digest | ellipsis}}
             </span>
             <span style="position: absolute;top: 80px; font-size: 15px;">
               时间：{{list[index].time | ellipsis}}
             </span>
           </template>
         </van-panel>
       </van-cell>
     </van-list>


  </div>
</template>

<script>

  import Axios from "axios";					//axios接口引用
export default {
  name: 'Search',
  filters:{
    ellipsis(value){
      if(!value) return ''
      if(value.length>=14){
        return value.slice(0,14) + '...'
      }
      return value
    }
  },
  data(){
    return{
      keyword:'',
      value:'',
      list: [],
      lists:[],
      loading: false,
      finished: false,
  }
  },
  created(){
    this.getParams()
  },
  methods:{
    getParams:function(){
      this.keyword= this.$route.params.keyword
      this.list=this.$route.params.list
      var t = this;
      Axios.get('https://v1.alapi.cn/api/new/toutiao?start=1&num=100').then((res)=>{
        t.lists = res.data.data
        if(t.keyword!=''){
          let lists = t.lists.filter(item=>(item.title.toString().indexOf(t.keyword)>=0||item.digest.toString().indexOf(t.keyword)>=0
        ));
          t.list=lists;
        }
      })
    },
    onSearch(){
      if(this.keyword!=''){
        let lists = this.lists.filter(item=>(item.title.toString().indexOf(this.keyword)>=0||item.digest.toString().indexOf(this.keyword)>=0
        ));
        this.list=lists;
      }
    },
    onCancel(){
      this.$router.push('/')
    },
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
        if (this.list.length >= 0) {
          this.finished = true;
        }
      }, 1000);
    },
  },
  watch:{
    '$route':'getParams'
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
