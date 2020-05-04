<template>
    <div>
        <el-form style="width: 60%" ref="form" :model="form"  label-width="120px" >
            <el-form-item label="新闻编号">
                <el-input v-model="form.nid" readOnly></el-input>
            </el-form-item>

            <el-form-item label="新闻标题" prop="title">
                <el-input v-model="form.title"></el-input>
            </el-form-item>

            <el-form-item label="新闻内容" prop="content">
                <el-input type="textarea" v-model="form.content"></el-input>
            </el-form-item>

            <el-form-item label="发布方">
                <el-input v-model="form.publisher"></el-input>
            </el-form-item>

            <el-form-item label="发布时间">
                <el-input v-model="form.ntime"></el-input>
            </el-form-item>

            <el-form-item label="涉及博物馆名" prop="mname">
                <el-input v-model="form.mname"></el-input>
            </el-form-item>

            <el-form-item label="新闻评价">
                <el-input v-model="form.evaluation"></el-input>
            </el-form-item>

            <el-form-item label="爬取源" prop="source">
                <el-input v-model="form.source"></el-input>
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
                        _this.axios.post('/museum/news/update',_this.form).then(function(resp){
                            if(resp.data.result=='success') {
                                _this.$alert('修改成功', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/page2')
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
                _this.$router.push('/page2')//跳转页面
            },
        },
        created:function(){
            const _this=this
            const nid = this.$route.query.nid;
            //console.log("传来的参数=="+nid)
            _this.axios.get('/museum/news/findBynid?nid='+nid).then(function(resp){
                //console.log(resp.data);
                _this.form=resp.data
            })

        },
        watch: {
            // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
            '$route': 'getParams'
        }
    }
</script>
