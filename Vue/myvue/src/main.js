// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import BaiduMap from 'vue-baidu-map'


//全局引入了vant，使用了vant内置的格式
import Vant from 'vant'
import 'vant/lib/index.css'
import Axios from "axios"					//axios接口引用
// 1.全局引用
import VideoPlayer from 'vue-video-player'


// import Video from 'video.js';
// Vue.use(Video)
import 'video.js/dist/video-js.css'



Vue.use(VideoPlayer)

// Vue.prototype.$video = Video
Vue.prototype.$axios=Axios	
Vue.prototype.$http = Axios

Axios.defaults.withCredentials=true;

Vue.use(Vant);

Vue.use(BaiduMap,{ak:'ArstD00t0HWNiwuMlIL0ZWrUscyFVu0R'});


Vue.config.productionTip = false;
Vue.component("newsitem",{
  props:["nums"],
  template:"<li>{{nums}}</li>"
});

//导入全局样式表
import './assets/css/global.css'


// App.all('*', function (req, res, next) {
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header('Access-Control-Allow-Headers', 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild');
//   res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
//   res.header("X-Powered-By", ' 3.2.1')
//   res.header("Content-Type", "application/json;charset=utf-8");
//   next();
// });






/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
 
console.log('1');
