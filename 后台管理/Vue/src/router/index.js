import Vue from 'vue'
import VueRouter from 'vue-router'
import page1 from "../views/page1";
import page1edit from "../views/page1edit";
import page2 from "../views/page2";
import page2edit from "../views/page2edit";
import page3 from "../views/page3";
import page4 from "../views/page4";
import page5 from "../views/page5";
import menu from "../views/menu";
import Change from '../views/Change'
import ChangeUsr from '../views/ChangeUsr'
import Login from "../views/Login";
import Audit from "../views/Audit"
import Auditedit from "../views/Auditedit";
import page3edit from "../views/page3edit";
Vue.use(VueRouter)

const routes = [
  {
    path:'',
    redirect:"/login",
  },
  {
    path:'/login',
    name:"登录",
    component:Login,
  },
  {
    path: '/museum',
    name: '博物馆信息',
    component: menu,
    show:true,
    children:[
      {
        path: '/page1',
        name: '基本信息',
        component: page1
      },
      {
        path: '/page2',
        name: '新闻信息',
        component:page2
      }
    ]
  },

  {
    path: '/page1edit',
    name: '博物馆信息',
    component:page1edit,

  },

  {
    path:'/Auditedit',
    name:'审核详情',
    component:Auditedit
  },
  {
    path:'/page3edit',
    name:'视频详情',
    component:page3edit
  },

  {
    path: '/page2edit',
    name: '新闻信息',
    component:page2edit,

  },

  {
    path: '/',
    name: '讲解信息',
    component: menu,
    show:true,
    children:[
      {
        path: '/page3',
        name: '讲解视频',
        component: page3
      },
      {
        path: '/Audit',
        name: '审核视频',
        component: Audit
      }
    ]
  },
  {
    path: '/',
    name: '用户管理',
    component: menu,
    show:true,
    children:[
      {
        path: '/page4',
        name: '用户管理',
        component:page4
      },
    ]
  },
  {
    path: '/',
    name: '系统管理',
    component: menu,
    show:true,
    children:[
      {
        path: '/page5',
        name: '系统管理',
        component:page5
      },
    ]
  },
  {
    path: "/change",
    component: Change,

  },
  {
    path: "/changeusr",
    component: ChangeUsr,

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
