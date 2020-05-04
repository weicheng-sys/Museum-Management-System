
<<template>
    <div class='register-div'>

<van-form >
<!-- <van-field
    v-model="user.uid"
    name="uid"
    label="账号"
    placeholder="账号"
    :rules="[{ required: true, message: '请填写账号' }]"
  />-->
  <van-field
    v-model="user.uname"
    name="uname"
    label="用户名"
    placeholder="user.uname"
    :rules="[{ required: true, message: '请填写用户名' }]"
  />
  <van-field
    v-model="user.upwd"
    type="password"
    name="upwd"
    label="密码"
    placeholder="密码"
  
  />
   <van-field
    v-model="user.phone"
    type="tel"
    name="手机号码"
    label="手机号码"
    placeholder="手机号码"
    :rules="[{ required: true, message: '请填写正确的手机号码' }]"
  />
  <van-field name="性别" label="性别">
  <template #input>
    <van-radio-group v-model="user.gender" direction="horizontal">
      <van-radio name="0">女</van-radio>
      <van-radio name="1">男</van-radio>
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
  name:'Register',
  data() {
    return {
      
      username: '',
      password: '',
      tel:'',
      gender:'女',
      
      pattern: /\d{6}/,
      user:{
        upwd:'',
        uname:'',
        gender:'',
        phone:'',
        authority:'0',
        // authority:'',
        // introduction:'',
       icon:'https://img.yzcdn.cn/vant/cat.jpeg',
      //  icon:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588920619&di=2a8c86bc38f2e77f180488820bfd1457&imgtype=jpg&er=1&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F1e2e62e6f57458ca32394a10211a9616498d25bd5459-K2uzdk_fw658',
      },
    };
  },
  methods: {
    onSubmit(values) {
     //const _this=this;
        //  Axios.get('http://localhost:8089/user/findAll').then(function (resp) {
        //     _this.user = resp.data.result;
        // })

//console.log('post前的用户'+_this.newuser.uname);
      //console.log('submit', values);
    
       // console.log(_this.newuser);
      //  _this.newuser=res.data;
      //   console.log('post后的用户'+_this.newuser);
   
    
    
      },
  
  onsave(){
  

    const _this=this;
    console.log(_this.user);
    Axios.get('http://localhost:8089/user/register?uname='+_this.user.uname).then(function (resp) {
       if(resp.data!=0)
       {
         Toast("该用户名已经被注册过了,请更换用户名");
  //           Axios.put("http://localhost:8089/user/update",_this.user).then((res)=>{
  //       console.log('put！'+res.data);        
  // });
       }
       
       else{
         console.log("提交的数据！"+_this.user);
  Axios.post("http://localhost:8089/user/add",_this.user).then((res)=>{
          
          
        console.log('post结果！'+res.data.msg);   
        // _this.$router.push('/Home');   



         Axios.get('http://localhost:8089/user/login', {
                params: {
                    uname: _this.user.uname,
                    upwd: _this.user.upwd,
                }
            }).then(result => {
                Toast(result.data.msg);
                console.log(result.data.success);
                console.log(JSON.stringify(result.data));

                if (result.data.success) {
                    Axios.get('http://localhost:8089/user/findAll').then((results) => {
                        console.log("findAll" + JSON.stringify(results.data));
                        console.log("findAll" + results.data.msg);

                        _this.$router.push('/Home');
                    });

                }
                console.log(result.data.msg);
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
.register-div{
    width:450px;
    height:300px;
    background-color:#fff;
    border-radius:1px 1px;
    position: absolute;
     top: 50%;
    left: 50%;
   transform: translate(-50%,80%);
}

  
</style>
