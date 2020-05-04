<<template>
    <div>

<van-cell-group>
<van-field
  v-model="this.user.uname"
  center
  label="用户名"
  :placeholder="this.user.uname"
  @input="getValue"
>
  <template #button>
    <van-button size="small" type="primary"  @click="change_name">保存</van-button>
  </template>
</van-field>
</van-cell-group>
    </div>
</template>  

<script>
import Toast from 'vant'
export default {
    name:"Change_name",
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

// onSubmit(values){

// this.user.uname=values.uname;
// },
getValue(e){

this.user.uname=e;
},

        change_name(){
          
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
         
         
         
         
         
         
         
         
         
         
