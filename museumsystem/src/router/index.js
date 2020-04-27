import Vue from 'vue';
import Router from 'vue-router';
import ranking from '@/components/ranking';
import HelloWorld from '@/components/HelloWorld';
import tohoprank from "@/components/tohoprank";
import mapview from "@/views/mainpage/mapview";
import personal from "@/components/personal";
import newview from "@/components/maintab/newview";
import testsong from "@/components/maintab/testsong";
import Search1 from "@/components/zanguo/Search1";
import ranklists from "@/components/maintab/Rankinglists/ranklists";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: "/",
      name: 'ranking',
      component: ranking
    },
    {
      path: "/HelloWorld",
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: "/Search1",
      name: 'Search1',
      component: Search1
    },
    {
      path: "/tohoprank",
      name: 'tohoprank',
      component: tohoprank
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
      path: "/testsong",
      name: 'testsong',
      component: testsong
    },
    {
      path: "/ranklists",
      name: 'ranklists',
      component: ranklists
    },

  ]

})
