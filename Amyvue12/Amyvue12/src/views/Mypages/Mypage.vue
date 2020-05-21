<template>
  <div id="app">
    <van-nav-bar title="我的" />

    <van-row type="flex">
      <van-col span="1"></van-col>
      <van-image class="image" @click="click_image0" round width="5rem" height="5rem" :src="user.icon" />
      <van-cell :title="user.uname" is-link to="/Portrait" :label="user.introduction" clasa="user" />
    </van-row>

    <van-cell title="视频" />

    <div class="upload">

      <div v-for="(item, index) in uploadVideoList" :key="index">

        <div style="font-size:xx-large;">{{index}}</div>
        <div class="video_list">

          <van-row type="flex">
            <van-image @click="click_image(index)" round width="5rem" height="5rem" :src="item.mimg" />
            <van-cell class="vinfo" :title="item.mname" :value="videoList[index].vname" />
            <van-icon name="delete" @click="delBtn(index)" class="delete" />
          </van-row>

          <van-cell class="vinfo" :title="videoList[index].vinfo" />

          <div class='videos'>
            <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions[index]"></video-player>
          </div>
        </div>
      </div>

    </div>

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
        id: 0,
        url: '',
        videoList: [],

        video: {

          uid: '13',
          mid: '109',
          vname: '中国博物馆的视频',
          vaddr: '',
          vinfo: '我爱中国！',
          status: 0,
        },
        user: {
          uname: '',
          uid: '',
          icon: '',
          introduction: '',
        },
        museums: {
          mid: '',
        },

        tagList: [],
        uploadTitle: '',
        currentTag: null,
        tagId: null,
        columnName: localStorage.getItem('columnName'),
        fileIdArr: [],

        uploadVideoList: [], // 选中的上传视频列表

        playerOptions: [],

      }

    },
    mounted() {
      this.createcode()
    },
    methods: {
      createcode() {
        //  var blob = new Blob(['C://fileupload//src//main//resources//files//video//20200504200811_30e19dfc2f91cd05f058643be98dc7b5.mp4']); // 文件转化成二进制文件
        // let uploadUrl = URL.createObjectURL(blob); //转化成url

        const _this = this;
        //找到当前登陆的用户！！！！！
        _this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {

          //video.uid存储
          _this.video.uid = results.data.results.uid;
          _this.user.uname = results.data.results.uname;
          _this.user.introduction = results.data.results.introduction;
          if (results.data.results.icon == null) {
            _this.user.icon = require('@/assets/user.jpg');
          } else {

            if (results.data.results.icon.substring(0, 1) == '/') {

              _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;

            } else {
              _this.user.icon = results.data.results.icon;
            }
          }

          //根据用户uid得到全部的用户所拍的视频列表！
          _this.$axios.get('http://39.98.108.11:8081/video/findByuid?uid=' + _this.video.uid).then((results) => {

            results.data.results.forEach((e, i) => {

              var url = e.vaddr;
              url = url.substring(0, url.length);
              var urls = 'http://39.98.108.11:8081/files' + url;
              var option = {
                playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 默认情况下将会消除任何音频。
                loop: false, // 导致视频一结束就重新开始。
                preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: 'zh-CN',
                aspectRatio: '4:3', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: {
                  src: 'http://39.98.108.11:8081/files' + url,
                  type: 'video/mp4', // 类型
                  type: "video/ogg",
                  type: "video/webm",

                },
                poster: "", //你的封面地址

                notSupportedMessage: '视频格式不支持，无法上传或者播放！', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                controlBar: {
                  timeDivider: true,
                  durationDisplay: true,
                  remainingTimeDisplay: false,
                  fullscreenToggle: true //全屏按钮
                }
              };

              this.$axios.get('http://39.98.108.11:8081/museum/findBymid?mid=' + e.mid).then((results) => {

                _this.museums = results.data.results;
                let x = results.data.results.mimg;
                if (x.indexOf('jpg')) {
                  let y = x.indexOf('jpg') + 1
                  results.data.results.mimg = x.substr(2, y);
                  option.poster=results.data.results.mimg;
                }

                _this.uploadVideoList.push(_this.museums);

                _this.videoList.push(e);
                if (e.status == 0) {
                  option.poster = require('@/assets/unreviewed.jpg');
                } else if (e.status == 1) {} else {
                  option.poster = require('@/assets/not_pass.jpg');
                }

                _this.playerOptions.push(option);
              });

            })
          });

        });
      },

      // 删除待上传的文件
      delBtn(index) {
        const _this = this;
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

        this.$axios.delete('http://39.98.108.11:8081/video/delete?vid=' + this.videoList[index].vid).then((results) => {

          _this.$axios.get('http://39.98.108.11:8081/video/findByuid?uid=' + _this.video.uid).then((results) => {

            _this.videoList = results.data.results;
          });

        });

      },

      click_image0() {
        Toast('进入个人信息页面');
        this.$router.push('/Portrait');
      },
      click_image(index) {
        Toast('进入博物馆信息页面');
        this.$router.push({
          name: 'mdetails',
          params: {
            id: this.uploadVideoList[index].mid
          }
        });

      },

      onClickLeft() {
        Toast('返回博物馆页面页面');
        this.$router.back();
      },

    },

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

  .forPreview_video {
    width: 80%;
    height: 20%;

    margin-left: 10%;
    border: 1px solid red;
    margin-top: 10px;
    background: green;

  }

  .video_info {
    display: flex;
    flex-direction: column;
    text-align: center;

  }

  .vinfo {
    margin-left: 0%;
    justify-content: space-between;
  }

  .video_list {
    border: 1px solid gray;
    margin-top: 10px;
    margin-left: 2%;
    margin-right: 2%;

  }

  .upload {
    margin: 0% 0% 10%;
  }

  .user {
    font-size: 40%;
  }
</style>
