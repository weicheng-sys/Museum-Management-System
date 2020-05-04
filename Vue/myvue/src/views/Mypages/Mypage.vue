<template>
<div id="app">

 <div style="text-align: center;margin-top: 50px">
            <form action="http://localhost:8083/uploadFile" method="post" enctype="multipart/form-data">
            <p><input type="file" name="fileName"/></p>
            <p><input type="submit" value="上传视频或图片"/></p>
        </form>
     <!-- <P th:text="${msg}"></P>
        <p th:text="${fileUrl}"></p>
        <img th:src="@{${fileUrl}}" th:alt="${msg}">-->
       
    </div>

    <!-- <Header></Header> -->
    <van-row type="flex">
        <van-col span="1"></van-col>
        <van-image class="image" @click="click_image" round width="5rem" height="5rem" :src="user.icon" />
        <van-cell v-model="user.uname"  is-link url="/#/Portrait" />
    </van-row>

    <van-cell title="视频？" is-link to="/" icon="location-o" />

    <van-cell title="收藏？" is-link to="/" icon="location-o" />

    <div class="upload">
        <div>
            <div class="forPreview_video" v-for="(item, index) in uploadVideoList" :key="index">
                <!--<video :src="videoSrc"></video>-->
                <div class='videos'>
                    <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions"></video-player>
                </div>
                <van-icon name="delete" @click="delBtn(index)" class="delte" />
            </div>
            <van-uploader v-show="true" preview-size="80px" accept="video/*" :before-read="beforeRead" :after-read="afterRead"></van-uploader>
        </div>
    </div>

    <div class="diy-submit">
        <van-button @click="doSubmit($event)">提交</van-button>
    </div>

    <div class='rowx'>
        <van-col span="1"></van-col>
        <div class='video1'>
            <div class='videos'>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions"></video-player>

            </div>
        </div>
        <van-col span="1"></van-col>
        <div class='video1'>
            <div class='videos'>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions1"></video-player>

            </div>
        </div>

        <van-col span="1"></van-col>
        <div class='video1'>
            <div class='videos'>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions1"></video-player>

            </div>
        </div>

        <van-col span="1"></van-col>
        <div class='video1'>
            <div class='videos'>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions1"></video-player>

            </div>
        </div>
        <van-col span="1"></van-col>
        <div class='video1'>
            <div class='videos'>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions1"></video-player>

            </div>
        </div>

    </div>
    <table>
        <tr v-for="item in museums">
            <td>{{item.id}}</td>
            <td>{{item.mname}}</td>
            <td>{{item.mlocation}}</td>
            <td>{{item.other}}</td>
        </tr>
    </table>



</div>
</template>

