<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    
    <br>
    
    <router-view/>
     <router-link to="/">Home</router-link>
     <router-link to="/Mypage">Mypage</router-link>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 2px;
}
/* 
div
{
    box-sizing:border-box;
    -moz-box-sizing:border-box;
    width:90%;
    height: 90%;
} */
</style>
