// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Mint from 'mint-ui';
import Viewer from 'v-viewer'

import 'viewerjs/dist/viewer.css'

Vue.use(Viewer)

Vue.use(Mint)
/*import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$http.defaults.baseURL = '' // `baseURL` 将自动加在 `url` 前面，除非 `url` 是一个绝对 URL*/
Vue.config.productionTip = false
Vue.use(ElementUI);
/* eslint-disable no-new */
Vue.component("news",{
  props:["nums"],
  template:"<li>{{nums}}</li>"
})
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
