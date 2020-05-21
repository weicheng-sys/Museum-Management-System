<<template>
<div>
    <van-nav-bar title="修改姓名" left-text="返回" left-arrow @click-left="onClickLeft" />
    <van-cell-group>
        <van-field v-model="this.user.uname" center label="用户名" :placeholder="this.user.uname" @input="getValue">
            <template #button>
                <van-button size="small" type="primary" @click="change_name">保存</van-button>
            </template>
        </van-field>
    </van-cell-group>
</div>
</template>

<script>
import {
    Toast
} from 'vant';
export default {
    name: "Change_name",
    data() {
        return {
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

                _this.user.upwd = results.data.results.upwd;
                _this.user.phone = results.data.results.phone;
                _this.user.icon = results.data.results.icon;
                _this.user.introduction = results.data.results.introduction;
                Toast(results.data.results.uname);

            });

        },
        getValue(e) {

            this.user.uname = e;
        },

        change_name() {

            const _this = this;
            _this.$axios.get('http://39.98.108.11:8081/user/register?uname=' + _this.user.uname).then(function (resp) {
                if (resp.data != 0) {

                    Toast('该用户名已经被注册过了,请更换用户名');
                } else {
                    _this.$axios.put("http://39.98.108.11:8081/user/update", _this.user).then((res) => {

                        _this.$router.push('/Portrait');

                    });
                }
            });

        }
    },
}
</script>

<style >

</style>
