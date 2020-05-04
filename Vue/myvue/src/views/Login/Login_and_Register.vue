<template>
<div class='login'>

 <van-tabs v-model="active" >
    <van-tab title="登录" name="登录">
        <Login></Login>
      </van-tab>

      <van-tab title="注册"  name="注册" >
        <Register></Register>
      </van-tab>

    </van-tabs>


</div>
</template>
   
<script>
import Login from './Login.vue'
import Register from './Register.vue'


export default {
    name: "login_and_Register",
    components:{Login,Register},
}
</script>

<style>
.login{
    background-color:#2b4b6b;
    height:100%; 
}
</style>