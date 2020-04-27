<template>

    <van-row>
      <van-col span="24">
        <form action="/">
          <van-search
            v-model="value"
            show-action
            placeholder="请输入搜索关键词"
            @search="onSearch"
          />
        </form>
      </van-col>
    </van-row>

</template>

<script>
export default {
  name: 'Search',
  data() {
      return {
        value: '',
        list:[]
      };
    },
    methods: {
      onSearch(val) {
        var t = this
        this.axios.get('https://v1.alapi.cn/api/new/toutiao?start=1&num=100').then((res)=>{
          t.list=res.data.data

          this.$router.push({name:'search1',
            params:{
            keyword: this.value,
            list:this.list
          }})
        })


      },

    //   goto(){
    //      this.$router.push('/Search1')
    // }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
