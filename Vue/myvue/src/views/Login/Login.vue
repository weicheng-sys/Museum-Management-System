<template>
<div class="login_container">
    <!-- <van-nav-bar title="标题" left-text="返回" right-text="按钮" left-arrow @click-left="onClickLeft" @click-right="onClickRight" />-->

    <div class="login_box">

        <div class="avatar_box">
            <img src="../../assets/logo.png">
        </div>
        <van-form @submit="onSubmit">
            <van-field v-model="username" name="username" label="用户名" placeholder="用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
            <van-field v-model="password" type="password" name="password" label="密码" placeholder="密码" :rules="[{ required: true, message: '请填写密码' }]" />
            <div style="margin: 16px;">

                <van-button round block type="info" native-type="submit">
                    提交
                </van-button>
                <br /><br /><br /><br />
                <van-row type="flex">

                    <van-button round block type="info" native-type="submit">
                        忘记密码
                    </van-button>
                    <van-col span="1">||</van-col>
                    <van-button round block type="info" native-type="submit" to="Register">
                         用户注册
                    </van-button>
                </van-row>
            </div>
        </van-form>
    </div>
</div>
</template>

<script>
import Axios from "axios" //axios接口引用
import {Toast
} from 'vant';

export default {
    name: "login",
    data() {
        return {
            msg: '注册页面',
            username: '',
            password: '',
            userErr: '用户名不能为空',
            passErr: '密码不能为空',
            user: {
                id: '123',
                name: '',
                password: '',
            }

        };
    },

    methods: {

        // resetloginref(){
        //   //  console.log(this);

        // this.$refs.loginref.resetValidation();
        // },

        //         onClickLeft() {
        //             this.$router.go(-1);
        //             Toast('返回');
        //         },
        //         onClickRight() {
        //             Toast('按钮');
        //         },

        onSubmit(values) {
            //             HttpServletRequest request;
            // HttpSession session = request.getSession();
            //             console.log("session"+session.getAttribute("user"));

            const _this = this;
            Toast('提交');
            console.log('submit', values);
            this.username = values.username;
            this.password = values.password;

            console.log('this', this.username, this.password);
            // Axios.get('http://localhost:8089/user/login?uname='this.username+'&upwd='+this.password).then(result=>{
            //       console.log(result)
            //       }),
            Axios.get('http://localhost:8089/user/login', {
                params: {
                    uname: this.username,
                    upwd: this.password
                }
            }).then(result => {
                Toast(result.data.msg);
                console.log(result.data.success);
                console.log(JSON.stringify(result.data));

                if (result.data.success) {
                    this.$axios.get('http://localhost:8089/user/findAll').then((results) => {
                        console.log("findAll" + JSON.stringify(results.data));
                        console.log("findAll" + results.data.msg);

                        _this.$router.push('/Home');
                    });

                }
                console.log(result.data.msg);
            });

        }
    },

};

// Axios.post('http://localhost:8089/user/create',this.user).then(function (response){

// }
// )
//     Axios.get('http://localhost:8089/user/findbyuname', {
//               params: {
//                   userName: values.username
//               }
//           }).then(function (response) {

//             //response.data[0].uname--findAll
//             //response.data.uname--findbyuname

//               console.log("hahah"+response.count);
//               console.log("hahah"+response.data.uid);
//               console.log("hahah"+response.data.uname);

//               if(values.username==response.data.uname)
//               {
//                 if(values.password!=response.data.upwd)
//                       console.log("密码错误"+response.data.upwd);
//                       else console.log("密码正确"+response.data.upwd);
//               }

//               var reslutData=response;
//               console.log("what?"+reslutData.data.status)
//               if(reslutData.data.status == 1002){
//                   this.$toast(reslutData.data.desc);
//               }
//               if(reslutData.data.status == 1000){
//                   this.$toast(reslutData.data.desc);
//                   this.$router.push({
//                   path: '/',
//                   query: {
//                     reslutData
//                   }
//                 });
//               }}.bind(this))
//           .catch(function (error) {
//               console.log("请求失败"+error);
//           });

//在这里调用网络请求
// request(){
//  Axios.get('http://localhost:8086/user/findAll').then(result=>{
//   console.log(result)
// })
// },

// // 回到上一步
//  goBackFn(){
//     this.$router.go(-1);
// },
</script>

<style lang="less">
// .login_container{
//     background-color:#2b4b6b;
//     height:100%;
// }

.login_box {
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 1px 1px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, 80%);
    // -ms-transform:translate(-50%,-50%);

    .avatar_box {
        height: 130px;
        width: 130px;
        border: 1px solid #eee;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 0 10px #ddd;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -100%);
        background-color: #fff;

        img {
            height: 100%;
            width: 100%;
            border-radius: 50%;
            background-color: #eee;

        }

    }
}
</style>
