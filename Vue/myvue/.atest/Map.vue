<template>
<div id="app">
    <van-nav-bar title="地图导航" left-text="返回主页" right-text="按钮" left-arrow @click-left="onClickLeft" @click-right="onClickRight" />

    <div id="allmap" class="Map" />

</div>
</template>

<script>
/* eslint-disable*/
import Header from "../../components/header/Header";
import {
    Toast
} from 'vant';



//  var map = new BMap.Map("allmap"); //创建Map实例，初始化map, 绑定id=allmap
//         map.centerAndZoom("中国", 12); //初始化时，即可设置中心点和地图缩放级别。
//         //map.centerAndZoom(new BMap.Point(116.4035,39.915),8);
//         map.enableScrollWheelZoom(true); //允许鼠标滑轮
function loadJScript() {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "//api.map.baidu.com/api?v=2.0&ak=ArstD00t0HWNiwuMlIL0ZWrUscyFVu0R&callback=init";
    document.body.appendChild(script);
}
// function init() {
//     var map = new BMap.Map("allmap"); // 创建Map实例
//     var point = new BMap.Point(116.404, 39.915); // 创建点坐标
//     map.centerAndZoom(point, 15);
//     map.enableScrollWheelZoom(); //启用滚轮放大缩小
// }
window.onload = loadJScript; //异步加载地图


