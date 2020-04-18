import Vue from 'vue';
import Router from 'vue-router';
import ranking from '@/components/ranking';
import HelloWorld from '@/components/HelloWorld';
import tosearch from "@/components/tosearch";
import tohoprank from "@/components/tohoprank";
import mapview from "@/views/mainpage/mapview";
import personal from "@/components/personal";
import newview from "@/components/maintab/newview";
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
      path: "/tosearch",
      name: 'tosearch',
      component: tosearch
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
  ]

})
