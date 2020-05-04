import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import axios from 'axios'

Vue.prototype.axios = axios;
Vue.config.productionTip = false
axios.defaults.baseURL="http://localhost:8787";
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
