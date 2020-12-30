<template>
  <div class = "bg-main">
    <div class="container logindiv">
      <br><br><br>
      <h1 class = "text-left"><b>로그인</b></h1>
      <br>
      <div class="form-group">
        <!-- <label for="username">사용자 이름</label> -->
        <input class="form-control" type="text" style = "width:500px;"
        id="username" placeholder = "사용자 이름" v-model="credentials.username">
      </div>
      <br>
      <div class="form-group">
        <!-- <label for="password">비밀번호</label> -->
        <input style = "width:500px;"
          placeholder="비밀번호"
          class="form-control" 
          type="password" 
          id="password" 
          v-model="credentials.password"
          @keypress.enter="login"
        >
      </div>
      <br>
      <button class="btn btn-primary" @click="login">로그인</button>
      
     
      <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      <br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post('http://127.0.0.1:8000/api/v1/accounts/api-token-auth/', this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.bg-main {
  width: 100%;
  height: 1000px;
  position: relative;
  margin-bottom: 250px;
  z-index: 1;
  
  
}
.bg-main::after {
  width: 100%;
  height: 1000px;
  content: "";
  background-image: url('https://i.pinimg.com/originals/df/36/22/df36227e94aadd202bcd3a9dd7cc6c5c.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  opacity: 0.5;

}

.logindiv {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50% ,-65%);
  background-color: rgba(0,0,0,.75);
  width: 550px;
  height: 550px;

}
</style>