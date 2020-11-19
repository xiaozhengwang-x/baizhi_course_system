<template>
  <div align="center">
    <el-container>
      <el-header>update Emp Info</el-header>
      <el-main>
        <table border="0" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td>id:</td>
            <td>
              <el-input v-model="id" placeholder="请输入内容"></el-input>
            </td>
          </tr>
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
              <el-button type="primary" size="mini" @click="update">Confirm</el-button>
            </td>
          </tr>
        </table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
// export default {
//   name: "Update"
// }
export default {
  name:'Update',
  data() {
    let id = this.$route.query.id
    console.log(id)
    let users=JSON.parse( localStorage.getItem('users'))
    console.log(users)
    for(let i=0;i<users.length;i++){
      if(users[i].id==id){
        console.log(12345)
       return {
         id: id,
         name:users[i].name,
         age:users[i].age,
         salary:users[i].salary ,
       }

      }
    }
  },
  methods:{
    update:function (){
      let user1 ={
        id:this.id,
        name:this.name,
        salary:this.salary,
        age:this.age,
      }
      let id = this.$route.query.id
      console.log(id)
      let users=JSON.parse( localStorage.getItem('users'))
      console.log(users)
      for (let i = 0; i < users.length; i++) {
        if(users[i].id===id){
          users[i]=user1
          localStorage.setItem('users',JSON.stringify(users))
          // users[i]={id:this.id,name:this.name,salary:this.salary,age:this.age}
        }
      }
      this.$router.push({
        name: 'Emplist',
        query: {
          id:this.id,
          name: this.name,
          salary: this.salary,
          age: this.age,
    }
  })
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