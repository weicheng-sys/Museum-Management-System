<<template>
    <div>
 <van-form @submit="onSubmit">

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
        <van-button round block type="info" native-type="submit" @click='change_gender'>
            保存修改
        </van-button>
    </div>

    </div>
</template>  

<script>
import Toast from 'vant'
export default {
    name:"Change_gender",
    data() {
        return {
            user:{
                uid:'',
                gender:'',
                uname:'',
                phone:'',
                upwd:'',
                icon:'',
                introduction:'',
            },
        }
    },
    mounted(){
    this.getuser();
    },

    methods: {

         getuser(){
            const _this=this;
            this.$axios.get('http://localhost:8089/user/findAll').then((results)=>{
            _this.user.uname=results.data.results.uname;
            _this.user.uid=results.data.results.uid;
            _this.user.gender=results.data.results.gender;
            // if(results.data.results.gender==0)
            // _this.user.gender='女';
            // else{ _this.user.gender='男'}
            _this.user.upwd=results.data.results.upwd;
            _this.user.phone=results.data.results.phone;
            _this.user.icon=results.data.results.icon;
            _this.user.introduction=results.data.results.introduction;
         Toast(results.data.results.uname);

        });

        },

onSubmit(values){

this.user.gender=values.gender;
},
// getValue(e){

// this.user.gender=e;
// },

        change_gender(){
          
const _this=this;
    this.$axios.put("http://localhost:8089/user/update",_this.user).then((res)=>{
        console.log("update之后的： "+JSON.stringify(_this.user));
        console.log('put！'+JSON.stringify(res.data));     
     //   Toast(JSON.stringify(res.data.msg));   
         _this.$router.push('/Portrait');

  });
        }
    },
}
</script>



<style >
    

</style>
         
         
         
         
         
         
         
         
         
         
