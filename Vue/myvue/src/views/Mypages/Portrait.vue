<template>
<div id="app">

    <van-nav-bar title="标题" left-text="个人信息" right-text="按钮" left-arrow @click-left="onClickLeft" />

    <li @change="changeImage($event)">
        <van-uploader multiple :accept="'image/*'" :preview-size="30" :deletable="false" :after-read="afterRead">
            <span>头像</span>
            <img :src="user.icon" class="img-avatar" round />
            <van-icon name="arrow" />
        </van-uploader>
    </li>

    <van-cell title="头像" right-icon='https://img.yzcdn.cn/vant/cat.jpeg' is-link url="/vant/mobile.html" v-model="user.icon" />


    <van-cell title="账号" v-model="user.uid"/>
    <van-cell title="用户名" is-link to="Change_name" v-model="user.uname"/>
    <van-cell title="性别" is-link to="Change_gender"  v-model="user.gender"/>
    <van-cell title="修改密码" is-link to="Change_password" v-model="user.upwd"/>
    <van-cell title="电话号码" is-link to="Change_phone" v-model="user.phone"/>
    <van-cell title="个人简介" is-link to="Change_introduction" v-model="user.introduction"/>
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
            user:{
                uid:'',
                gender:'',
                uname:'',
                phone:'',
                upwd:'',
                icon:'https://img.yzcdn.cn/vant/cat.jpeg',
                introduction:'',
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
        getuser(){
            const _this=this;
            this.$axios.get('http://localhost:8089/user/findAll').then((results)=>{
            console.log("findAll"+JSON.stringify(results.data));
            console.log("findAll"+results.data.msg);
            _this.user.uname=results.data.results.uname;
            _this.user.uid=results.data.results.uid;
            if(results.data.results.gender==0)
            _this.user.gender='女';
            else{ _this.user.gender='男'}
            _this.user.upwd=results.data.results.upwd;
            _this.user.phone=results.data.results.phone;
            _this.user.icon=results.data.results.icon;
            _this.user.introduction=results.data.results.introduction;
          //  _this.user.uid=results.data.results.uname;
            Toast(results.data.results.uname);

        });

        },
        logout(){
    Axios.get('http://localhost:8089/user/logout').then(result=>{
      console.log(result);
       //this.$router.push('/'+result.data);
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

        afterRead(file) {
            //文件读取完成后的回调函数
            let content = file.file;
            //创建一个新的FormData
            let formData = new FormData();
            // upload这个名字是后台给的
            formData.append("upload", content);
            //获取formdata表单所有的数据
            console.log(formData.getAll(""));
            // axios
            //   .post(
            //服务器上传地址
            //     `http://xxxxxxxxxxxx`,
            //服务器需要的数据，此处是formdata表单
            //     formData,
            //如果默认请求头是json，需要改一下请求头数据格式
            //     {
            //       "Content-Type": "multipart/form-data"
            //     }
            //   )
            //   .then(res => {
            //     console.log(res);
            //     console.log(res.config.headers);
            //   });

            // axios({
            //   method: "post",
            //   //服务器上传地址
            //   url: `http://xxxxxxxxxxxxxxxxxxxxxxxxxxx`,
            //   data: formData,
            //   headers: {
            //     // 修改请求头
            //     "Content-Type": "multipart/form-data"
            //   }
            // }).then(res => {
            //   console.log(res);
            //   console.log(res.config.headers);
            // });
        }

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
