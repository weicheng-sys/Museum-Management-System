<template>
  <div v-cloak>
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

       <van-cell v-for="(item,index) in list" :key="index" >
         <van-panel  @click='xiang(index)'>
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


  </div>
</template>

<script>

export default {
  name: 'Search2',

  filters:{
    ellipsis(value){
      if(!value) return ''
      if(value.length>=30){
        return value.slice(0,30) + '...'
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
      scroll: null,

  }
  },
  beforeRouteEnter: (to,from,next) => {
    if(to.name === 'newsdl'){
      from.meta.keepAlive = true;
    }else{
      from.meta.keepAlive = false;
    }
    next(vm=>{
      vm.getParams();
    });
  },
  methods:{
    getParams:function(){
      if(this.$route.params.keyword)
      this.keyword= this.$route.params.keyword
      var t = this
      this.axios.get('http://localhost:8989/imsub/News/findAll').then((res)=>{
        t.lists = res.data.result
        if(t.keyword!=''){
          let lists = t.lists.filter(item=>(item.title.toString().indexOf(t.keyword)>=0||item.content.toString().indexOf(t.keyword)>=0
            ||item.mname.toString().indexOf(t.keyword)>=0
        ));
          t.list=lists;
        }
      })
    },
    onSearch(){
      if(this.keyword!=''){
        let lists = this.lists.filter(item=>(item.title.toString().indexOf(this.keyword)>=0||item.content.toString().indexOf(this.keyword)>=0
        ));
        this.list=lists;
      }
      window.scrollTo(0,0)
    },
    onCancel(){
      this.$router.back()
    },
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
        window.scrollTo(100,this.x)
      }, 1000);
    },
    xiang:function(index){
      this.$router.push({name:'newsdl',
                      params:{
                        id:this.list[index].nid,
                      }
                    })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
