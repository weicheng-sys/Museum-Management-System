/* eslint-disable */

import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Homes/Home'
import Mypage from '@/views/Mypages/Mypage'
import Maps from '@/views/Maps/Map'
import Portrait from '@/views/Mypages/Portrait'
//import Login from '@/views/Login/Login'
import Register from '@/views/Login/Register'
import Login_and_Register from '@/views/Login/Login_and_Register'
import Search from '@/views/Homes/HomeChild/Search'
import Change_name from '@/views/Mypages/Change/Change_name'
import Change_phone from '@/views/Mypages/Change/Change_phone'
import Change_password from '@/views/Mypages/Change/Change_password'
import Change_gender from '@/views/Mypages/Change/Change_gender'
import Change_introduction from '@/views/Mypages/Change/Change_introduction'
import Upload from '@/views/Mypages/Upload'
import scoring from '../views/Homes/HomeChild/museum_details/scoring'
import Search0 from '../views/Homes/HomeChild/Search_all/Search0'
import Search2 from '../views/Homes/HomeChild/Search_all/Search2'
import Search1 from '../views/Homes/HomeChild/Search_all/Search1'
import ranklists from '../views/Homes/HomeChild/museum_details/ranklists'
import newsdl from '../views/Homes/HomeChild/ndetails/newsdl'
import collections from '../views/Homes/HomeChild/museum_details/collections'
import newview from '../views/Homes/HomeChild/News'
import mdetails from '../views/Homes/HomeChild/museum_details/mdetails'
import mvideo from '../views/Homes/HomeChild/museum_details/mvideo'
import newsdl2 from '@/views/Homes/HomeChild/ndetails/newsdl2'
import mdetails2 from '../views/Homes/HomeChild/museum_details/mdetails2'
Vue.use(Router)


const router= new Router({
  routes: [
    {
      path: '/',
      redirect: '/Login_and_Register',
      meta: {
        keeptabbar: false
      }

    },
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      meta: {
        keepAlive: true,
        keeptabbar: true
      }
    },
    {
      path: '/Mypage',
      name: 'Mypage',
      component: Mypage,
      meta: {
        keepAlive: false,
        keeptabbar: true
      }
    },
    {
    path: '/Portrait',
    name: 'Portrait',
    component: Portrait,
    meta: {
      keepAlive: false,
      keeptabbar: true
    }

    },
    {
      path:'/Map',
      name:'Maps',
      component: Maps,
      meta: {
        keepAlive: true,
        keeptabbar: true
      }
    },
    {
      path:'/Login_and_Register',
      name:'Login_and_Register',
      component: Login_and_Register
    },


    {
      path:'/Search',
      name:'Search',
      component: Search
    },
    {
      path:'/Register',
      name:'Register',
      component: Register
    },
    {
      path:'/Change_name',
      name:'Change_name',
      component: Change_name
    },
    {
      path:'/Change_phone',
      name:'Change_phone',
      component: Change_phone
    },
    {
      path:'/Change_password',
      name:'Change_password',
      component: Change_password
    },
    {
      path:'/Change_gender',
      name:'Change_gender',
      component: Change_gender
    },
    {
      path:'/Change_introduction',
      name:'Change_introduction',
      component: Change_introduction
    },
    {
      path:'/Upload',
      name:'Upload',
      component: Upload

    },

    {
      path: "/search1",
      name: 'search1',
      component: Search1,
      meta: {
        keepAlive: true,
        keeptabbar: true
      }
    },
    {
      path: "/search0",
      name: 'search0',
      component: Search0,

    },
    {
      path: "/search2",
      name: 'search2',
      component: Search2,
      meta: {
        keepAlive: true,
        keeptabbar: true
      }
    },
    {
      path: "/newview",
      name: 'newview',
      component: newview
    },
    {
      path: "/ranklists",
      name: 'ranklists',
      component: ranklists,
      meta: {
        keepAlive: true,
        isBack: false,
        keeptabbar: true
      }
    },
    {
      path: "/mdetails",
      name: 'mdetails',
      component: mdetails,
      meta: {
        keepAlive: true,
        keeptabbar: true
      }
    },
    {
      path: "/mdetails2",
      name: 'mdetails2',
      component: mdetails2,
      meta: {
        keepAlive: true,
        isBack: false,
        keeptabbar: true
      }
    },
    {
      path: "/collections",
      name: 'collections',
      component: collections,
      meta: {
        keepAlive: true,
        isBack: false,
        keeptabbar: true
      }
    },

    {
      path: "/newsdl",
      name: 'newsdl',
      component: newsdl,
    },
    {
      path: "/newsdl2",
      name: 'newsdl2',
      component: newsdl2,
    },
    {
      path: "/scoring",
      name: 'scoring',
      component: scoring,
    },
    {
      path:"/mvideo",
      name:'mvideo',
      component:mvideo,
      meta: {
        keepAlive: false,
        keeptabbar: true
      }
    }

  ]
})


// //挂载导航守卫
// router.beforeEach((to,from,next)=>{
// //to要访问的路径
// //from从哪个路径而来
// //next 一个函数，表示放行
// if(to.path==='/login') return next();
//   //获取token
//   const tokenstr=window.sessionStorage.getItem('token')
//   if(!tokenstr) return next('/login');
//   next();
// })

export default router;
