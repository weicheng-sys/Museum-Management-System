<template>
    <el-form style="width: 60%" :model="ruleForm"  ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="账号" prop="uname">
            <el-input v-model="ruleForm.uname"></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="upwd">
            <el-input v-model="ruleForm.upwd"></el-input>
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
                       _this.axios.post('/admin/update',this.ruleForm).then(function (resp) {
                            if (resp.data.result == 'success'){  //如取得来自后端的接收成功信号'success'
                                _this.$alert('修改成功', '成功', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/page5')
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
                _this.$router.push('/page5')//跳转页面
            },
        },
        created() {
            const _this = this
            _this.axios.get('/admin/findByid?uid='+_this.$route.query.uid).then(function (resp) {
                _this.ruleForm = resp.data
            })
        },
        watch: {
            // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
            '$route': 'getParams'
        },

        data() {
            return {
                //添加表单的校验规则
                ruleForm: {
                },
                rules: {
                    uname: [
                        { required: true, message: '账号不能为空', trigger: 'blur' },
                        { min: 6, max: 6, message: '长度为6个数字', trigger: 'blur' }
                    ],
                    upwd: [
                        { required: true, message: '密码不能为空', trigger: 'blur' },
                        { min: 6, max: 6, message: '长度为6个数字', trigger: 'blur' }
                    ]
                }
            }
        },
    }
</script>

<style scoped>

</style>