export default {

    name: "Map-test", //map-test组件
    components: {
        Header
    },
    data() {
        return {};
    },

    mounted: function () {

        // // 百度地图API功能
        var map = new BMap.Map("allmap"); //创建Map实例，初始化map, 绑定id=allmap
        map.centerAndZoom("中国", 12); //初始化时，即可设置中心点和地图缩放级别。
        //map.centerAndZoom(new BMap.Point(116.4035,39.915),8);
        map.enableScrollWheelZoom(true); //允许鼠标滑轮



        //直线距离：
        // var map = new BMap.Map("allmap");
        // map.centerAndZoom("重庆",12);  //初始化地图,设置城市和地图级别。
        // var pointA = new BMap.Point(106.486654,29.490295);  // 创建点坐标A--大渡口区
        // var pointB = new BMap.Point(106.581515,29.615467);  // 创建点坐标B--江北区
        // alert('从大渡口区到江北区的距离是：'+(map.getDistance(pointA,pointB)).toFixed(2)+' 米。');  //获取两点距离,保留小数点后两位
        // var polyline = new BMap.Polyline([pointA,pointB], {strokeColor:"blue", strokeWeight:6, strokeOpacity:0.5});  //定义折线
        // map.addOverlay(polyline);     //添加折线到地图上




        //导航控制组件，加入的控件
        map.addControl(new BMap.NavigationControl());
        map.addControl(new BMap.ScaleControl());
        map.addControl(new BMap.OverviewMapControl());
        map.addControl(new BMap.MapTypeControl());


        //获取当前个人定位
        var geolocation = new BMap.Geolocation();
        var ce_lng;
        var ce_lat; //用来给定地图中心的，把当前个人定位的位置作为中心了
        var personal_loc;
        var personal_point;
        geolocation.enableSDKLocation(); //sdk辅助定位
        geolocation.getCurrentPosition(function (r) {
            if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                var mk = new BMap.Marker(r.point); //添加标注
                map.addOverlay(mk);
                map.panTo(r.point); //平滑的移动到指定点

                personal_point = r.point;
                ce_lat = r.lat;
                ce_lng = r.lng;

                // 根据坐标得到地址描述，----逆地址解析
                var myGeo = new BMap.Geocoder();
                myGeo.getLocation(new BMap.Point(r.point.lng, r.point.lat), function (result) {
                    if (result) {
                        alert("您的定位: " + result.address);
                        personal_loc = result.address;

                        var label = new BMap.Label("您的位置： " + personal_loc, {
                            offset: new BMap.Size(25, 5)
                        });
                        mk.setLabel(label);

                    }
                });
            } else {
                alert('failed' + this.getStatus());
            }
        });
        var point = new BMap.Point(ce_lng, ce_lat); // 初始化point, 给定经纬度--当前的个人定位,页面中心点
        map.centerAndZoom(point, 6); // 将point点放入map中，展示在页面中心展示，6=缩放程度



        //地址解析--可将对应的博物馆名称直接对应坐标
        var geocoder = new BMap.Geocoder();
        geocoder.getPoint("中国军事博物馆", function (point) {
                if (point) {
                    // map.centerAndZoom(point, 16);
                    var marker = new BMap.Marker(point);
                    map.addOverlay(marker);
                    var label = new BMap.Label("中国人民军事博物馆", {
                        offset: new BMap.Size(25, 5)
                    });
                    marker.setLabel(label);
                } else {
                    alert("您选择地址没有解析到结果!");
                }
            },
            "中国"
        );



        //这个是顺序表吗？let关键字没百度明白，如果是的话里面那些数据能不能单提出来？不是很清楚
        //let data = [{
        //        name: "四川博物院",
        //        location: "某市某区某街道---",
        //    },
        //    {
        //        name: "中国国家博物馆",
        //        location: "某市某区某街道---",
        //    },
        //    {
        //        name: "连云港市博物馆",
        //        location: "某市某区某街道---",
        //    }
        //];



        //遍历data数组，进行地址解析，并且标注，定义点击事件
        var min = 10000000000;
        var museum;
        data.forEach((e, i) => {
            geocoder.getPoint(e.name, function (point) {
                    if (point) {
                        //覆盖物marker与文本标注label
                        var marker = new BMap.Marker(point);
                        map.addOverlay(marker);
                        var label = new BMap.Label(e.name, {
                            offset: new BMap.Size(25, 5)
                        });
                        marker.setLabel(label);

                        var transit = new BMap.DrivingRoute(map, {
                            renderOptions: {
                                map: map
                            },
                            onSearchComplete: function (results) {
                                if (transit.getStatus() != BMAP_STATUS_SUCCESS) {
                                    return;
                                }
                                var plan = results.getPlan(0);
                                // output += plan.getDuration(true) + "\n";        //获取时间
                                // output += "总路程为：" ;
                                output = plan.getDistance(true); // + "\n";       //获取距离
                            },

                            onPolylinesSet: function () {
                                // setTimeout(function(){alert(output+"\n"+i+"\n"+min)},"1000");
                            }
                        });

                        transit.search(personal_point, point);

                        // 创建point, 将x,y值传入到百度地图对象中
                        let pointNumber = new BMap.Point(point.lng, point.lat);
                        // 创建信息窗口对象
                        let infoWindow = new BMap.InfoWindow("地址：" + e.location + i, {
                            width: 150, // 信息窗口宽度
                            height: 100, // 信息窗口高度
                            title: "名称：" + e.name // 信息窗口标题
                        });

                        // 将data中的name加入地图中
                        var label = new BMap.Label(e.name, {
                            offset: new BMap.Size(25, 5)
                        });
                        markerFun(pointNumber, infoWindow, label);

                    } else {
                        alert("您选择地址没有解析到结果!");
                    }
                },
                "中国"
            );
        });



        function markerFun(points, infoWindows, label) {
            let markers = new BMap.Marker(points);
            map.addOverlay(markers); // 将标注添加到地图中
            markers.setLabel(label); // 将data中的name添加到地图中
            // 标注的点击事件
            markers.addEventListener("click", function (event) {
                map.openInfoWindow(infoWindows, points); //参数：窗口、点  根据点击的点出现对应的窗口
                //window.location.href = '../Homes/Home';
                // map.openInfoWindow(infoWindows, points); //参数：窗口、点  根据点击的点出现对应的窗口
                //this.$router.push('/#');

            });

            //双击跳转至主页面
            markers.addEventListener("dblclick", function (event) {
                window.location.href = '../Homes/Home';
                //this.$router.push('/#');
            });
        }


      // 如有多个point去展示，可根据后端接口传入为主
      // let data = [
      //   { x: 120, y: 30, name: "博物馆大哥1号", location: "某市某区某街道---" },
      //   {
      //     x: 121.447254,
      //     y: 31.32362,
      //     name: "博物馆小弟2号",
      //     location: "某市某区某街道---"
      //   },
      //   { x: 120, y: 32, name: "博物馆小弟3号", location: "某市某区某街道---" }
      // ];
      //用这一组数据尝试


function getRad(d){   
   var PI = Math.PI;    
   return d*PI/180.0;    
}
      
        //这里用单独写的函数，百度API那个附带功能有丶多拆不开
        //由经纬度获取直线距离（这段直接粘的网上的算法，网址https://blog.csdn.net/qq_33417035/article/details/78028461）
        function GetLineDistance(lng1,lat1,lng2,lat2)
        {
           var f = getRad((lat1 + lat2)/2);
           var g = getRad((lat1 - lat2)/2);
           var l = getRad((lng1 - lng2)/2);
           var sg = Math.sin(g);
           var sl = Math.sin(l);
           var sf = Math.sin(f);
           var s,c,w,r,d,h1,h2;
           var a = 6378137.0;//The Radius of eath in meter.
           var fl = 1/298.257;
           sg = sg*sg;
           sl = sl*sl;
           sf = sf*sf;
           s = sg*(1-sl) + (1-sf)*sl;
           c = (1-sg)*(1-sl) + sf*sl;
           w = Math.atan(Math.sqrt(s/c));
           r = Math.sqrt(s*c)/w;
           d = 2*w*a;
           h1 = (3*r -1)/2/c;
           h2 = (3*r +1)/2/s;
           s = d*(1 + fl*(h1*sf*(1-sg) - h2*(1-sf)*sg));
           s = s/1000;
           s = s.toFixed(2);//指定小数点后的位数。
             return s;
        }
        //返回距离数值

        //博物馆类，js的类跟C++和java思路不一样，不好面向对象
        function MuseumClass(name,position,longitude,latitude)
        {
            this.Name=name;
            this.Position=position;
            this.Longitude=longitude;
            this.Latitude=latitude;
        }

        //我觉着这些博物馆名称地址还有经纬度最好爬好了一起传进来，百度地图API那些中间变量实在是整不明白怎么提取出来
        //这里直接就用数组当假数据了，爬的数据直接按列赋值到这些数组里？先默认3个（用静态变量？）
        var MuseumName=new Array(3);//博物馆名
        MuseumName[0]="博物馆1";
        MuseumName[1]="博物馆2";
        MuseumName[2]="博物馆3";

        var MuseumPosition=new Array(3);//博物馆地址
        MuseumPosition[0]="博物馆地址1";
        MuseumPosition[1]="博物馆地址2";
        MuseumPosition[2]="博物馆地址3";

        var MuseumLongitude=new Array(3);//经度
        MuseumLongitude[0]="120";
        MuseumLongitude[1]="121.447254";
        MuseumLongitude[2]="120";

        var MuseumLatitude=new Array(3);//纬度
        MuseumLatitude[0]="30";
        MuseumLatitude[1]="31.32362";
        MuseumLatitude[2]="32";
        //这里 ; 需不需要？？？官网为啥没有 ;

        //赋值给三个博物馆类
        var MC1=new MuseumClass(MuseumName[0],MuseumPosition[0],MuseumLongitude[0],MuseumLatitude[0]);
        var MC2=new MuseumClass(MuseumName[1],MuseumPosition[1],MuseumLongitude[1],MuseumLatitude[1]);
        var MC3=new MuseumClass(MuseumName[2],MuseumPosition[2],MuseumLongitude[2],MuseumLatitude[2]);

        //定义起始点，这里定义假数据，应该用定位点，但是前面定位组件里面的变量好像不能拿过来直接用，没找到方法
        var SP=new MuseumClass("起始点","起始点",115,30);//这里是不是应该再定义一个类，先这样凑合一下

        //距离数组
        var Distance=new Array(3);
        Distance[0]=GetLineDistance(SP.Longitude,SP.Latitude,MC1.Longitude,MC1.Latitude);
        Distance[1]=GetLineDistance(SP.Longitude,SP.Latitude,MC2.Longitude,MC2.Latitude);
        Distance[2]=GetLineDistance(SP.Longitude,SP.Latitude,MC3.Longitude,MC3.Latitude);

        //取最小值标号函数
        function indexOfSmallest(a)
        {
           var lowest = 0;
           for (var i = 1; i < a.length; i++)
           {
              if (a[i] < a[lowest]) lowest = i;
           }
           return lowest;
        }

        var index=indexOfSmallest(Distance);

        //依据坐标求驾驶路径
        var p1 = new BMap.Point(SP.Longitude,SP.Latitude);
        var p2 = new BMap.Point(MuseumLongitude[index],MuseumLatitude[index]);
        var driving = new BMap.DrivingRoute(map, {renderOptions:{map: map, autoViewport: true}});
        driving.search(p1, p2);

        //显示路径时间和距离
        var output= "从起始点到终点需要";
        var searchComplete = function (results) {
          if (transit.getStatus() != BMAP_STATUS_SUCCESS) {
            return;
          }
          var plan = results.getPlan(0);
          output += plan.getDuration(true) + "\n"; //获取时间
          output += "总路程为：";
          output = plan.getDistance(true) + "\n"; //获取距离
        }
        var transit = new BMap.DrivingRoute(map, {renderOptions: {map: map},
          onSearchComplete: searchComplete,
          onPolylinesSet: function(){
            setTimeout(function(){alert(output)},"1000");
          }});
        transit.search(p1, p2);

        //如果大量不定量数据的话，只用一个博物馆类变量，把一组数据带进去，由定位点算出距离存入数组
        //循环操作，从数组中找到最小的距离，提取标号作为函数返回值（不知道能不能实现姑且写上）
        //没找到js怎么数组传参，写思路伪码了.....
        //function AntherWay(博物馆数量,博物馆名数组,博物馆地址数组,博物馆经度数组,博物馆纬度数组,MuseumClass类对象起始点)
        //{
        //    var i=0;
        //    var Distance=new Array(博物馆数量);
        //    循环(i=0;i<博物馆数量;i++)
        //    {
        //        var SP=MuseumClass类对象起始点;
        //        var MC=new MuseumClass(MuseumName[i],MuseumPosition[i],MuseumLongitude[i],MuseumLatitude[i]);
        //        Distance[i]=GetLineDistance(SP.longitude,SP.latitude,MC.longitude,MC.latitude);
        //    }
        //    然后这里来一个取数组最小值算法;
        //    return 数组最小值的标号；
        //}






    },
    methods: {

        onClickLeft() {
            Toast('返回主页');
            this.$router.push('/');
        }
    }
};


</script>

<style>
.Map {
    /* height: calc(100vh - 126px); */
    height: 470px;
    width: 100%;
}

#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 2px;
}
</style>
