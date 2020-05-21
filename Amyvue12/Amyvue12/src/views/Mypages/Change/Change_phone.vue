<<template>
<div>
    <van-nav-bar title="修改联系方式" left-text="返回" left-arrow @click-left="onClickLeft" />

    <van-cell-group>
        <van-form>
            <van-field v-model="this.user.phone" center type="tel" name="validator" label="联系方式" :placeholder="this.user.phone" @input="getValue" :rules="[{validator, message: '请填写正确的手机号码' }]">

            </van-field>
        </van-form>
    </van-cell-group>
    <div>
        <van-button size="small" type="primary" @click="change_phone">保存</van-button>
    </div>
</div>
</template>

<script>
import Toast from 'vant'
export default {
    name: "Change_phone",
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
            const _this = this

            _this.$router.push('/Portrait');
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
        validator(val) {
            return /1\d{10}/.test(val);
        },

        getValue(e) {
            this.user.phone = e;
        },

        change_phone() {
            const _this = this;
            this.$axios.put("http://39.98.108.11:8081/user/update", _this.user).then((res) => {
                _this.$router.push('/Portrait');

            });
        }
    },
}
</script>

<style >

</style>
