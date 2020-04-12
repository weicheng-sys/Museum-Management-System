<template>
  <div>
    <div class="m-b-20 ovf-hd">
      <div class="fl" v-show="addShow">
        <router-link class="btn-link-large add-btn" to="add">
          <i class="el-icon-plus"></i>&nbsp;&nbsp;添加成员
        </router-link>
      </div>
      <div class="fl w-200 m-l-30">
        <el-input placeholder="请输入姓名" v-model="keywords">
          <el-button slot="append" icon="search" @click="search()"></el-button>
        </el-input>
      </div>
    </div>
    <el-table
    :data="tableData"
    style="width: 100%"
    @selection-change="selectItem">
      <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="姓名">
            <span>{{ props.row.name }}</span>
          </el-form-item>
          <el-form-item label="性别">
            <span>{{ props.row.shop }}</span>
          </el-form-item>
          <el-form-item label="部门">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="学号">
            <span>{{ props.row.shopId }}</span>
          </el-form-item>
          <el-form-item label="专业">
            <span>{{ props.row.category }}</span>
          </el-form-item>
          <el-form-item label="宿舍">
            <span>{{ props.row.address }}</span>
          </el-form-item>
          <el-form-item label="导员">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="出生日期">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="民族">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="籍贯">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="政治面貌">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="现任职务">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          <el-form-item label="联系电话">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
          </el-form-item>
          <el-form-item label="特长和爱好">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      type="selection"
      width="50">
      </el-table-column>
    <el-table-column
      label="部门"
      prop="id"
      :filters="[{text: '学生网络中心', value: '学生网络中心'}, {text: '办公室', value: '办公室'}, {text: '市场部', value: '市场部'}, {text: '宣传部', value: '宣传部'}, {text: '技术部开发组', value: '技术部开发组'}, {text: '技术部平面组', value: '技术部平面组'}, {text: '技术部系统维护组', value: '技术部系统维护组'}, {text: '媒体运营部', value: '媒体运营部'}, {text: '3', value: '3'}]"
      :filter-method="filterHandler">
    </el-table-column>
    <el-table-column
      label="姓名"
      prop="name"
      :formatter="formatter">
    </el-table-column>
    <el-table-column
      label="性别"
      prop="desc"
      :filters="[{text: '男', value: '男'}, {text: '女', value: '女'}]"
      :filter-method="filterHandler">
    </el-table-column>
    <el-table-column
      label="专业"
      prop="desc">
    </el-table-column> 
    <el-table-column
      label="学号"
      prop="account"
      width="200">
    </el-table-column>
    <el-table-column
      label="联系电话"
      prop="desc"
      width="200">
    </el-table-column>
      <el-table-column
      label="操作"
      width="200">
        <template scope="scope">
          <div>
            <span>
              <router-link :to="{ name: 'informationEdit', params: { id: scope.row.id }}" class="btn-link edit-btn">
            编辑
              </router-link>
            </span>
            <span>
              <el-button size="small" type="danger" @click="confirmDelete(scope.row)">删除</el-button>
            </span>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <div class="pos-rel p-t-20">
      <btnGroup :selectedData="multipleSelection" :type="'users'"></btnGroup>
      <div class="block pages">
        <el-pagination
        @current-change="handleCurrentChange"
        layout="prev, pager, next"
        :page-size="limit"
        :current-page="currentPage"
        :total="dataCount">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
  import btnGroup from '../../../Common/btn-group.vue'
  import http from '../../../../assets/js/http'

  export default {
    data() {
      return {
        tableData: [],
        dataCount: null,
        currentPage: null,
        keywords: '',
        multipleSelection: [],
        limit: 15
      }
    },
    methods: {
      testtest() {
        console(0)
      },
      search() {
        router.push({ path: this.$route.path, query: { keywords: this.keywords, page: 1 }})
      },
      selectItem(val) {
        this.multipleSelection = val
      },
      handleCurrentChange(page) {
        router.push({ path: this.$route.path, query: { keywords: this.keywords, page: page }})
      },
      confirmDelete(item) {
        this.$confirm('确认删除该用户?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          _g.openGlobalLoading()
          this.apiDelete('admin/users/', item.id).then((res) => {
            _g.closeGlobalLoading()
            this.handelResponse(res, (data) => {
              _g.toastMsg('success', '删除成功')
              setTimeout(() => {
                _g.shallowRefresh(this.$route.name)
              }, 1500)
            })
          })
        }).catch(() => {
          // catch error
        })
      },
      getAllUsers() {
        this.loading = true
        const data = {
          params: {
            keywords: this.keywords,
            page: this.currentPage,
            limit: this.limit
          }
        }
        this.apiGet('admin/users', data).then((res) => {
          this.handelResponse(res, (data) => {
            this.tableData = data.list
            this.dataCount = data.dataCount
          })
        })
      },
      getCurrentPage() {
        let data = this.$route.query
        if (data) {
          if (data.page) {
            this.currentPage = parseInt(data.page)
          } else {
            this.currentPage = 1
          }
        }
      },
      getKeywords() {
        let data = this.$route.query
        if (data) {
          if (data.keywords) {
            this.keywords = data.keywords
          } else {
            this.keywords = ''
          }
        }
      },
      init() {
        this.getKeywords()
        this.getCurrentPage()
        this.getAllUsers()
      }
    },
    created() {
      this.init()
    },
    formatter(row, column) {
      return row.name
    },
    filterTag(value, row) {
      return row.tag === value
    },
    filterHandler(value, row, column) {
      const property = column['property']
      return row[property] === value
    },
    computed: {
      addShow() {
        return _g.getHasRule('users-save')
      },
      editShow() {
        return _g.getHasRule('users-update')
      },
      deleteShow() {
        return _g.getHasRule('users-delete')
      }
    },
    watch: {
      '$route' (to, from) {
        this.init()
      }
    },
    components: {
      btnGroup
    },
    mixins: [http]
  }
</script>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>