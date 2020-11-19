<template>
  <div>
    <el-table
        :data="tableData"
        style="width: 100%">
      <el-table-column
          label="编号"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-number"></i>
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="姓名"
          width="180">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>姓名: {{ scope.row.name }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.name }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column
          label="薪水"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-salary"></i>
          <span style="margin-left: 10px">{{ scope.row.salary }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="年龄"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-age"></i>
          <span style="margin-left: 10px">{{ scope.row.age }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="头像"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-headpicture"></i>
          <span style="margin-left: 10px">{{ scope.row.headpicture }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
              size="mini"
              @click="handleEdit(scope.row.id)">编辑
          </el-button>
          <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
        background
        layout="prev, pager, next"
        :total="50">
    </el-pagination>
    <el-row>
      <el-button type="primary" round @click="add">Addemployee</el-button>
    </el-row>

    <!--    <div class="table-pagination">-->
    <!--      <el-pagination-->
    <!--          background-->
    <!--          layout="prev, pager, next"-->
    <!--          :total="page.total"-->
    <!--          :page-size="page.limit"-->
    <!--          @current-change="pageChange"-->
    <!--      ></el-pagination>-->
    <!--    </div>-->
  </div>

</template>

<script>
export default {
  name: "Emplist",
  data: function () {
    return {
      tableData: JSON.parse(localStorage.getItem("users"))
    }
  },
  methods: {
    handleDelete(index) {
      this.tableData.splice(index,1)
      let users = JSON.parse(localStorage.getItem("users"))
      users.splice(index,1)
      let users_json=JSON.stringify(users)
      localStorage.setItem('users',users_json)
    },
    add: function () {
      this.$router.push({
        name: 'Addemp',
      })
    },
    handleEdit:function (id){
      this.$router.push({
        name: 'Update',
        query:{
          id:id,
          name:this.$route.query.name,
          salary:this.$route.query.salary,
          age:this.$route.query.age,
        }
      })
    }
  },
  created() {
    if (!localStorage.getItem('number')){
      localStorage.setItem("number",0)
    }
    if(!localStorage.getItem('users'))
    localStorage.setItem("users",JSON.stringify([]))
  }
}

</script>

<style scoped>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>