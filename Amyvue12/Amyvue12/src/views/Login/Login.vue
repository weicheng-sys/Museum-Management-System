<template>
<div class="login_container">
    <!-- <van-nav-bar title="标题" left-text="返回" right-text="按钮" left-arrow @click-left="onClickLeft" @click-right="onClickRight" />-->

    <div class="login_box">

        <div class="avatar_box">
            <img src="../../assets/museum.jpg">
        </div>

        <van-form @submit="onSubmit">
            <van-field v-model="username" name="username" label="用户名" placeholder="用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
            <van-field v-model="password" type="password" name="password" label="密码" placeholder="密码" :rules="[{ required: true, message: '请填写密码' }]" />
            <div>

                <van-button round block type="info" native-type="submit">
                    提交
                </van-button>
                <br /><br /><br /><br />
                <!--  <van-row type="flex">

                    <van-button round block type="info" native-type="submit">
                        忘记密码
                    </van-button>
                    <van-col span="1">||</van-col>
                    <van-button round block type="info" native-type="submit" to="Register">
                         用户注册
                    </van-button>
                </van-row>-->

            </div>
        </van-form>
    </div>
</div>
</template>

<script>
import Axios from "axios" //axios接口引用
import {
    Toast
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
        onSubmit(values) {

            const _this = this;
            Toast('提交');
            this.username = values.username;
            this.password = values.password;
            Axios.get('http://39.98.108.11:8081/user/login', {
                params: {
                    uname: this.username,
                    upwd: this.password
                }
            }).then(result => {
                Toast(result.data.msg);
                if (result.data.success) {
                    this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
                        _this.$router.push('/Home');
                    });

                }
            });

        }
    },

};
</script>

<style lang="less">
.login_box {
    height: 360px;
    width: 300px;
    background-color: #fff;
    border-radius: 1px 1px;
    position: absolute;
    //    right: 30%;
    top: 300%;
    left: 10%;
    // transform: translate(50%, 80%);
    //     -ms-transform:translate(-50%,-50%);

    .avatar_box {
        height: 90px;
        width: 90px;
        border: 2px solid #eee;
        border-radius: 50%;
        padding: 20px;
        box-shadow: 0 0 3px #ddd;
        margin-left: 27%;
        //text
        // position: absolute;
        // left: 50%;
        // transform: translate(-50%, -100%);
        // background-color: #fff;

        img {
            height: 100%;
            width: 100%;
            border-radius: 50%;
            background-color: #eee;

        }

    }
}
</style>
