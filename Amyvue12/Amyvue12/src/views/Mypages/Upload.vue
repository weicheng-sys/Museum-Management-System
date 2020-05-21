<<template>
<div>
    <van-nav-bar title="上传视频" left-text="返回" left-arrow @click-left="onClickLeft" />
    <van-form>
        <van-field v-model="video.vname" name="vname" label="视频名称" placeholder="请输入视频名称" />
        <van-field v-model="video.vinfo" name="vinfo" label="视频简介" placeholder="请输入视频简介" />
    </van-form>

    <van-uploader v-show="true" preview-size="80px" accept="video/*" :before-read="beforeRead"></van-uploader>

    <div class="forPreview_video" v-for="(item, index) in uploadVideoList" :key="index">
        <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsinline="true" :options="playerOptions"></video-player>
    </div>
    <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit" @click='onsave'>
            确认上传视频
        </van-button>
    </div>
</div>
</template>

 
<script>
import {
    Toast
} from 'vant';
export default {
    name: "Upload",
    data() {
        return {
            formData: '',
            config: '',
            video: {
                uid: '',
                mid: '',
                vname: '',
                vaddr: '',
                vinfo: '',
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
            uploadVideoList: [],
            playerOptions: {

                playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 默认情况下将会消除任何音频。
                loop: false, // 导致视频一结束就重新开始。
                preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: 'zh-CN',
                aspectRatio: '4:3', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: {

                    src: '', // 路径
                    type: 'video/mp4',
                    type: "video/ogg",
                    type: "video/webm",
                    // 类型
                },
                poster: "", //你的封面地址
                // width: 10,
                notSupportedMessage: '选择视频后，可在此处进行预览', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                controlBar: {
                    timeDivider: true,
                    durationDisplay: true,
                    remainingTimeDisplay: false,
                    fullscreenToggle: true //全屏按钮
                }
            },

        }
    },
    mounted() {
        this.getinfo();
    },

    methods: {

        getinfo() {
            const _this = this;
            _this.museums = this.$route.params.museum;
            _this.video.mid = _this.museums.mid;
            //找到当前登陆的用户！！！！！
            _this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
                _this.video.uid = results.data.results.uid;

            });
        },
        onsave() {
            const _this = this;

            _this.$axios.post('http://39.98.108.11:8081/video/uploadFile', _this.formData, _this.config).then(results => {
                //上传成功，存入video表！
                if (results.data.success == true) {
                    _this.video.vaddr = results.data.fileUrl;

                    _this.$axios.post('http://39.98.108.11:8081/video/add', _this.video).then((results) => {
                        Toast('文件上传成功！')
                    });

                }
                //this.fileIdArr = res.data.data;  // 把選中的文件傳送給後台
            }).catch(err => {
                Toast('文件上傳失敗！')
            });

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

            // let uploadUrl = URL.createObjectURL(file); // 将选中的上传文件转化为二进制文件，显示在页面上
            // console.log(file);

            this.uploadVideoList.push(file);
            _this.playerOptions.sources.src = uploadUrl;
            //_this.playerOptions.poster=require('@/assets/look.jpg');

            formData.append("fileName", file);

            _this.formData = formData;
            _this.config = config;

        },

        onClickLeft() {
            Toast('返回' + this.museums.mname + '视频讲解页面');
            this.$router.push({
                name: 'mvideo',
                params: {
                    museum: this.museums
                }
            })
        },

    },
}
</script>
