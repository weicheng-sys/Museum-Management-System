// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { Search } from 'vant';
import { Swipe, SwipeItem } from 'vant';
import { List } from 'vant';
import { Cell, CellGroup } from 'vant';
import { Card } from 'vant';
import { Col, Row } from 'vant';
import { Image } from 'vant';
import { Icon } from 'vant';
import { NavBar } from 'vant';
import { Tabbar, TabbarItem } from 'vant';
import { Tab, Tabs } from 'vant';
import { Panel } from 'vant';

Vue.use(Panel);
Vue.use(Tab);
Vue.use(Tabs);
Vue.use(Tabbar);
Vue.use(TabbarItem);
Vue.use(NavBar);
Vue.use(Icon);
Vue.use(Image);
Vue.use(Col);
Vue.use(Row);
Vue.use(Card);
Vue.use(Cell);
Vue.use(CellGroup);
Vue.use(List);
Vue.use(Swipe);
Vue.use(SwipeItem);
Vue.use(Search);
Vue.config.productionTip = false;
Vue.component("news",{
  props:["nums"],
  template:"<li>{{nums}}</li>"
});
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
