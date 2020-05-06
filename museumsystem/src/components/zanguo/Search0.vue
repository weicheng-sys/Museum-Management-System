<template>
  <div>
    <van-row>
      <van-col span="24">
        <form action="/">
          <van-search
            v-model="value"
            show-action
            placeholder="请输入搜索关键词"
            @search="onSearch"
            @cancel="onCancel"
          />
        </form>
      </van-col>
    </van-row>
    <div style="text-align: center;">
      搜索指定内容
    </div>
    <div>
      &nbsp;
    </div>
      <van-row >
        <van-col span="4">&nbsp;</van-col>
        <van-col span="7" style="text-align: center;font-size: 16px;color: blue;" @click="goto1">博物馆</van-col>
        <van-col span="2" style="text-align: center;">|</van-col>
        <van-col span="7" style="text-align: center;font-size: 16px;color: blue" @click="goto2">新闻</van-col>
        <van-col span="4">&nbsp;</van-col>
      </van-row>
  </div>
</template>

<script>
export default {
  name: 'Search0',
  data() {
      return {
        value: '',
        list:[]
      };
    },
    methods: {
      onSearch(val) {
          this.$router.push({name:'search1',
            params:{
            keyword: this.value,
          }})
      },
      onCancel(){
        this.$router.back()
      },
      goto1(){
        this.$router.push('/search1')
      },
      goto2(){
        this.$router.push('/search2')
      }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
