<template>
  <div id="app">
    <table border="0" cellspacing="0" cellpadding="0" align="center">
      <tr>
        <td>用户名：</td>
        <td><input type="text" v-model="username"></td>
      </tr>
      <tr>
        <td>密码：</td>
        <td><input type="text" v-model="password"></td>
      </tr>
      <tr>
        <button @click="go">注册</button>
      </tr>
      <div>{{ msg }}</div>
    </table>
  </div>
</template>

<script>

export default {
  name: "Register",
  data: function () {
    return {
      username: '',
      password: '',
      msg: ''
    }
  },
  methods: {
    go: function () {
      if (this.username === '') {
        alert('用户名不能为空')
        this.msg = "用户名不能为空"
        return
      } else if (this.password === '') {
        this.msg = "密码不能为空"
        return
      }
      this.$router.push({
        name: 'Login',
        query: {
          username: this.username,
          password: this.password,
        }
      })
    }
  }
}

</script>

<style scoped>

</style>
