<template>
    <div>
        <el-form style="width: 60%" ref="form" :model="form"  label-width="120px" >
            <el-form-item label="博物馆编号">
                <el-input v-model="form.mid" readOnly></el-input>
            </el-form-item>

            <el-form-item label="博物馆名称" prop="mname">
                <el-input v-model="form.mname"></el-input>
            </el-form-item>

            <el-form-item label="评价">
                <el-input type="textarea" v-model="form.evaluate"></el-input>
            </el-form-item>

            <el-form-item label="总评分">
                <el-input v-model="form.grade"></el-input>
            </el-form-item>
            <el-form-item label="展览评分">
                <el-input v-model="form.grade_1"></el-input>
            </el-form-item>
            <el-form-item label="服务评分">
                <el-input v-model="form.grade_2"></el-input>
            </el-form-item>
            <el-form-item label="环境评分">
                <el-input v-model="form.grade_3"></el-input>
            </el-form-item>

            <el-form-item label="基本信息">
                <el-input type="textarea" v-model="form.basic_info"></el-input>
            </el-form-item>

            <el-form-item label="其他信息">
                <el-input type="textarea" v-model="form.other_info"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="Confirm('form')">确认</el-button>
                <el-button type="primary" @click="Cancle('form')">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                form: {

                },
                // rules:{
                //     title:[
                //         {required:true,message:'不能为空',trigger:'blur'}
                //     ],
                //     content:[
                //         {required:true,message:'不能为空',trigger:'blur'}
                //     ],
                //     mname:[
                //         {required:true,message:'不能为空',trigger:'blur'}
                //     ],
                //     source:[
                //         {required:true,message:'不能为空',trigger:'blur'}
                //     ],
                // }
            };
        },
        methods: {
            Confirm(formName) {
                const _this=this
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        //测试
                        // _this.$alert('修改成功', '消息', {
                        //     confirmButtonText: '确定',
                        //     callback: action => {
                        //         _this.$router.push('/page2')
                        //     }
                        // })
                        //前后端对接
                        _this.axios.post('/museum/update',_this.form).then(function(resp){
                            if(resp.data.result=='success') {
                                _this.$alert('修改成功', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/page1')
                                    }
                                })
                            }
                            else _this.$alert(resp.data.msg)

                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },

            Cancle(){
                const _this=this
                _this.$router.push('/page1')//跳转页面
            },
        },
        created(){
            const _this=this
            const mid = this.$route.query.mid;
            console.log(mid)
            //console.log("传来的参数=="+nid)
            _this.axios.get('/museum/findById?mid='+mid).then(function(resp){
                console.log(resp.data);
                _this.form=resp.data
            })

        },
        watch: {
            // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
            '$route': 'getParams'
        }
    }
</script>
