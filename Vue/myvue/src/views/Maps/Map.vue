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

    name: "Map", //map组件
    data() {
        return {

            museum: [{}],
            min_i: '',
            min_distance: -1,
            min_lng: '',
            min_lat: '',
            ce_lng: '',
            ce_lat: '',
            personal_loc: '',
        };
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

        // var min_i;
        // var min_distance=-1;
        // var min_lng;
        // var min_lat;
        //  var ce_lng;
        // var ce_lat; //用来给定地图中心的，把当前个人定位的位置作为中心了
        //获取当前个人定位
        var geolocation = new BMap.Geolocation();

        //  personal_loc;
        var personal_point;
        geolocation.enableSDKLocation(); //sdk辅助定位
        const _this = this;
        geolocation.getCurrentPosition(function (r) {
            if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                var mk = new BMap.Marker(r.point); //添加标注
                map.addOverlay(mk);
                map.panTo(r.point); //平滑的移动到指定点
                console.log("point " + JSON.stringify(r.point));
                personal_point = r.point;
                _this.ce_lat = r.point.lat;
                _this.ce_lng = r.point.lng;

                console.log('个人定位的维度：' + r.point.lat, r.point.lng);
                console.log('个人的位置LLL' + _this.personal_loc);

                // 根据坐标得到地址描述，----逆地址解析
                var myGeo = new BMap.Geocoder();
                myGeo.getLocation(new BMap.Point(r.point.lng, r.point.lat), function (result) {
                    if (result) {
                        alert("您的定位: " + result.address);
                        _this.personal_loc = result.address;
                        console.log('个人的位置LLL' + _this.personal_loc);
                        var label = new BMap.Label("您的位置： " + _this.personal_loc, {
                            offset: new BMap.Size(25, 5)
                        });
                        mk.setLabel(label);

                    }
                });

                var sum = 0;
                let data = [{}];
                _this.$axios.get('http://localhost:8089/museum/findAll').then((results) => {
                    this.museum = results.data.results;
                    console.log("博物馆们！" + JSON.stringify(results.data.results));
                    //   console.log(this.museum[0].mname);
                    //   console.log(this.museum[1].mname);
                    //   console.log(this.museum[2].mname);
                    //   console.log(this.museum[3].mname);
                    data = this.museum;

                    data.forEach((e, i) => {

                        geocoder.getPoint(e.mname, function (point) {
                                if (point) {

                                    sum = sum + 1;
                                    //计算每个博物馆与当前博物馆的距离
                                    var distance = GetLineDistance(point.lng, point.lat, _this.ce_lng, _this.ce_lat);
                                    console.log(e.mname + '距离我当前的位置的距离为： ' + distance);
                                    console.log("此时的最近距离：" + _this.min_distance);
                                    if (_this.min_distance == -1 || parseInt(_this.min_distance) >= parseInt(distance)) {
                                        console.log("当前最近距离" + _this.min_distance + "需更新为更近的距离：" + distance);
                                        _this.min_distance = distance;
                                        _this.min_i = e.mname;
                                        console.log("min_i: " + _this.min_i);
                                        _this.min_lng = point.lng;
                                        _this.min_lat = point.lat;
                                    }

                                    //覆盖物marker与文本标注label
                                    var marker = new BMap.Marker(point); //marker是红色小点点们
                                    map.addOverlay(marker);

                                    var label = new BMap.Label(e.mname, {
                                        offset: new BMap.Size(25, 5)
                                    });
                                    marker.setLabel(label); //文本标注！？？？？？？

                                    // 创建point, 将x,y值传入到百度地图对象中
                                    let pointNumber = new BMap.Point(point.lng, point.lat);
                                    // 创建信息窗口对象
                                    let infoWindow = new BMap.InfoWindow("地址：" + e.basic_info + "\n" + "距离我当前位置的距离约为" + distance + "公里", {
                                        width: 150, // 信息窗口宽度
                                        height: 100, // 信息窗口高度
                                        title: "名称：" + e.mname // 信息窗口标题
                                    });

                                    // 将data中的name加入地图中
                                    var label = new BMap.Label(e.mname, {
                                        offset: new BMap.Size(25, 5)
                                    });
                                    markerFun(pointNumber, infoWindow, label);

                                    //以上是关于每个博物馆的标注

                                    if (sum == 4) {
                                        var output = "需要";
                                        console.log("当前位置" + _this.personal_loc);
                                        var searchComplete = function (results) {
                                            if (transit.getStatus() != BMAP_STATUS_SUCCESS) {
                                                return;
                                            }
                                            var plan = results.getPlan(0);
                                            output += plan.getDuration(true) + "\n"; //获取时间
                                            output += "总路程为：";
                                            output = plan.getDistance(true) + "\n"; //获取距离
                                        }
                                        var transit = new BMap.DrivingRoute(map, {
                                            renderOptions: {
                                                map: map
                                            },
                                            onSearchComplete: searchComplete,
                                            onPolylinesSet: function () {
                                                console.log("output::" + output);
                                                setTimeout(function () {
                                                    alert(output)
                                                }, "1000");
                                            }
                                        });
                                        // transit.search(min_lng,min_lat,ce_lng,ce_lat);

                                        transit.search(_this.personal_loc, _this.min_i);
                                    }

                                } else {
                                    alert("您选择地址没有解析到结果!");
                                }
                            },
                            "中国"
                        );

                    });

                });

            } else {
                alert('failed' + this.getStatus());
            }
        });
        console.log('个人的位置LLL' + _this.personal_loc);
        var point = new BMap.Point(_this.ce_lng, _this.ce_lat); // 初始化point, 给定经纬度--当前的个人定位,页面中心点
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
                _this.$router.push('/Home');
                // window.location.href = '../Homes/Home';
                //this.$router.push('/#');
            });
        };

        function getRad(d) {
            var PI = Math.PI;
            return d * PI / 180.0;
        }

        function GetLineDistance(lng1, lat1, lng2, lat2) {
            console.log(lng1, lat1, lng2, lat2);
            var f = getRad((lat1 + lat2) / 2);
            var g = getRad((lat1 - lat2) / 2);
            var l = getRad((lng1 - lng2) / 2);
            var sg = Math.sin(g);
            var sl = Math.sin(l);
            var sf = Math.sin(f);
            var s, c, w, r, d, h1, h2;
            var a = 6378137.0; //The Radius of eath in meter.
            var fl = 1 / 298.257;
            sg = sg * sg;
            sl = sl * sl;
            sf = sf * sf;
            s = sg * (1 - sl) + (1 - sf) * sl;
            c = (1 - sg) * (1 - sl) + sf * sl;
            w = Math.atan(Math.sqrt(s / c));
            r = Math.sqrt(s * c) / w;
            d = 2 * w * a;
            h1 = (3 * r - 1) / 2 / c;
            h2 = (3 * r + 1) / 2 / s;
            s = d * (1 + fl * (h1 * sf * (1 - sg) - h2 * (1 - sf) * sg));
            s = s / 1000;
            s = s.toFixed(2); //指定小数点后的位数。
            return s;
        }

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
