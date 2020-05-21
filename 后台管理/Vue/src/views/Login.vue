<template>
    <div class="login">
      <p class="tit">后台管理</p>
      <el-form :model="ruleForm" :rules="rules"  label-width="100px" >
        
        <el-form-item label="账号" prop="uname">
          <el-input v-model="ruleForm.uname" style="width: 75%;"></el-input>
        </el-form-item>
 
        <el-form-item label="密码" prop="upwd">
          <el-input type="password" v-model="ruleForm.upwd" style="width: 75%;"></el-input>
        </el-form-item>

 
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')" style="width:60%;">登录</el-button>
        <!--  <el-button @click="resetForm('ruleForm')">重置</el-button> -->
        </el-form-item>
      </el-form>
    </div>

</template>
 
<script>
 
export default {
   data() {
      return {
        ruleForm: {
        },
        rules: {
          username: [
            { required: true, message: '请输入账号', trigger: 'blur' },
            { min: 5,  message: '长度不少于5', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { min: 5,  message: '长度不少于5', trigger: 'blur' }
          ]
        },
        checked: false
    
      };
    },
    //页面加载调用获取cookie值
    mounted() {
        this.getCookie();
    },
    methods: {
      submitForm(formName) {
        const _this=this
        //console.log(_this.ruleForm.uname)
        _this.axios.get('admin/findByname?uname='+_this.ruleForm.uname)
        .then(function (resp) {

           if(resp.data.upwd==_this.ruleForm.upwd){
               _this.$alert('登录成功', '消息', {
                confirmButtonText: '确定',
                 callback: action => {
                   _this.$router.push({ path:'/museum'})
                 }
               })
             }
             else alert(resp.data.msg)
          })

        // this.$refs[formName].validate((valid) => {
        //  if (valid) {
        //     const self = this;
        //     //判断复选框是否被勾选 勾选则调用配置cookie方法
        //     if (self.checked == true) {
        //         //传入账号名，密码，和保存天数3个参数
        //         self.setCookie(self.ruleForm.username, self.ruleForm.password, 7);
        //     }else {
        //       console.log("清空Cookie");
        //       //清空Cookie
        //       self.clearCookie();
        //   }
        //     alert('登录成功!');
        //     this.$router.push({ path:'/museum',params:{user:self.ruleForm.username,pwd:self.ruleForm.password}});
        //   } else {
        //     console.log('error submit!!');
        //     return false;
        //   }
        // });
      },

      resetForm(formName) {
        this.$refs[formName].resetFields();
      },

      //设置cookie
      setCookie(c_name, c_pwd, exdays) {
          var exdate = new Date(); //获取时间
          exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays); //保存的天数
          //字符串拼接cookie
          window.document.cookie = "userName" + "=" + c_name + ";path=/;expires=" + exdate.toGMTString();
          window.document.cookie = "password" + "=" + c_pwd + ";path=/;expires=" + exdate.toGMTString();
      },
      //读取cookie
      getCookie: function() {
          if (document.cookie.length > 0) {
              var arr = document.cookie.split('; '); //这里显示的格式需要切割一下自己可输出看下
              for (var i = 0; i < arr.length; i++) {
                  var arr2 = arr[i].split('='); //再次切割
                  //判断查找相对应的值
                  if (arr2[0] == 'userName') {
                    //  console.log(arr2[1])
                      this.ruleForm.username = arr2[1]; //保存到保存数据的地方
                  } else if (arr2[0] == 'password') {
                    // console.log(arr2[1])
                      this.ruleForm.password = arr2[1];
                  }
              }
               this.checked = true;
          }
      },
      //清除cookie
      clearCookie: function() {
          this.setCookie("", "", -1); //修改2值都为空，天数为负1天就好了
      }
    }
  }


</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login{
  background-color: rgb(102,249,207,.8);
  border-radius: 25px;
  width: 25%;
  height: 75%;
  position:absolute;
  margin: 50px 500px ;
}
.tit{
  font-family: STXinwei;
  font-size: 50px;
  text-align: center;
}
.lf{
  float: left;
}
.box{
  min-width: 350px;
  margin-left:50px; 
  width: 30%;
}
.rf{
  float:right;
}
.clearfix:after {
  content:"."; 
  display:block; 
  height:0; 
  visibility:hidden; 
  clear:both; 
}
.clearfix { 
  *zoom:1; 
}
</style>