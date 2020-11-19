<template>
  <div align="center">
    <el-container>
      <el-header>add Emp Info</el-header>
      <el-main>
        <table border="0" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td>name:</td>
            <td>
              <el-input v-model="name" placeholder="请输入内容"></el-input>
            </td>
          </tr>
          <tr>
            <td>salary:</td>
            <td>
              <el-input v-model="salary" placeholder="请输入内容"></el-input>
            </td>
          </tr>
          <tr>
            <td>age:</td>
            <td>
              <el-input v-model="age" placeholder="请输入内容"></el-input>
            </td>
          </tr>
          <tr>
            <td>headpicture:</td>
            <td>
              <el-button type="primary" size="mini">选择文件</el-button>
              <span>未选择任何文件</span></td>
          </tr>
          <tr>
            <td>
              <el-button type="primary" size="mini" @click="add">Confirm</el-button>
            </td>
          </tr>
        </table>
      </el-main>
    </el-container>

  </div>
</template>
<script>
// export default {
//   name: "Addemp"
// }
export default {
  name: "Addemp",
  data() {
    return {
      name: '',
      salary: '',
      age: '',
    }
  },
  methods: {
    add: function () {
      if(this.name===''){
        alert('用户名不能为空！')
      }
      if(this.salary===""){
        alert('薪水不能为空！')
      }
      if(this.age===''){
        alert('年龄不能为空！')
      }else{
        let number = parseInt(localStorage.getItem("number"))
        let id =++ number
        console.log(id)
        localStorage.setItem("number",id)
        let users = JSON.parse(localStorage.getItem("users"))
        users.push({id:id,name:this.name,age:this.age,salary:this.salary})
        localStorage.setItem("users",JSON.stringify(users))
        this.$router.push({
          name: 'Emplist',
        })

      }
      // users.push({id:id,name:this.name,age:this.age,salary:this.salary})
      // localStorage.setItem("users",JSON.stringify(users))
      // this.$router.push({
      //   name: 'Emplist',
      // })
    }
  }
}
</script>

<style scoped>
span {
  font-size: 10px;
}

.el-input {
  width: 100%;
}

.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  /*line-height: 60px;*/
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  /*line-height: 200px;*/
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  /*line-height: 160px;*/
}

body > .el-container {
  margin-bottom: 40px;
}

</style>