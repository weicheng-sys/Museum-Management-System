<template>
  <div id="app">
  <Header></Header>



<div class="topnav">
  <a href="#/Portrait">修改用户个人资料</a>
  <a href="#/">链接2</a>
  <a href="#/">链接3</a>
</div>
  <br>


  <!-- <router-link to="/Portrait">用户头像</router-link>
  <router-view/> -->

  <br>
  <br>
  <br>
  <br>作品   动态  收藏
  <br>
  <br>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>
</template>


<script>

import Header from '../../components/header/Header'
export default {
    data(){
      return {
          books:[]
      }
    },
   created() {
      const _this=this
      axios.get('http://localhost:8181/book/findAll/'+currentPage).then(function (resp) {
          _this.books=resp.data

      })
   }

}
</script>


<style>

/* 导航条 */
.topnav {
  overflow: hidden;
  background-color: rgb(30, 209, 200);
}

/* div
{
    box-sizing:border-box;
    -moz-box-sizing:border-box;
    width:90%;
    height: 90%;
} */

</style>
