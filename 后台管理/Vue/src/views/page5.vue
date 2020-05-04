<template>
    <div>
        <el-table
                :data="tableData"
                style="width: 100%">
            <el-table-column
                    fixed
                    prop="uname"
                    label="管理员账号"
                    >
            </el-table-column>
            <el-table-column
                    prop="upwd"
                    label="管理员密码"
                    >
            </el-table-column>
            <el-table-column
                    label="操作"
                    >
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

        <el-form style="width: 60%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="管理员账号" prop="uname">
                <el-input v-model="ruleForm.uname"></el-input>
            </el-form-item>

            <el-form-item label="管理员密码" prop="upwd">
                <el-input v-model="ruleForm.upwd"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">添加</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        methods: {
            deleteUsr(row){ //将要删除的数据请求后端
                const _this = this
                _this.axios.get('/admin/delete?uid='+row.uid).then(function (resp) {
                    if(resp.data.result=='success'){
                        _this.$alert('删除成功', '成功', {
                            confirmButtonText: '确定',
                            callback: action => {
                                window.location.reload()
                            }
                        })
                    }
                    else _this.$alert(resp.data.msg)

                })
            },
            edit(row) {//取得id
                this.$router.push({ //跳转至修改页面
                    path:'/change',
                    query:{
                        uid:row.uid
                    }
                })
            },
            page(currentPage)
            {
                const _this = this //从下方地址的后端接口取得全部返回值（后端页面）需要axios组件

                this.tableData=this.allData.slice((currentPage-1)*10,currentPage*10-1)
            },
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) { //回调，将表单输入数据传送给后端存储接口
                        _this.axios.post('/admin/add',_this.ruleForm).then(function (resp) {
                            if (resp.data.result == 'success'){  //如取得来自后端的接收成功信号'success'
                                _this.$alert('添加成功', '成功', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        window.location.reload()
                                    }
                                })
                            }
                            else _this.$alert(resp.data.msg)
                        })
                    } else {
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        },
        created() {
            const _this = this //get请求取得以下特定后端接口页面的返回值
            this.axios.get('/admin/findAll').then(function (response) {
                _this.length=response.data.length
                _this.allData=response.data
                _this.tableData=_this.allData.slice(0,9)
            })
        },

        data() {
            return {
                //预设空值等待参数传递
                length:null,
                allData:[],
                tableData: [],
                currentpage:1,
                //添加表单的校验规则
                ruleForm: {
                },
                rules: {
                    uname: [
                        { required: true, message: '管理员账号不能为空', trigger: 'blur' },
                        { min: 5,  message: '长度不少于5', trigger: 'blur' }
                    ],
                    upwd: [
                        { required: true, message: '管理员密码不能为空', trigger: 'blur' },
                        { min: 5,  message: '长度不少于5', trigger: 'blur' }
                    ]
                }
            }
        },
    }
</script>