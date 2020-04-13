import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Homes/Home'
import Mypage from '@/pages/Mypages/Mypage'
import Portrait from '@/pages/Mypages/Portrait'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Mypage',
      name: 'Mypage',
      component: Mypage
    },
    {
    path: '/Portrait',
    name: 'Portrait',
    component: Portrait

    }
  ]
})
