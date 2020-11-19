<template>
  <div>preparing for  {{username}}  congratulations</div>
</template>
<script>
export default {
  name: "Inde",
  data:function (){
    return {
      username:this.$route.query.username
    }
  },
}
</script>

<style scoped>

</style>