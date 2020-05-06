import Vue from 'vue';
import Router from 'vue-router';
import ranking from '@/components/ranking';
import HelloWorld from '@/components/HelloWorld';

import mapview from "@/views/mainpage/mapview";
import personal from "../components/huangxu/personal";
import newview from "@/components/maintab/newview";
import Search1 from "@/components/zanguo/Search1";
import ranklists from "@/components/maintab/Rankinglists/ranklists";
import mdetails from "../components/mdetails";
import collections from "../components/collections";
import newsdl2 from "../components/newsdl2";
import setting1 from "../components/huangxu/setting1";
import changepassword from "../components/huangxu/changepassword";
import collect from "../components/huangxu/collect";
import vidio from "../components/maintab/vidio";
import newsdl from "../components/maintab/newsdl";
import scoring from "../components/scoring";
import Search0 from "../components/zanguo/Search0";
import Search2 from "../components/zanguo/Search2";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: "/",
      name: 'ranking',
      component: ranking,
      meta: {
        keepAlive: true
      }
    },
    {
      path: "/HelloWorld",
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: "/search1",
      name: 'search1',
      component: Search1,
      meta: {
        keepAlive: true
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
        keepAlive: true
      }
    },
    {
      path: "/vidio",
      name: 'vidio',
      component: vidio
    },
    {
      path: "/mapview",
      name: 'mapview',
      component: mapview
    },
    {
      path: "/personal",
      name: 'personal',
      component: personal
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
        keepAlive: true
      }
    },
    {
      path: "/mdetails",
      name: 'mdetails',
      component: mdetails,
      meta: {
        title: "text",
        keepAlive: true
      }
    },

    {
      path: "/collections",
      name: 'collections',
      component: collections,
      meta: {
        keepAlive: true
      }
    },
    {
      path: "/newsdl2",
      name: 'newsdl2',
      component: newsdl2,
      meta: {
        keepAlive: true
      }
    },
    {
      path: "/setting1",
      name: 'setting1',
      component: setting1,
    },
    {
      path: "/newsdl",
      name: 'newsdl',
      component: newsdl,
    },
    {
      path: "/scoring",
      name: 'scoring',
      component: scoring,
    },

  ]

})
