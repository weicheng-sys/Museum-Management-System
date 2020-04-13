import Vue from 'vue'
import router from '@/router'
import Header from '@/components/header'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#header',
  router,
  components: { Header },
  template: '<Header/>'
})
