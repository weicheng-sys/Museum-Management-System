<template>
  <div id="app">

    <div class="upload">

      <div v-for="(item, index) in uploadVideoList" :key="index">

        <div style="font-size:large;margin-top:3px;" @click="gotodetail(index)">{{index}}:{{museum_list[index].mname}}</div>
        <div class="video_list">

          <van-row type="flex">
            <van-image @click="click_image" round width="5rem" height="5rem" :src="item.icon" />
            <van-cell class="vinfo" :title="item.uname" :value="videoList[index].vname" />
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
  import Axios from "axios" //axios接口引用
  import {
    Toast
  } from 'vant';
  export default {
    data() {
      return {
        flag: -1,
        msg: "周梦仔！！！",
        id: 0,
        url: '',
        videoList: [],
        video: [],

        user: {
          uname: '',
          uid: '',
          icon: '',
        },
        museums: {
          mid: '',
          mname: '',
        },
        museum_list: [],

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

    filters: {
      formatSize(val) { // 格式化文件大小
        if (val > 0) {
          return (val / 1024 / 1024).toFixed(2) + 'M';
        } else {
          return '0M';
        }
      },
    },
    mounted() {
      this.createcode()
    },
    methods: {
      gotodetail(index) {
        const _this = this
        _this.$router.push({
          name: 'mdetails',
          params: {
            id: _this.museum_list[index].mid
          }
        })
      },
      createcode() {
        const _this = this

        _this.$axios.get('http://39.98.108.11:8081/video/findAll').then((results) => {
          results.data.results.forEach((e, i) => {

            if (results.data.results.length >= 20) {
              this.flag = Math.round(Math.random() * results.data.results.length);
            }
            if (e.status == 1 && this.flag == -1 || e.status == 1 && e.vid == this.flag) {
              var url = e.vaddr;
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
                  src: urls,
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
                let x = results.data.results.mimg;
                if (x.indexOf('jpg')) {
                  let y = x.indexOf('jpg') + 1
                  results.data.results.mimg = x.substr(2, y);
                  option.poster=results.data.results.mimg;
                }

                _this.videoList.push(e);
                _this.museums.mname = results.data.results.mname;
                _this.museums.mid = results.data.results.mid;
                var muse = {
                  mname: _this.museums.mname,
                  mid: _this.museums.mid,
                }
                _this.museum_list.push(muse);

                this.$axios.get('http://39.98.108.11:8081/user/findById?uid=' + e.uid).then((results) => {

                  _this.user = results.data.results;
                  if (results.data.results.icon == null)
                    _this.user.icon = require('@/assets/user.jpg')
                  else {
                    _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;
                  }

                  var user_muse = {
                    uname: _this.user.uname,

                    icon: _this.user.icon,
                  };

                  _this.uploadVideoList.push(user_muse);

                  _this.playerOptions.push(option);

                });

              });
            }
          })

        })

      },

      click_image() {
        Toast('进入个人信息页面');
        this.$router.push('/Portrait');
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
</style>
