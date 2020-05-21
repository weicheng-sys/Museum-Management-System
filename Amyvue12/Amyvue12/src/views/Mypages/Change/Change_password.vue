<<template>
<div>
    <van-nav-bar title="修改密码" left-text="返回" left-arrow @click-left="onClickLeft" />
    <van-form @submit="onSubmit">

        <van-field v-model="upwd1" type="password" name="upwd" label="原密码" placeholder="请输入原密码" />
        <van-field v-model="upwd2" type="password" name="upwd" label="新密码" placeholder="请输入新密码" />

    </van-form>

    <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit" @click='change_password'>
            保存修改
        </van-button>
    </div>
</div>
</template>

<script>
import {Toast} from 'vant'
export default {
    name: "Change_password",
    data() {
        return {
            upwd1: '',
            upwd2: '',

            user: {
                uid: '',
                gender: '',
                uname: '',
                phone: '',
                upwd: '',
                icon: '',
                introduction: '',
            },
        }
    },
    mounted() {
        this.getuser();
    },

    methods: {
        onClickLeft() {

            this.$router.push('/Portrait');
        },
        getuser() {
            const _this = this;
            this.$axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
                _this.user.uname = results.data.results.uname;
                _this.user.uid = results.data.results.uid;
                _this.user.gender = results.data.results.gender;
                // if(results.data.results.gender==0)
                // _this.user.gender='女';
                // else{ _this.user.gender='男'}
                _this.user.upwd = results.data.results.upwd;
                _this.user.phone = results.data.results.phone;
                _this.user.icon = results.data.results.icon;
                _this.user.introduction = results.data.results.introduction;

            });

        },

        onSubmit(values) {

            this.upwd1 = values.upwd1;
            this.upwd2 = values.upwd2;

        },

        change_password() {

            if (this.user.upwd == this.upwd1) {

                //原密码输入正确
                if (this.upwd2 != this.upwd1) {

                    //可以修改密码
                    const _this = this;
                    _this.user.upwd = _this.upwd2;
                    this.$axios.put("http://39.98.108.11:8081/user/update", _this.user).then((res) => {
                        Toast('密码修改成功')
                        _this.$router.push('/Portrait');

                    });
                } else {
                    Toast('新密码与原密码相同')
                }
            } else {
                Toast('原密码输入错误')
            }

        }
    },
}
</script>

<style >

</style>
