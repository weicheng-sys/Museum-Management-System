<template>
  <div id="app" v-cloak>
    <h2>样式1</h2>
    <ul>
      <li>视频列表</li>
      <li v-for="item in urlss">
        <a :href="item.url">视频{{item.id}}</a>
      </li>
    </ul>
    <br><br><br><br><br><br>
    <h2>样式1</h2>
    <select onchange="javascript:if (this.options[this.selectedIndex].value != '') window.open(this.options[this.selectedIndex].value);this.options[0].selected;">
    　　<option>视频列表</option>
    　　<option v-for="item in urlss" :value="item.url">
          视频{{item.id}}
        </option>
    　　
    </select>
  </div>
</template>

<script>
  export default {
    name: "App",
    data(){
      return {
        urlss:[{"id":1,"url": "https://img.tukuppt.com/video_show/2475824/00/02/19/5b527330214a6.mp4"},
          {"id":2,"url":"kkkk"},
          {"id":3,"url":"kkkk"},
          {"id":4,"url":"kkkk"},
        ]
      }
    }
  }


</script>

<style scoped>

</style>
