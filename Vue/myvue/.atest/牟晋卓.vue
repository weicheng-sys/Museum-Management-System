<template>
    
<div>
<!-- header start -->
<header id="header">
  <div class="mw1200 header-contain clearfix">
    <!-- logo start -->
    <h1 class="logo">
      <a href="javascript:void(0);" class="logo-title">LOGIN</a>
    </h1>
    <!-- logo end -->
    <!-- nav start -->
    <nav class="nav">
      <ul class="menu">
        <li class="active"><a href="./xianqing.html">音视屏</a></li>
        <li><a href="#">导航二</a></li>
        <li><a href="#">导航三</a></li>
        <li><a href="#">导航四</a></li>
      </ul>
    </nav>
    <!-- nav end -->
    <!-- login start -->
    <div class="login-box">
      <div>
        <i class="PyWhich py-user"></i>
        <span>
                        <a href="./login.html" class="login">登录</a> / <a href="./register.html" class="reg">注册</a>
                      </span>
      </div>
      <div class="author hide">
        <i class="PyWhich py-user"></i>
        <span>qwertyui</span>
        <ul class="author-menu">
          <li><a href="javascript:void(0);">后台管理</a></li>
          <li><a href="javascript:void(0);">退出登录</a></li>
        </ul>
      </div>
    </div>
    <!-- login end -->
  </div>
</header>
<!-- header end -->

<!-- container start -->
<main id="container">
  <div class="register-contain">
    <div class="top-contain">
      <h4 class="please-register">请注册</h4>
      <a href="javascript:void(0);" class="login">立即登录 &gt;</a>
    </div>
    <form action="" method="post" class="form-contain">


      <div class="form-item">
        <input type="text" placeholder="请输入用户名" id="user_name" name="username" class="form-control" autocomplete="off">
      </div>
      <div class="form-item">
        <input type="password" placeholder="请输入密码" id="pwd" name="password" class="form-control">
      </div>
      <div class="form-item">
        <input type="password" placeholder="请输入确认密码" name="password_repeat" class="form-control">
      </div>
      <div class="form-item">
        <input type="tel" placeholder="请输入手机号" id="mobile" name="telephone" class="form-control" autocomplete="off" autofocus>
      </div>
      <div class="form-item">
        <input type="text" placeholder="请输入图形验证码" id="input_captcha" name="captcha_graph" class="form-captcha">
        <a href="javascript:void(0);" class="captcha-graph-img">
          <img src="../../assets/images/captcha.png" alt="验证码" title="点击刷新">
        </a>
      </div>
      <div class="form-item">
        <input type="text" placeholder="请输入短信验证码" name="sms_captcha" class="form-captcha" id="input_smscode" autocomplete="off">
        <a href="javascript:void(0);" class="sms-captcha" title="发送验证码">获取短信验证码</a>
      </div>
      <div class="form-item">
        <input type="submit" value="立即注册" class="register-btn">
      </div>
    </form>
  </div>
</main>
<!-- container end -->

<!-- footer start -->
<footer id="footer">
  <div class="footer-box">
    <div class="footer-content">
      <h3>这是页面底部</h3>
    </div>
    <p class="copyright-desc">
      软件工程第四小组：周梦，牟晋卓，江锐，卢峰霖，石彦祖------奥利给！！！
    </p>
  </div>
</footer>
</div>
</template>

<<script>

export default {
  name:"login"
}
</script>

<style>
@import  "../../assets/css/authPro/auth.css";
@import  "../../assets/css/base/common.css";
@import  "../../assets/css/base/reset.css";
@import  "../../assets/css/base/side.css";
@import  "../../assets/css/base/sweetalert.css";
</style>
