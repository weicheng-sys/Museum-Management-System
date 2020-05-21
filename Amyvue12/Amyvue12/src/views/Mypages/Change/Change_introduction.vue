<<template>
<div>
    <van-nav-bar title="修改简介" left-text="返回" left-arrow @click-left="onClickLeft" />
    <van-cell-group>
        <van-field v-model="this.user.introduction" rows="2" autosize label="个人简介" type="textarea" maxlength="50" placeholder="请输入个人简介" show-word-limit @input="getValue" />

        </van-field>
    </van-cell-group>

    <van-button size="small" type="primary" @click="change_introduction">保存</van-button>

</div>
</template>

<script>
import Toast from 'vant'
export default {
    name: "Change_introduction",
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
                //  Toast(results.data.results.uname);

            });

        },

        getValue(e) {

            this.user.introduction = e;
            

        },

        change_introduction() {

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
