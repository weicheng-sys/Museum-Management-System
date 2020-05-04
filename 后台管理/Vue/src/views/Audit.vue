<template>
    <div>
        <el-table
                :data="tableData"
                style="width: 100%">
            <el-table-column
                    fixed
                    prop="vid"
                    label="序号"
                    >
            </el-table-column>
            <el-table-column
                    prop="vname"
                    label="名称"
                    >
            </el-table-column>
            <el-table-column
                    fixed="right"
                    label="操作"
                    >
                <template slot-scope="scope">
                    <el-button @click="audit(scope.row)"  size="big">审核</el-button>
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
            audit(row) {
                console.log('传出：'+row.vid)
                this.$router.push({ //跳转至审核页面
                    path: './Auditedit',
                    query: {
                        vid: row.vid
                    }
                })
            },
            page(currentPage){
                const _this = this //从下方地址的后端接口取得全部返回值（后端页面）需要axios组件

                this.tableData=this.allData.slice((currentPage-1)*10,currentPage*10-1)
            }
        },
        created() {
            const _this = this //get请求取得以下特定后端接口页面的返回值
            this.axios.get('/video/findAll_ready').then(function (response) {
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
                length:null
            }
        }
    }
</script>