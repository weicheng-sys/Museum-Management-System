VueThink
===============

VueThink不仅适用于管理后台或管理系统开发，且广泛适用于B/S架构的项目开发。VueThink是对前后端分离技术的应用实践，2016年由洪睿科技的技术团队研发并投入商业开发使用，已有许多的商业项目实践。而今框架开源，希望能有更多志同道合的伙伴参与VueThink的迭代 ^_^

使用许可：VueThink是基于MIT协议的开源框架，它完全免费。你可以免费下载VueThink，用来搭建自己的或者团体的软件。

主要适用技术栈：
后端框架：ThinkPHP 5.x
前端MVVM框架：Vue.JS 2.x
开发工作流：Webpack 1.x
路由：Vue-Router 2.x
数据交互：Axios
代码风格检测：Eslint
UI框架：Element-UI 1.1.6
JS函数库：Lodash

> VueThink的运行环境要求PHP5.4以上。

详细开发文档参考 [ThinkPHP5完全开发手册](http://www.kancloud.cn/manual/thinkphp5)

### 后端部署

1.服务端使用的框架为thinkphp5.搭建前请确保拥有lamp/lnmp/wamp环境。
  集成环境推荐使用phpset：<http://www.phpset.cn/>

2.配置重写：请参考<https://www.kancloud.cn/manual/thinkphp5/177576>

3.导入数据库并配置
  导入服务端根文件夹数据库文件install.sql，(数据库内用户表账号admin，密码123456)并修改config/database.php配置文件。

* PHP >= 5.6.0
* PDO PHP Extension
* MBstring PHP Extension
* CURL PHP Extension
