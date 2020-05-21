<template>
<div>

    <van-sticky>
        <van-row class="bgset" style="width:100%;height:50px;">
            <van-col span="24">
                <van-nav-bar left-text="返回" left-arrow @click-left="back">

                </van-nav-bar>
            </van-col>
        </van-row>
    </van-sticky>

    <img :src="mimgs" style="width:100%;height:200px;" />

    <van-panel style="text-align: left;font-size: 15px;height:80px">
        <div>
            <van-row>
                <textarea class="maintext" v-model="list.basic_info" style="height:80px;width: 100%;border: none;outline: none;resize:none;" readonly>
          </textarea>
            </van-row>

        </div>
    </van-panel>
    <van-divider />
    <van-panel title="简述" style="text-align: left;font-size: 20px">
        <div style="text-align: left;font-size: 13px">
            <textarea class="maintext" v-model="list.other_info" style="height:80px;width: 100%;border: none;outline: none;resize:none;" readonly>
          </textarea>
        </div>
    </van-panel>

    <!--评分面板-->
    <van-panel style="background: rgba(80,230,225,0.28);margin : 10px 10px 10px 10px;border-radius: 35px;">
        <van-row>
            <van-col span="1">
            </van-col>
            <van-col span="7" style="text-align: left;font-size: 20px"> 综合评分：</van-col>
            <van-col span="3" style="text-align: left;font-size: 15px">{{list.grade}}</van-col>
            <van-col span="12" style="text-align: right;font-size: 20px">
                <van-rate v-model=starrr allow-half void-icon="star" void-color="#eee" readonly />
            </van-col>
            <van-col span="1">
            </van-col>
        </van-row>
        <van-row><br>
            <van-col span="1">
            </van-col>
            <van-col span="8" style="text-align: left;font-size: 20px">展览：</van-col>
            <van-col span="15">
                <van-progress :percentage=Number(list.grade_1) stroke-width="8" />
            </van-col>
        </van-row>
        <van-row><br>
            <van-col span="1">
            </van-col>
            <van-col span="8" style="text-align: left;font-size: 20px">服务：</van-col>
            <van-col span="15">
                <van-progress :percentage=Number(list.grade_2) stroke-width="8" />
            </van-col>
        </van-row>
        <van-row><br>
            <van-col span="1">
            </van-col>
            <van-col span="8" style="text-align: left;font-size: 20px">环境：</van-col>
            <van-col span="15">
                <van-progress :percentage=Number(list.grade_3) stroke-width="8" />
            </van-col>
        </van-row>
        <van-row>

            <van-col span="24" style="text-align: center;font-size: 18px">
                <van-button text="为他打分" type="round" color="#a92e43" v-on:click="toscoring"></van-button>
            </van-col>
        </van-row>
    </van-panel>

    <!--新闻面板-->
    <van-panel>
        <van-row>
            <van-col span="4" style="text-align: left;font-size: 16px">新闻：</van-col>
            <van-col span="20" style="text-align: right;font-size: 16px" v-on:click="tocollection">查看全部</van-col>
        </van-row>
        <van-grid :column-num=4>
            <van-grid-item v-for="(item,index) in mimglist" :key="index" v-if="index<4">
                <img :src="mimglist[index]" style="width:100%;height:100%;" />
            </van-grid-item>
        </van-grid>
    </van-panel>
    <!--视频面板-->
    <van-panel>
        <van-row>
            <van-col span="4" style="text-align: left;font-size: 16px">视频：</van-col>
            <van-col span="20" style="text-align: right;font-size: 16px" v-on:click="tovideo">查看全部</van-col>
        </van-row>

        <van-row type="flex">
            <van-image round width="5rem" height="5rem" :src="uploadVideoList[0].icon" />
            <van-cell class="vinfo" :title="uploadVideoList[0].uname" :value="videoList[0].vname" />
        </van-row>

        <van-cell class="vinfo" :title="videoList[0].vinfo" />
        <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions[0]"></video-player>

    </van-panel>

    <!--评价-->
    <van-row>
        <van-col span="4" style="text-align: left;font-size: 18px">
            <van-image round width="40px" height="40px" src="https://img.yzcdn.cn/vant/cat.jpeg" />
        </van-col>

        <van-col span="16" style="text-align: left;font-size: 18px">
            <van-cell-group>
                <van-field v-model="coment" placeholder="请输入评价" />
            </van-cell-group>
        </van-col>

        <van-col span="4" style="text-align: right;font-size: 18px">
            <van-button text="评价" type="info" color="#e33e33" v-on:click="update"></van-button>
        </van-col>
    </van-row>

    <van-list v-model="loading" :finished="finished" finished-text="没有更多了" @load="onLoad">
        <van-cell v-for="item in evaluate">

            <van-panel>
                <van-row>
                    <van-col span="4" style="text-align: left;font-size: 18px">
                        <img :src=mlist.mimg style="width:40px;height:40px;border-radius: 50%;background-repeat: no-repeat" />
                    </van-col>
                    <van-col span="18" style="text-align: left;font-size: 16px">
                        匿名
                    </van-col>
                    <van-col span="2">
                        举报
                    </van-col>
                </van-row>
                <van-row>
                    {{item}}
                </van-row>
            </van-panel>
        </van-cell>
    </van-list>
    <br><br><br>

</div>
</template>

<script>
import {
    Toast
} from 'vant'