<script>
import Header from '../../components/header/Header'
import Axios from "axios" //axios接口引用
import {
    Toast
} from 'vant';
export default {
    data() {
        return {
            msg: "周梦仔！！！",
            video:{
              
                uid:'13',
                mid:'109',
                vname:'计科1702班会视频',
                vaddr:'urlxxxxxx',
                vinfo:'这是一个关于博物馆的神奇的视频！',
                status:0,
            },
            user:{
              uname:'',
              uid:'',
              icon:'',
            },
            museums: [
                // {
                //   ID:0,
                //   MNAME:"周梦",
                //   MLOCATION:"连云港",
                //   OTHER:"晒"
                // },
            ],

            tagList: [],
            uploadTitle: '',
            currentTag: null,
            tagId: null,
            columnName: localStorage.getItem('columnName'),
            fileIdArr: [],

            uploadVideoList: ['https://vdept.bdstatic.com/6833426778694556337176476846564c/42516635444a6b47/0f148546f324ec61619901fd8103c729fc287819e4718e5e2dc4c377790f0e5accf4dcc0f285451b944b789667975f172a9656cbd626862223f5aebaec68bf25.mp4?auth_key=1587961687-0-0-0783afa09d0b756f9e58688e5c0217b1'], // 选中的上传视频列表
            videoSrc: 'https://vdept.bdstatic.com/6833426778694556337176476846564c/42516635444a6b47/0f148546f324ec61619901fd8103c729fc287819e4718e5e2dc4c377790f0e5accf4dcc0f285451b944b789667975f172a9656cbd626862223f5aebaec68bf25.mp4?auth_key=1587961687-0-0-0783afa09d0b756f9e58688e5c0217b1', // 选中的视频的src，用来显示视频

            playerOptions: {
                playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 默认情况下将会消除任何音频。
                loop: false, // 导致视频一结束就重新开始。
                preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: 'zh-CN',
                aspectRatio: '4:3', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: [{

                    src: 'https://vdept.bdstatic.com/467a5961565852457857676549726b4e/726e4b417878327a/9c480314075d690396aa95e2d4f73dc5191d0ceb8b1fe0efa858ea1b0d68fb26c01f4b3244f6153a098b66c3bee4e15e.mp4?auth_key=1587981082-0-0-43336b41eaac589167cd431289fde71d', // 路径
                    // type: 'video'  // 类型
                }, {
                    src: 'https://vdept.bdstatic.com/6833426778694556337176476846564c/42516635444a6b47/0f148546f324ec61619901fd8103c729fc287819e4718e5e2dc4c377790f0e5accf4dcc0f285451b944b789667975f172a9656cbd626862223f5aebaec68bf25.mp4?auth_key=1587961687-0-0-0783afa09d0b756f9e58688e5c0217b1',
                    // type: 'video/webm' 
                }],
                poster: "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1587954181&di=3468923acf01d6e335055699dfebefc1&src=http://image.zp365.com/news/2020/3/64996729615082.png", //你的封面地址
                // width: document.documentElement.clientWidth,
                notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                controlBar: {
                    timeDivider: true,
                    durationDisplay: true,
                    remainingTimeDisplay: false,
                    fullscreenToggle: true //全屏按钮
                }
            },

            playerOptions1: {
                playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 默认情况下将会消除任何音频。
                loop: false, // 导致视频一结束就重新开始。
                preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: 'zh-CN',
                aspectRatio: '4:3', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: [{

                    src: 'https://vdept.bdstatic.com/467a5961565852457857676549726b4e/726e4b417878327a/9c480314075d690396aa95e2d4f73dc5191d0ceb8b1fe0efa858ea1b0d68fb26c01f4b3244f6153a098b66c3bee4e15e.mp4?auth_key=1587981082-0-0-43336b41eaac589167cd431289fde71d', // 路径
                    // type: 'video'  // 类型
                // }, 
                // {
                //     src: 'https://vdept.bdstatic.com/6833426778694556337176476846564c/42516635444a6b47/0f148546f324ec61619901fd8103c729fc287819e4718e5e2dc4c377790f0e5accf4dcc0f285451b944b789667975f172a9656cbd626862223f5aebaec68bf25.mp4?auth_key=1587961687-0-0-0783afa09d0b756f9e58688e5c0217b1',
                //     // type: 'video/webm' 
                // 
                }
                ],
                poster: "https://pic.rmb.bdstatic.com/75b13b3bb936d253e22c1988e280e2e3.jpeg@s_0,w_800,h_1000,q_80", //你的封面地址
                // width: 10,
                notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                controlBar: {
                    timeDivider: true,
                    durationDisplay: true,
                    remainingTimeDisplay: false,
                    fullscreenToggle: true //全屏按钮
                }
            }
        }

    },

    filters: {
        formatSize(val) { // 格式化文件大小
            if (val > 0) {
                return (val / 1024 / 1024).toFixed(2) + 'M';
            } else {
                return '0M';
            }
        },
    },
    mounted(){
       
        this.createcode()
    },
    methods: {
         createcode(){
             const _this=this;
            _this.$axios.get('http://localhost:8089/user/findAll').then((results)=>{
            console.log("findAll"+JSON.stringify(results.data));
    console.log("findAll"+results.data.msg);
    _this.video.uid=results.data.results.uid;
    _this.user.uname=results.data.results.uname;
     _this.user.icon=results.data.results.icon;
  Toast(results.data.results.uname);
});

// _this.$axios.get('http://localhost:8089/museum/findSession').then((results)=>{
//  _this.video.mid=results.data.results.mid;

// });



         },
        // vant上传文件前校验文件事件
        // 文件选中后先提交给后台，后台根据选中的文件，返回数组（这一业务根据后台而定）
        beforeRead(file) {
            const _this=this;
            let formData = new FormData(); // 为上传文件定义一个formData对象
            let config = {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            };

            var blob = new Blob([file]); // 文件转化成二进制文件
            let uploadUrl = URL.createObjectURL(blob); //转化成url

            console.log("file" +JSON.stringify(file) );
            console.log("url" + URL.createObjectURL(file));
            // let uploadUrl = URL.createObjectURL(file); // 将选中的上传文件转化为二进制文件，显示在页面上
            // console.log(file);
            // if(this.columnName === '视频'){
            this.uploadVideoList.push(file);
            this.videoSrc = uploadUrl;
            this.playerOptions.sources[0].src = uploadUrl;
            console.log(uploadUrl);
            Toast(uploadUrl);
            Toast('上传文件！')
            // 这里使用foreach是为了将选中的多个文件都添加进定义的formdata变量中
            // this.uploadVideoList.forEach(item => {
            //   formData.append(item.name, item)
            // })

            formData.append("fileName", file);
            formData.append("video",_this.video);
            // }

            //  this.$api.post(uploadFile, formData, config).then(res => {
            //   this.fileIdArr = res.data.data;  // 把選中的文件傳送給後台
            // }).catch(err => {
            //   Toast('文件上傳失敗！')
            // })
              Axios.get('http://localhost:8089/upload').then((results)=>{
                 console.log(results);
                 
              });
           Axios.post('http://localhost:8089/video/uploadFile',formData,config).then(results=>{
console.log(formData);
                 
                console.log("result"+JSON.stringify(results));
               

//上传成功，存入video表！
                if(results.data.success==true)
                {
                _this.video.url=results.data.fileUrl;
                 Axios.post('http://localhost:8089/video/add',_this.video).then((results)=>{
                 console.log(JSON.stringify(results));






                 });





                }
 //this.fileIdArr = res.data.data;  // 把選中的文件傳送給後台
            }).catch(err => {
              Toast('文件上傳失敗！')
            });


        //    });
        },

        // 删除待上传的文件
        delBtn(index) {

            // 先判断当前的选中的索引是否是在有效范围中，如果不是则跳出方法 
            if (isNaN(index) || index >= this.uploadVideoList.length) {
                return false;
            }
            let tmp = [];
            // 将没被选中的上传文件存放进一个临时数组中
            for (let i = 0; i < this.uploadVideoList.length; i++) {
                if (this.uploadVideoList[i] !== this.uploadVideoList[index]) {
                    tmp.push(this.uploadVideoList[i]);
                }
            }
            // 存放当前未被选中的上传文件
            this.uploadVideoList = tmp;
        },

        click_image() {
            Toast('进入个人信息页面');
            this.$router.push('/Portrait');

        },
        doSubmit() {
            let params = {
                classify: this.tagId, // 针对视频资源时对应的分类id
                file: this.fileIdArr, // 选择完文件后，调用uploadFile这个接口，后端返回的数组
                resourceColumnId: JSON.parse(localStorage.getItem('columnId')), // 资源栏目id(视频、图片、音频、文档)
                title: this.uploadTitle // 上传时填写的标题
            };
            let columnName = localStorage.getItem('columnName')
            this.$api.post(addResources, params).then(res => {
                if (res.data.code === 1001) {
                    if (columnName === '视频') {
                        this.$router.push({
                            name: 'myVideo'
                        });
                    } else {
                        this.$router.push({
                            name: 'myResourceClassify'
                        });
                    }
                }
            }).catch(err => {
                console.log(err)
            })
        },

    },
    components: {
        Header
    },

    created() {
        // const _this = this
        // Axios.get('http://localhost:8086/museum/findAll').then(function (resp) {
        //     _this.museums = resp.data
        //     console.log(resp.data[0])

        // })
    }

}
</script>

<style>
/* 导航条 */
.topnav {
    overflow: hidden;
    background-color: rgb(30, 209, 200);
}

.image {
    padding: 5px 5px
}

/* div
{
    box-sizing:border-box;
    -moz-box-sizing:border-box;
    width:90%;
    height: 90%;
} */
.video-js.vjs-big-play-button {}

.videos {
    width: 100%;
    height: 100%;
    padding: 0px 0px 0px 0px;
}

.video1 {
    width: 28%;
    height: 20%;
    padding-top: 4px
}

.rowx {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
</style>
