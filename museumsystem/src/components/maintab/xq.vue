<template>
<div>
  <van-card
    class="lb"
    currency=""
    price="关注度99%"

    title="“司母戊鼎”为何突然改称“后母戊鼎”？--铜鼎"
    thumb="http://img2.99114.com/group1/M00/2F/65/wKgGTFYBKH-ADlLEAALlTzqKbD0080.jpg"
  >
  <template #tags>
      <van-tag plain type="danger">大国重器</van-tag>
      <van-tag plain type="danger">经典流传</van-tag>
    </template>
  </van-card>
     <van-swipe :autoplay="3000">
     <van-swipe-item v-for="(image, index) in images" :key="index" style="weight: 100% ; height: 200px">
       <img v-lazy="image" style="weight: 100% ; height: 200px"/>
     </van-swipe-item>
   </van-swipe>
  <span>




    </span>

  <span>
     1939年出土于安阳的司母戊鼎为商代后期王室青铜祭器，是迄今发现的世界上最大、最重的青铜器。对此，人们耳熟能详。但有报道称，“司母戊鼎”有可能更名为“后母戊鼎”。国宝级铜鼎到底该姓“司”还是姓“后”？

           2011年3月6日，央视午间《新闻30分》在播报“新国家博物馆即将开馆”的新闻时，主持人将“铸铜司母戊鼎”播为“后母戊鼎”。“司母戊鼎缘何变成了后母戊鼎？”不少观众颇感疑惑，并通过不同方式向央视求证。随即，该节目官方微博回应：主持人没有错，播前已作核实，其实考古界早已将世界上最大青铜器的姓氏由“司”更正为“后”了。3月11日，北京某媒体称：国家博物馆相关部门负责人表示，司母戊大方鼎国宝将入驻国博青铜厅，入驻“新家”的同时，它也将被正式更名为“后母戊鼎”。

  </span>
</div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        'http://c.hiphotos.baidu.com/baike/pic/item/5882b2b7d0a20cf4035ff0bb72094b36adaf9982.jpg',
        'http://img.sanhao.com/community_news/3278/20160730144309165.jpg',
        'http://www.dugoogle.com/uploads/allimg/171103/6_171103182332_1.jpg',
      ],
    };
  },
};

</script>

<style>
.lb{
  font-size: 15px;
}
</style>
