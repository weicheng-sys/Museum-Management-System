<template>
<div id="app">
    <van-nav-bar title="博物馆讲解视频列表" left-text="返回" left-arrow @click-left="onClickLeft" right-text="上传" @click-right="onClickRight" />

    <div class="upload">

        <div v-for="(item, index) in uploadVideoList" :key="index">

            <div style="font-size:xx-large;">{{index}}</div>
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
  <br>
  <br>
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
            msg: "仔！！！",
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

        createcode() {
            const _this = this
            _this.museums = this.$route.params.museum

            _this.$axios.get('http://39.98.108.11:8081/video/findBymid?mid=' + _this.museums.mid).then((results) => {

                //加入到播放列表当中
                results.data.results.forEach((e, i) => {

                    if (e.status == 1) {

                        _this.videoList.push(e);

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
                            // width: 10,
                            notSupportedMessage: '视频格式不支持，无法上传或者播放！', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                            controlBar: {
                                timeDivider: true,
                                durationDisplay: true,
                                remainingTimeDisplay: false,
                                fullscreenToggle: true //全屏按钮
                            }
                        };

                        //根据用户uid去获得用户信息，加入到uploadVideoList中去了
                        this.$axios.get('http://39.98.108.11:8081/user/findById?uid=' + e.uid).then((results) => {
                            console.log("用户信息：" + JSON.stringify(results));
                            _this.user = results.data.results;

                            if (results.data.results.icon == null) {
                                _this.user.icon = require('@/assets/user.jpg');
                            } else {
                                _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;
                            }

                            _this.uploadVideoList.push(_this.user);

                            _this.uploadVideoList.forEach((e, i) => {

                            });

                            if (e.status == 0) {
                                option.poster = require('@/assets/unreviewed.jpg');

                                option.sources.src = urls;

                                // option.poster ='';
                            } else if (e.status == 1) {
                                // option.poster = _this.museums.mimg;
                            } else {
                                option.poster = require('@/assets/not_pass.jpg');
                            }

                            _this.playerOptions.push(option);
                            _this.playerOptions.forEach((e, i) => {

                            });
                        });

                    }

                    if (_this.videoList.length == 0) {
                        var u = {
                            icon: require('@/assets/user.jpg'),
                            uname: '暂无讲解视频',
                        }

                        _this.uploadVideoList.push(u);
                        var v = {
                            vinfo: '',
                            vname: '',
                        }
                        _this.videoList.push(v);

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
                                src: '',
                                type: 'video/mp4', // 类型
                                type: "video/ogg",
                                type: "video/webm",
                            },
                            poster: require('@/assets/novideo.jpg'), //你的封面地址

                            notSupportedMessage: '暂无讲解视频！', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                            controlBar: {
                                timeDivider: true,
                                durationDisplay: true,
                                remainingTimeDisplay: false,
                                fullscreenToggle: true //全屏按钮
                            }
                        };
                        _this.playerOptions.push(option);

                    }

                })
            })

        },
        click_image() {
            Toast('进入个人信息页面');
            this.$router.push('/Portrait');

        },

        onClickLeft() {
            Toast('返回博物馆页面页面');
            this.$router.push({
                name: 'mdetails',
                params: {
                    id: this.museums.mid
                }
            })
        },
        onClickRight() {
            this.$router.push({
                name: 'Upload',
                params: {
                    museum: this.museums
                }
            })
        },

    },
    components: {

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
