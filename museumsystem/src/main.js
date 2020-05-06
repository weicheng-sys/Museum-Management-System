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
import axios from 'axios'
import VueAxios from 'vue-axios'
import { Sticky } from 'vant';
import { Grid, GridItem } from 'vant';
import { Divider } from 'vant';
import { Rate } from 'vant';
import { Progress } from 'vant';
import { Field } from 'vant';
import { Button } from 'vant';
import { Pagination } from 'vant';
import { NoticeBar } from 'vant';
import { Toast } from 'vant';
import { Slider } from 'vant';
import { RadioGroup, Radio } from 'vant';

Vue.use(Radio);
Vue.use(RadioGroup);
Vue.use(Slider);
Vue.use(Toast)
Vue.use(NoticeBar);
Vue.use(Pagination);
Vue.use(Button);
Vue.use(Field);
Vue.use(Progress);
Vue.use(Rate);
Vue.use(Divider);
Vue.use(Grid);
Vue.use(GridItem);
Vue.use(Sticky);
/*import VueResource from 'vue-resource'
Vue.use(VueResource)*/
Vue.use(VueAxios, axios)
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
