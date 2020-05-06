<template>
  <div id="main">
    <div v-for="(item,i) in list" :key="i" style="position: center">
      <p>这里可以给每个视频添加描述信息如:</p>
      <h4>{{item.info}}</h4>
      <h4>{{item.title}}</h4>
      <video :id="'myVideo'+item.id" class="video-js">
        <source :src="item.src" type="video/mp4">
      </video>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SendV',
  data () {
    return {
      list: [
        {
          info: '这里是视频0',
          title: '故宫博物馆—青花瓷',
          src: 'http://img.yopoo.cn/banner_video.mp4 ',
          id: 0,
          pic: '../../assets/images/logo.png'
        },
        {
          info: '这里是视频1',
          title: '军事博物馆—大飞机',
          src: 'http://img.yopoo.cn/banner_video.mp4 ',
          id: 1,
          pic: ''
        },
        {
          info: '这里是视频2',
          title: '重庆博物馆—大茶壶',
          src: 'http://img.yopoo.cn/banner_video.mp4 ',
          id: 2,
          pic: ''
        }
      ]
    }
  },
  mounted () {
    this.initVideo()
    this.findvideocover()
  },
  methods: {
    initVideo () {
      // 初始化视频方法 循环列表获取每个视频的id
      this.list.map((item, i) => {
        let myPlayer = this.$video('myVideo' + item.id, {
          // 确定播放器是否具有用户可以与之交互的控件。没有控件，启动视频播放的唯一方法是使用autoplay属性或通过Player API。
          controls: true,
          // 建议浏览器是否应在<video>加载元素后立即开始下载视频数据。
          preload: 'auto',
          // 设置视频播放器的显示宽度（以像素为单位）
          width: '300px',
          // 设置视频播放器的显示高度（以像素为单位）
          height: '240px',
          // 封面图
          poster: item.pic
        })
      })
    },

    findvideocover () {
      let _this = this
      this.$nextTick(() => {
        let video = document.getElementsByClassName('video=js')
        let source = document.createElement('source')
        // source.src = require("../../assets/5b086751dbb7af1ea8fa8d05e66fe5c3.mp4");this.formLabelAlign.video
        source.src = this.formLabelAlign.video
        source.type = 'video/mp4'
        video.appendChild(source)
        video.addEventListener('loadeddata', function () {
          var canvas = document.createElement('canvas')
          canvas.width = '300'
          canvas.height = '240'
          canvas
            .getContext('2d')
            .drawImage(video, 0, 0, canvas.width, canvas.width)
          var img = document.createElement('img')
          let imgsrc = canvas.toDataURL('image/png')
          _this.Videoframehandle(imgsrc.split(',')[1])
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #main{
    position: relative;
  }
  .video-js{
    border: 0;
    margin: 2px;
    padding: 0;
    width: 98%;
  }
</style>
