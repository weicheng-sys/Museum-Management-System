<template>
  <div>
        <el-table :data="tableData"
                style="width: 100%">

            <el-table-column
                    label="博物馆编号"
                    prop="mid">
            </el-table-column>

            <el-table-column
                    label="博物馆"
                    prop="mname">
            </el-table-column>
            <!--搜索框-->
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-input
                            v-model="search"
                            size="small"
                            placeholder="输入博物馆名字进行搜索"
                            clearable
                            @keyup.enter.native="findBymname(search)"
                            @clear="clear"
                    />
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
                length:null
            }
        },
        methods: {
            //编辑
            Edit(row) {
                this.$router.push({
                    path:'./page1edit',
                    query:{
                        mid:row.mid//跳转页面
                    }
                })
            },
            //删除 row->对象
            Delete(row) {
                const _this=this
                //测试
                //console.log(row)
                _this.axios.get('/museum/delete?mid='+row.mid).then(function(resp){
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

            findBymname(search){
                const _this=this

                //console.log(this.search)
                this.currentpage=1
                this.pageshow=false
                this.axios.get('/museum/findBymname?mname='+search).then(function (response) {

                     _this.allData=response.data
                    _this.length=response.data.length

                    if(response.data.length>10)
                        _this.tableData=_this.allData.slice(0,9)

                    else

                        _this.tableData=_this.allData
                    _this.pageshow=true
                })

            },

            clear(){
                this.currentpage=1
                this.allData=this.All
                this.tableData=this.allData.slice(0,9)
                this.length=this.allData.length
                this.pageshow=false

                //改变后再改变
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
            this.axios.get('/museum/findAll').then(function(response){
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
