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
Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       redirect: '/Register',
//       name: 'Home',
//       component: Home
//     },
//     {
//       path: '/Mypage',
//       name: 'Mypage',
//       component: Mypage
//     },
//     {
//     path: '/Portrait',
//     name: 'Portrait',
//     component: Portrait

//     },
//     {
//       path:'/Map',
//       name:'Maps',
//       component: Maps
//     },
//     {
//       path:'/Login',
//       name:'Login',
//       component: Login
//     },
//     {
//       path:'/Search',
//       name:'Search',
//       component: Search
//     },
//     {
//       path:'/Register',
//       name:'Register',
//       component: Register
//     }
//   ]
// })


const router= new Router({
  routes: [
    {
      path: '/',
      redirect: '/Login_and_Register',
    },
    {
      path: '/Home',
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

    },
    {
      path:'/Map',
      name:'Maps',
      component: Maps
    },
    {
      path:'/Login_and_Register',
      name:'Login_and_Register',
      component: Login_and_Register
    },
    // {
    //   path:'/Login',
    //   name:'Login',
    //   component: Login
    // },

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
