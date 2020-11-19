<template>
  <div id="app">
    <table border="0" cellspacing="0" cellpadding="0" align="center">
      <tr>
        <td>
          用户名：
        </td>
        <td>
          <input type="text" v-model="username">
        </td>
      </tr>
      <tr>
        <td>
          密码：
        </td>
        <td>
          <input type="text" v-model="password">
        </td>
      </tr>
      <tr>
        <button @click="go">登录</button>
      </tr>
    </table>
    <router-view></router-view>
  </div>

</template>

<script>

export default {
  name: "Login",
  data: function () {
    return {
      username: this.$route.query.username,
      password: this.$route.query.password
    }
  },
  methods: {
    go: function () {
      this.$router.push({
        name: 'Inde',
        query: {
          username: this.username
        }
      })
    }

  }
}

</script>

<style scoped>

</style>

