<template>
    <el-form :model="ruleForm"  ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="编号" prop="uid">
            <el-input v-model="ruleForm.uid"></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="upwd">
            <el-input v-model="ruleForm.upwd"></el-input>
        </el-form-item>

        <el-form-item label="账号" prop="uname">
            <el-input v-model="ruleForm.uname"></el-input>
        </el-form-item>

        <el-form-item label="性别" prop="gender">
            <el-input v-model="ruleForm.gender"></el-input>
        </el-form-item>

        <el-form-item label="简介" prop="introduction">
            <el-input type="textarea" v-model="ruleForm.introduction"></el-input>
        </el-form-item>

        <el-form-item label="电话" prop="phone">
            <el-input v-model="ruleForm.phone"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">修改</el-button>
            <el-button @click="Cancle()">取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    export default {
        methods: {
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) { //回调，将修改后的数据传送给后端
                        _this.axios.post('user/update',_this.ruleForm).then(function (resp) {
                            if(resp.data.result=='success') {
                                _this.$alert('修改成功', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/page4')
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
            Cancle(){
                const _this=this
                _this.$router.push('/page4')//跳转页面
            },
        },
        created() {
            const _this = this //请求要修改的用户账户uid
            _this.axios.get('/user/findByid?uid='+_this.$route.query.uid).then(function (resp) {
                _this.ruleForm = resp.data
            })
        },
        watch: {
            // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
            '$route': 'getParams'
        },

        data() {
            return {
                //预设空值等待参数传递
                total:null,
                tableData: null,

                ruleForm: {
                },
                rules: {
                    uid: [
                        { required: true, message: '账号不能为空', trigger: 'blur' },
                        { min: 6, max: 6, message: '长度为6个数字', trigger: 'blur' }
                    ],
                    upwd: [
                        { required: true, message: '密码不能为空', trigger: 'blur' },
                        { min: 6, max: 6, message: '长度为6个数字', trigger: 'blur' }
                    ],
                    uname: [
                        { required: true, message: '姓名不能为空', trigger: 'blur' },
                        { min: 2, max: 4, message: '姓名为2到4个汉字', trigger: 'blur' }
                    ],
                    gender: [
                        { required: true, message: '性别不能为空', trigger: 'blur' },
                        { min: 1, max: 1, message: '1个汉字', trigger: 'blur' }
                    ],
                    introduction: [
                        { required: true, message: '介绍不能为空', trigger: 'blur' },
                        { min: 1, max: 500, message: '介绍不能为空', trigger: 'blur' }
                    ],
                    phone: [
                        { required: true, message: '电话不能为空', trigger: 'blur' },
                        { min: 11, max: 11, message: '长度为11个数字', trigger: 'blur' }
                    ]
                }
            }
        },
    }
</script>
