<template>
  <div class="hello">
    <!-- 导航栏 代码省略-->

    <!-- 登录页 用户表单 -->
      <van-cell-group>
        <van-field
          v-model="username"
          clearable
          label="用户名"
          right-icon="question-o"
          placeholder="请输入用户名"
          left-icon="contact"
          @click-right-icon="$toast('用户名必须是手机号')"
        />

        <van-field
          v-model="password"
          clearable
          type="password"
          label="密码"
          right-icon="question-o"
          placeholder="请输入密码"
          left-icon="closed-eye"
          @click-right-icon="$toast('密码必须是数字、字母、下划线')"
        />
        <!--登录按钮-->
        <div class="pd15"><van-button type="primary" size="large" @click="onClickButtonSubmit">登录</van-button></div>
      </van-cell-group>
  </div>
</template>

<script>
import axios from 'axios'
const token = '123456';
  export default {
    name: 'changepassword',
    data () {
      return {
        errors: [],
        username: "",
        password: ""
      }
    },
    methods: {
      onClickRight() {
        this.$toast('请填写注册信息');
        this.$router.push({ path:'/register'});
      },
      // 表单提交
      onClickButtonSubmit: function (e,username,password) {
        if(this.username == ''){
          this.$toast("用户名不能为空");
          return false;
        }
        if(this.password == ''){
          this.$toast("密码不能为空");
          return false;
        }
        else{
              // this.$toast('token='+token);
         	 var that=this // 放置指针，便于then操作的获取

          axios.get('接口地址', {
              params: {
                  userName: this.username
              }
          }).then(function (response) {
              console.log(response);
              var reslutData=response;
              console.log(reslutData.data.status )
              if(reslutData.data.status == 1002){
                  this.$toast(reslutData.data.desc);
              }
              if(reslutData.data.status == 1000){
                  this.$toast(reslutData.data.desc);
                  this.$router.push({
                  path: '/receData',
                  query: {
                    reslutData
                  }
                });
              }
          }.bind(this))
          .catch(function (error) {
              console.log("请求失败"+error);
          });
          e.preventDefault();
        }
      },
      validEmail: function (password) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(password);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bgset{
  background: #50a1e6;}
</style>
