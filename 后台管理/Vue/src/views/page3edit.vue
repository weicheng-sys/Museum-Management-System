<template >
    <el-form style="width: 60%" ref="form" :model="ruleForm"  label-width="120px" >
        <el-form-item label="视频编号">
            <el-input v-model="ruleForm.vid" ></el-input>
        </el-form-item>

        <el-form-item label="用户编号" prop="mname">
            <el-input v-model="ruleForm.uid" ></el-input>
        </el-form-item>

        <el-form-item label="博物馆编号">
            <el-input v-model="ruleForm.mid" ></el-input>
        </el-form-item>

        <el-form-item label="视频名">
            <el-input v-model="ruleForm.vname" ></el-input>
        </el-form-item>

        <el-form-item label="视频介绍">
            <el-input type="textarea" v-model="ruleForm.vinfo" ></el-input>
        </el-form-item>

        <el-form-item label="视频" >
            <video :src="ruleForm.vaddr" ></video>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="Confirm()">修改</el-button>
            <el-button type="primary" @click="Cancle()">取消</el-button>
        </el-form-item>
    </el-form>

</template>

<script>
    export default {
        data() {
            return {
                ruleForm: {

                },
            };
        },
        methods: {
            Confirm() {
                const _this=this

                        _this.axios.post('/video/update',_this.ruleForm).then(function(resp){
                            if(resp.data.result=='success') {
                                _this.$alert('修改成功', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/page3')
                                    }
                                })
                            }
                            else _this.$alert(resp.data.msg)

                        })
                },

            Cancle(){
                const _this=this
                _this.$router.push('/page3')//跳转页面
            },
        },
        created:function(){
            const _this=this
            const vid = this.$route.query.vid;
            //console.log("传来的参数=="+vid)
            _this.axios.get('/video/findByvid?vid='+vid).then(function(resp){
                //console.log(resp.data);
                _this.ruleForm=resp.data
            })

        },
        watch: {
            // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
            '$route': 'getParams'
        }
    }
</script>
