<<template>
<div class='register-div'>

    <van-form>
        <van-field v-model="user.uname" name="uname" label="用户名" placeholder="请输入用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
        <van-field v-model="user.upwd" type="password" name="upwd" label="密码" placeholder="密码" :rules="[{ required: true, message: '请填写密码' }]" />
        <van-field v-model="user.phone" type="tel" name="validator" label="手机号码" placeholder="手机号码" :rules="[{validator, message: '请填写正确的手机号码' }]" />
        <van-field name="性别" label="性别">
            <template #input>
                <van-radio-group v-model="user.gender" direction="horizontal">
                    <van-radio name="女">女</van-radio>
                    <van-radio name="男">男</van-radio>
                </van-radio-group>
            </template>
        </van-field>

    </van-form>

    <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit" @click='onsave'>
            立即注册
        </van-button>
    </div>
</div>
</template>

<script>
import Axios from 'axios'
import {
    Toast
} from 'vant';

export default {
    name: 'Register',
    data() {
        return {

            username: '',
            password: '',
            tel: '',
            gender: '女',

            user: {
                upwd: '',
                uname: '',
                gender: '',
                phone: '',
                authority: 0,
                icon: null,

            },
        };
    },
    methods: {
        onsave() {
          const  _this=this;
            Axios.get('http://39.98.108.11:8081/user/register?uname=' + _this.user.uname).then(function (resp) {
                if (resp.data != 0) {
                    Toast("该用户名已经被注册过了,请更换用户名");
                } else {

                    Axios.post("http://39.98.108.11:8081/user/add", _this.user).then((res) => {

                        Axios.get('http://39.98.108.11:8081/user/login', {
                            params: {
                                uname: _this.user.uname,
                                upwd: _this.user.upwd,
                            }
                        }).then(result => {
                            Toast(result.data.msg);
                            if (result.data.success) {
                                Axios.get('http://39.98.108.11:8081/user/findAll').then((results) => {
                                    _this.$router.push('/Home');
                                });

                            }
                        });
                    });

                }

            })

        },
        // 校验函数返回 true 表示校验通过，false 表示不通过
        validator(val) {
            return /1\d{10}/.test(val);
        },
        // 异步校验函数返回 Promise
        asyncValidator(val) {
            return new Promise((resolve) => {
                Toast.loading('验证中...');

                setTimeout(() => {
                    Toast.clear();
                    resolve(/\d{6}/.test(val));
                }, 1000);
            });
        },
    },

};
</script>

<style>
.register-div {
    width: 300px;
    height: 300px;
    background-color: #fff;
    border-radius: 1px 1px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, 30%);
}
</style>