export default {
    name: "mdetails",
    data() {
        return {
            value: "",
            p1: [60, 70, 80],
            value1: 2,
            list: [],
            Collection: [],
            user: [],
            mid: 0,
            mimgs: [],
            starrr: 0,
            nimglist: [],
            coment: "",
            mlist: {
                mid: 1,
                mname: "中国航天博物馆",
                maddr: "北京",
                mtype: "科技",
                ticket: 10,
                buidtime: "1969",
                opentime: "全天",
                cnum: 650,
                ctype: 35,
                enum: 8,
                mimg: ["https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3493135802,624957787&fm=173&app=25&f=JPEG?w=529&h=294&s=F281D80302C30CEC34913CB00300C020"],
                evaluate: "还不错",
                grade: 4.5
            },
            mimglist: [],
            loading: false,
            finished: false,
            currentPage: 1,
            evaluate: [],
            newslist: [],
            playerOptions: [],
            videoList: [],
            uploadVideoList: [],
        };
    },
    created() {
        this.getid();
        this.getlist();

    },

    beforeRouteLeave(to, from, next) {

        if (to.path == "/collections") {
            from.meta.keepAlive = true;
            to.meta.keepAlive = false;
        } else {
            from.meta.keepAlive = false;
        }

        next();
    },
    methods: {
        onLoad() {
            // 异步更新数据
            // setTimeout 仅做示例，真实场景中一般为 ajax 请求
            setTimeout(() => {
                for (let i = 0; i < 10; i++) {
                    this.list.push(this.list.length + 1);
                }

                // 加载状态结束
                this.loading = false;

                // 数据全部加载完成
                if (this.list.length >= 40) {
                    this.finished = true;
                }
            }, 1000);
        },
        back() {
            this.$router.back()
        },
        tocollection() {
            this.$router.push({
                name: 'collections',
                params: {
                    mname: this.list.mname,
                    mid: this.list.mid
                }
            })
        },
        tovideo2() {
            this.$router.push({
                name: 'video2',
                params: {
                    mname: this.list.mname
                }
            })
        },
        tovideo() {
            this.$router.push({
                name: 'mvideo',
                params: {
                    museum: this.list
                }
            })
        },
        getid() {
            this.mid = this.$route.params.id
        },
        setevaluate() {
            this.evaluate = this.list.evaluate.split('<-$->')
            console.log(this.evaluate)
        },
        addevaluate() {
            this.list.evaluate = this.list.evaluate + '<-$->' + this.coment
        },
        update() {
            this.addevaluate();
            console.log("评价")
            var _self = this;
            this.$http.post("http://39.98.108.11:8081/MDL/update", JSON.stringify(this.list), {
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Token': '84c6635800b14e0eba4f7ece65e095a1'
                }
            }).then((response) => {
                _self.ok = response.data
                console.log("ok")
                Toast('评价成功');
            })
        },
        sliptsd(img) {
            var img2 = img.split('[')
            var img3 = img2[1].split(']')
            var img4 = img3[0].replace(/,\'https:/g, ',,\'https:')
            var img5 = img4.replace(/\'/g, '')
            return img5.split(',,')
        },
        getlist4() {
            var _self = this;
            console.log(4);
            console.log(this.list.mname);
            this.$http.get("http://39.98.108.11:8081/News/findByname?name=" + this.list.mname).then((response) => {
                _self.newslist = response.data
                console.log(_self.newslist)
                console.log(5)
            })
        },
        getlist() {
            var t = this;
            console.log("博物馆详情页面")

            this.$http.get("http://39.98.108.11:8081/MDL/findByid?id=" + this.mid).then((response) => {
                t.list = response.data
                this.setevaluate()
                console.log(t.list)
                console.log(t.list.mname);
                t.starrr = Number(t.list.grade)

                let x = t.list.mimg;

                if (x.indexOf("', ")) {
                    console.log("abc")
                    let n = x.split("', ");
                    if (n.length > 1) {
                        t.mimgs.push(n[0].substr(2));
                        for (let i = 1; i < n.length - 1; i++) {
                            t.mimglist.push(n[i].substr(1));
                        }
                        t.mimglist.push(n[n.length - 1].slice(1, n[n.length - 1].length - 2))
                        console.log(t.mimglist)
                    }

                }
                if (x.indexOf('jpg')) {
                    let y = x.indexOf('jpg') + 1
                    t.mimgs = x.substr(2, y);
                    t.mimglist.clear();
                    console.log(t.mimglist)
                }
            })

            const _this = this
            _this.$axios.get('http://39.98.108.11:8081/video/findBymid?mid=' + _this.mid).then((results) => {

                if (results.data.results.length == 0) {
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

                } else {

                    //加入到播放列表当中
                    results.data.results.forEach((e, i) => {

                        if (e.status == 1)

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
                            _this.user = results.data.results;
                            if (results.data.results.icon == null) {
                                _this.user.icon = require('@/assets/user.jpg')
                            } else {

                                _this.user.icon = 'http://39.98.108.11:8081/files' + results.data.results.icon;

                            }

                            _this.uploadVideoList.push(_this.user);

                            _this.uploadVideoList.forEach((e, i) => {

                            });

                            if (e.status == 0) {
                                option.poster = require('@/assets/unreviewed.jpg');
                                option.sources.src = urls;
                            } else if (e.status == 1) {} else {
                                option.poster = require('@/assets/not_pass.jpg');
                            }
                            _this.playerOptions.push(option);

                        });

                    })

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
                }

            })

        },
        toscoring() {
            this.$router.push({
                name: 'scoring',
                params: {
                    id: this.list.mid
                }
            })
        },

    },

}
</script>

<style scoped>
.maintext {
    text-align: left;
    white-space: pre-wrap;
    text-indent: 2em;
    line-height: 1.8em;

}
</style>
