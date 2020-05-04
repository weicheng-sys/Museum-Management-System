<template>
    <div>
        <el-table :data="tableData"
                  style="width: 100%">

            <el-table-column
                    label="视频编号"
                    prop="vid">
            </el-table-column>

            <el-table-column
                    label="视频名"
                    prop="vname">
            </el-table-column>
            <!--搜索框-->
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-input
                            v-model="search"
                            size="small"
                            placeholder="输入关键字进行搜索"
                            clearable
                            @clear="clear">

                        <el-select v-model="select" slot="prepend" placeholder="请选择" style="width:130px" >
                            <el-option label="视频名称" value=1></el-option>
                            <el-option label="用户名称" value=2></el-option>
                            <el-option label="博物馆名称" value=3></el-option>
                        </el-select>
                        <el-button
                                slot="append"
                                icon="el-icon-search"
                                @click="findByKey(search,select)">
                        </el-button>
                    </el-input>
                </template>

                <!--修改删除按钮-->
                <template slot-scope="scope">
                    <el-button
                            type=""
                            size="small"
                            @click="Edit(scope.row)">修改</el-button>
                    <el-button
                            type="danger"
                            size="small"
                            @click="Delete(scope.row)">删除</el-button>
                </template>
            </el-table-column>

        </el-table>

        <!--分页-->
        <el-pagination
                v-if="pageshow"
                background
                layout="prev, pager, next"
                :page-size="10"
                :total="length"
                :current-page="currentpage"
                @current-change="page">
        </el-pagination>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                pageshow:true,
                currentpage:1,
                t:'',
                allData:[],
                All:[],
                tableData:[],
                search: '',
                select:'',
                length:null
            }
        },
        methods: {
            //编辑
            Edit(row) {
                this.$router.push({
                    path:'/page3edit',
                    query:{
                        vid:row.vid//跳转页面
                    }
                })
            },
            Delete(row) {
                const _this=this
                //测试
                //console.log(row)
                _this.axios.get('/video/delete?vid='+row.vid).then(function(resp){
                    //console.log(resp.data)
                    if(resp.data.result=='success') {
                        _this.$alert('删除成功', '消息', {
                            confirmButtonText: '确定',
                            callback: action => {
                                window.location.reload()
                            }
                        })
                    }
                    else
                        _this.$alert(resp.data.msg)
                    // if(resp.data.result=='success') {
                    //     alert(resp.data.msg)
                    // }
                    //
                    // else alert(resp.data.msg)

                })
            },

            //查询
            findByKey(search,select){
                const _this=this
                //console.log(this.search,this.select)
                this.currentpage=1
                this.pageshow=false

                //按视频名查询 vname
                if(select==1)
                {
                    //console.log(this.search,this.select,"视频名")
                    this.axios.get('/video/findByvname?vname='+search).then(function (response) {
                        _this.tableData=[]
                        _this.tableData.push(response.data)
                        _this.length=1
                        _this.pageshow=true
                    })
                }
                //按用户名查询 uname
                else if(select==2)
                {
                    //console.log(this.search,this.select,"用户名")
                    this.axios.get('/video/findByuname?uname='+search).then(function (response) {
                        _this.allData=response.data
                        _this.length=response.data.length
                        if(response.data.length>10)
                            _this.tableData=_this.allData.slice(0,9)
                        else
                            _this.tableData=_this.allData
                        _this.pageshow=true
                    })
                }
                //按博物馆名查询 mname
                if(select==3)
                {
                    //console.log(this.search,this.select,"博物馆名")
                    this.axios.get('/video/findBymname?mname='+search).then(function (response) {
                        _this.allData=response.data
                        _this.length=response.data.length
                        if(response.data.length>10)
                            _this.tableData=_this.allData.slice(0,9)
                        else
                            _this.tableData=_this.allData
                        _this.pageshow=true
                    })
                }
            },

            clear(){
                this.currentpage=1
                this.allData=this.All
                this.tableData=this.allData.slice(0,9)
                this.length=this.allData.length
                this.pageshow=false

                //改变后再显示
                this.$nextTick(() => {
                    this.pageshow = true
                })
            },


            //分页
            page(currentPage){
                // alert(currentPage)
                // console.log(this.currentpage)
                this.tableData=this.allData.slice((currentPage-1)*10,currentPage*10-1)

            }
        },

        created(){
            const _this=this
            //前后端对接 获取数据
            this.axios.get('/video/findAll_passed').then(function(response){
                //console.log(response);
                _this.All=response.data
                _this.length=response.data.length
                _this.allData=response.data
                _this.tableData=_this.allData.slice(0,9)
            })

        }
    }
</script>

<style scoped>

</style>
