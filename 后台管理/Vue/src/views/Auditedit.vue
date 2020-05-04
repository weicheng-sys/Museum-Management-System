<template slot-scope="props">
<!--    <el-form style="width: 60%" ref="form" :model="ruleForm"  label-width="120px" >-->

<!--          <el-form-item label="视频编号">-->
<!--            <span>{{ props.vid }}</span>-->
<!--          </el-form-item>-->
<!--          <el-form-item label="账号">-->
<!--            <span>{{ props.uid }}</span>-->
<!--          </el-form-item>-->
<!--          <el-form-item label="博物馆编号">-->
<!--            <span>{{ props.mid }}</span>-->
<!--          </el-form-item>-->

<!--          <el-form-item label="视频名">-->
<!--            <span>{{ props.vname }}</span>-->
<!--          </el-form-item>-->

<!--          <el-form-item label="视频介绍">-->
<!--            <span>{{ props.vinfo }}</span>-->
<!--          </el-form-item>-->

<!--            <el-form-item label="视频">-->
<!--                <span><video :src='props.vaddr'></video></span>-->
<!--            </el-form-item>-->

<!--        <el-form-item>-->
<!--            <el-button type="" @click="pass(props.vid)">通过</el-button>-->
<!--            <el-button type="" @click="fail(props.vid)">不通过</el-button>-->

<!--        </el-form-item>-->
<!--    </el-form>-->

    <el-form style="width: 60%" ref="form" :model="ruleForm"  label-width="120px" >
        <el-form-item label="视频编号">
            <el-input v-model="ruleForm.vid" readOnly></el-input>
        </el-form-item>

        <el-form-item label="用户编号" prop="mname">
            <el-input v-model="ruleForm.uid" readonly></el-input>
        </el-form-item>

        <el-form-item label="博物馆编号">
            <el-input v-model="ruleForm.mid" readonly></el-input>
        </el-form-item>

        <el-form-item label="视频名">
            <el-input v-model="ruleForm.vname" readonly></el-input>
        </el-form-item>

        <el-form-item label="视频介绍">
            <el-input type="textarea" v-model="ruleForm.vinfo" readonly></el-input>
        </el-form-item>

        <el-form-item label="视频" >
            <video :src="ruleForm.vaddr" ></video>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="pass(ruleForm.vid)">通过</el-button>
            <el-button type="primary" @click="fail(ruleForm.vid)">不通过</el-button>
        </el-form-item>
    </el-form>


</template>

<script>
    export default {
        data() {
            return {
                ruleForm: {}
            }
        },

        methods: {
            //审核
            pass(vid) {
                const _this = this
                //测试
                console.log(vid)
                _this.axios.get('/video/pass?vid=' + vid).then(
                    function (resp) {
                        if (resp.data.result == 'success') {
                            _this.$alert(resp.data.msg,
                                {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/Audit')
                                    }
                                })
                        } else _this.$alert(resp.data.msg)

                    })


            },
            fail(vid) {
                const _this = this
                //测试
                console.log(vid)
                _this.axios.get('/video/fail?vid=' + vid).then(
                    function (resp) {
                        if (resp.data.result == 'success') {
                            _this.$alert(resp.data.msg,
                                {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/Audit')
                                    }
                                })
                        } else _this.$alert(resp.data.msg)

                    })


            },
        },

            created() {
                const _this = this
                console.log('收到'+_this.$route.query.vid)
                _this.axios.get('/video/findByvid?vid=' + _this.$route.query.vid).then(function (resp) {
                    _this.ruleForm = resp.data
                })
            },
            watch: {
                // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
                '$route': 'getParams'
            },

    }
</script>
