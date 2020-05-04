<template>
    <div>
    <el-table
            :data="tableData"
            style="width: 100%">
        <el-table-column
                prop="uid"
                label="编号">
        </el-table-column>

        <el-table-column
                prop="uname"
                label="账号">
        </el-table-column>

        <el-table-column align="right">
            <template slot="header" slot-scope="scope">
                <el-input
                        v-model="search"
                        size="small"
                        placeholder="输入用户账号进行搜索"
                        clearable
                        @keyup.enter.native="findByname(search)"
                        @clear="clear"
                />
            </template>
            <template slot-scope="scope">
                <el-button @click="edit(scope.row)" type="" size="small">修改</el-button>
                <el-button @click="deleteUsr(scope.row)" type="danger" size="small">删除</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination
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
        methods: {
            findByname(search){
                const _this=this


                //console.log(search)
                this.axios.get('/user/findByname?uname='+search).then(function (response) {
                    //console.log(response)
                   _this.tableData=response.data
                    _this.currentpage=1
                    _this.length=1
                })
            },
            deleteUsr(row){ //将要删除的数据请求后端
                const _this = this
                _this.axios.get('/user/delete?uid='+row.uid).then(function (resp) {
                    if(resp.data.result=='success') {
                        _this.$alert('删除成功', '消息', {
                            confirmButtonText: '确定',
                            callback: action => {
                                window.location.reload()
                            }
                        })
                    }
                    else alert(resp.data.msg)

                })
            },
            edit(row) {
                this.$router.push({ //跳转至修改页面
                    path: '/Changeusr',
                    query: {
                        uid: row.uid
                    }
                })
            },

            input(){
                this.$forceUpdate()
            },
            clear(){
                this.currentpage=1
                this.tableData=this.allData.slice(0,9)
                this.length=this.allData.length
            },
            page(currentPage){
                const _this = this //从下方地址的后端接口取得全部返回值（后端页面）需要axios组件

                this.tableData=this.allData.slice((currentPage-1)*10,currentPage*10-1)
            }
        },
        created() {
            const _this = this //get请求取得以下特定后端接口页面的返回值
            this.axios.get('/user/findAll').then(function (response) {
                _this.length=response.data.length
                _this.allData=response.data
                _this.tableData=_this.allData.slice(0,9)
            })
        },

        data() {
            return {//初始置空等待请求返回值
                allData:[],
                currentpage:1,
                tableData: [],
                search:'',
                length:null
            }
        }
    }
</script>