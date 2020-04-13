<template>
  <div id="app">
    <nav>  
　　<ul>
　　　　<li v-for="(item, i) in navData" :class="{ nav_li : active === i }" :key="i" @click="$router.push({ path: item.path }), active = i">
　　　　　　{{item.name}}
　　　　</li>
   </ul> 
</nav>


  个人信息：
   
  <ul class="a">
  <li>头像</li>
  <li>昵称</li>
  <li>性别</li>
</ul>
 
<ul class="b">
  <li>地区</li>
  <li>账号</li>
  <li>个性签名</li>
</ul>

  </div>


</template>


<script>

export default {
  data () {
    return {
      active: 0,
      navData: [
        { name: '1', path: './Mypage'},
        { name: '2', path: '@/Homes/Home'  },
    
      ]
    }
  }

}

</script>


<style>

ul.a {list-style-type:circle;}
ul.b {list-style-type:square;}

/* ul {
        width: 1200px;
        height: 88px;
        line-height: 88px;
        margin: 0 auto;
        background: #3b2d50;
        color: #fff;
        font-size: 18px;
        display: flex;
         justify-content: space-between;
       
       
  }

   li {
                text-align: center;
            }
            .nav_li {
                background-color: #dedede;
                color: #353535;   
            }        */
</style>