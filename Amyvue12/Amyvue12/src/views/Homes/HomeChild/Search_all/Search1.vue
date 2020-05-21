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
        <van-panel style="position: relative;"  @click='xiang(index)'>
          <template #footer>
            <van-image width="100" height="100" :src="list[index].mimg"/>
            <span style="position: absolute;top: 5px; font-size: 15px;">
               名称：{{list[index].mname}}
             </span>
            <span style="position: absolute;top: 30px; font-size: 15px;">
               基本信息：{{list[index].basic_info | ellipsis }}
             </span>
          </template>
        </van-panel>
      </van-cell>
    </van-list>


  </div>
</template>

<script>

  export default {
    name: 'Search1',

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
      if(to.name === 'mdetails'){
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
        this.$http.get('http://39.98.108.11:8081/MDL/findAll').then((res)=>{
          t.lists = res.data.result
          let l = t.lists.length;
          for(let i=0;i<l;i++){
            let x = t.lists[i].mimg;
            if(x.indexOf('jpg')){
              let y = x.indexOf('jpg')+1
              t.lists[i].mimg = x.substr(2,y);
            }
          }
          if(t.keyword!=''){
            let lists = t.lists.filter(item=>(item.mname.toString().indexOf(t.keyword)>=0||item.basic_info.toString().indexOf(t.keyword)>=0
            ));
            t.list=lists;

          }
        })
      },
      onSearch(){
        if(this.keyword!=''){
          let lists = this.lists.filter(item=>(item.mname.toString().indexOf(this.keyword)>=0||item.basic_info.toString().indexOf(this.keyword)>=0
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
        this.$router.push({name:'mdetails',
          params:{
            id:this.list[index].mid,
          }
        })
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
