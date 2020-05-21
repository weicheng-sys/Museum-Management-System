<template>
<div id="app">

    <van-nav-bar title="修改" left-text="个人信息" left-arrow @click-left="onClickLeft" />

    <van-uploader class="icon" multiple :accept="'image/*'" :preview-size="30" :deletable="false" :before-read="beforeRead" :after-read="afterRead">

        <van-image class="img-avatar" round width="8rem" height="8rem" :src="user.icon" />
    </van-uploader>

    <div class="change">
        <van-cell title="用户名" is-link to="Change_name" v-model="user.uname" />
        <van-cell title="性别" is-link to="Change_gender" v-model="user.gender" />
        <van-cell title="修改密码" is-link to="Change_password" v-model="user.upwd" />
        <van-cell title="电话号码" is-link to="Change_phone" v-model="user.phone" />
        <van-cell title="个人简介" is-link to="Change_introduction" v-model="user.introduction" />
    </div>
    <van-button round block type="info" native-type="submit" @click="logout">
        注销
    </van-button>

</div>
</template>

<script>
import {
    Toast
} from 'vant';
import Axios from "axios" //axios接口引用
export default {
    data() {
        return {
            user: {
                uid: '',
                gender: '',
                uname: '',
                phone: '',
                upwd: '',
                icon: require('@/assets/user.jpg'),
                introduction: '',
            },
            filelist: [],
            avatar: 'https://img.yzcdn.cn/vant/cat.jpeg',
            active: 0,

        }
    },
    mounted() {
        this.getuser();
    },
    methods: {
        getuser() {
            const _this = this;
            this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
             
                _this.user.uname = results.data.results.uname;
                _this.user.uid = results.data.results.uid;
                _this.user.gender = results.data.results.gender;
                _this.user.upwd = results.data.results.upwd;
                _this.user.phone = results.data.results.phone;

                _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;

                _this.user.introduction = results.data.results.introduction;

                Toast(results.data.results.uname);

            });

        },
        logout() {
            Axios.get('http://39.98.108.11:8081/user/logout').then(result => {
                this.$router.push('/Login_and_Register');
            });
        },
        onClickLeft() {
            Toast('返回我的页面');
            this.$router.push('/Mypage');
        },

        changeImage(e) {
            const file = e.target.files[0];
            const reader = new FileReader();
            const that = this;
            reader.readAsDataURL(file);
            reader.onload = function () {
                that.avatar = this.result;
            };
        },
        beforeRead(file) {
            const _this = this;
            let formData = new FormData(); // 为上传文件定义一个formData对象
            let config = {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            };

            var blob = new Blob([file]); // 文件转化成二进制文件
            let uploadUrl = URL.createObjectURL(blob); //转化成url

            Toast('上传文件！')
            // 这里使用foreach是为了将选中的多个文件都添加进定义的formdata变量中           

            formData.append("fileName", file);

            Axios.post('http://39.98.108.11:8081/video/uploadFile', formData, config).then(results => {
                // //上传成功，存入video表！
                if (results.data.success == true) {
                    _this.user.icon = results.data.fileUrl;

                    this.$axios.put("http://39.98.108.11:8081/user/update", _this.user).then((res) => {

                        if (res.data.success == true) {
                            this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
                               
                                _this.user.uname = results.data.results.uname;
                                _this.user.uid = results.data.results.uid;
                                _this.user.gender = results.data.results.gender;
                                _this.user.upwd = results.data.results.upwd;
                                _this.user.phone = results.data.results.phone;

                                _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;

                                _this.user.introduction = results.data.results.introduction;

                                Toast(results.data.results.uname);

                            });
                        }

                    });

                }
                //this.fileIdArr = res.data.data;  // 把選中的文件傳送給後台
            }).catch(err => {
                Toast('文件上傳失敗！')
            });

        },
    },

}
</script>

<style>
ul.a {
    list-style-type: circle;
}

ul.b {
    list-style-type: square;
}

.img-avatar {
    width: 5rem;
    height: 5rem
}

.icon {
    padding: 2%;
    display: flex;
    justify-content: center;
}

.change {
    padding: 5%;
}
</style>
