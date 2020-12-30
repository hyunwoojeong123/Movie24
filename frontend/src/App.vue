<template>
  <div id="app" class = 'text-white bgblack'>
    <b-navbar class="sticky-top bl" toggleable="lg" type="dark" variant="dark">
      <router-link class="navbar-brand" to="/home"><a href="/home"><img src="https://fontmeme.com/permalink/201125/e5e0cb70c6e30a55fb77051ec55bc665.png" alt="netflix-type" border="0"></a></router-link>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav v-if="login">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/movies">
                <svg width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-camera-reels" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M0 8a2 2 0 0 1 2-2h7.5a2 2 0 0 1 1.983 1.738l3.11-1.382A1 1 0 0 1 16 7.269v7.462a1 1 0 0 1-1.406.913l-3.111-1.382A2 2 0 0 1 9.5 16H2a2 2 0 0 1-2-2V8zm11.5 5.175l3.5 1.556V7.269l-3.5 1.556v4.35zM2 7a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h7.5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H2z"/>
                  <path fill-rule="evenodd" d="M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                  <path fill-rule="evenodd" d="M9 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                </svg>
                <b>영화</b>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="liked-movies">
                <svg width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-bookmark-heart" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                  <path fill-rule="evenodd" d="M8 4.41c1.387-1.425 4.854 1.07 0 4.277C3.146 5.48 6.613 2.986 8 4.412z"/>
                </svg>
                <b>내가 찜한 콘텐츠</b> 
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/community">
                <svg width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-chat-square-text" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M14 1H2a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h2.5a2 2 0 0 1 1.6.8L8 14.333 9.9 11.8a2 2 0 0 1 1.6-.8H14a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                  <path fill-rule="evenodd" d="M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
                </svg>
                <b>커뮤니티</b>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/profile">
                <svg width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-person-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M14 1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                  <path fill-rule="evenodd" d="M2 15v-1c0-1 1-4 6-4s6 3 6 4v1H2zm6-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                </svg>
                <b>내 프로필</b> 
              </router-link>
            </li>
          </ul>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav v-if="login">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <router-link class="nav-link" @click.native="logout" to="#">로그아웃</router-link>
              </li>
            </ul>
          </b-navbar-nav>
          <b-navbar-nav v-else>
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <router-link class="nav-link" to="/signup">회원가입</router-link> 
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/login">로그인</router-link>
              </li>
            </ul>
          </b-navbar-nav>
          <!-- <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <p></p>
    <router-view @login="login = true" />
    <div class="footerWrap">
      <div class="footer">
        <div class="f1">
          <!-- <img src="./assets/두번째.jpg" alt="">   -->
          <pre>
          Movie24 대한민국
          이메일 주소: korea@movie24.com
          주소: 대전광역시 유성구 동서대로 98-39
          Movie24서비시스코리아 유한회사 통신판매업신고번호: 제2018-대전유성-0426호 전화번호: 00-308-321-0058
          </pre>
        </div>
        <div class="f2">
          <ul>
            <li><a href="https://twitter.com/?lang=ko"><i class="fab fa-twitter"></i></a></li>
            <li><a href="https://www.facebook.com/"><i class="fab fa-facebook-f"></i></a></li>
            <li><a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a></li>
            <li><a href="https://www.google.co.kr/"><i class="fab fa-google-plus-g"></i></a></li>
          </ul>
        </div>
    </div>
  </div>
  </div>
  
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: 'MainPage' })
    }
  },
  created() {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
  /* background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScfuPDUP8qBxH359UPfXjb6zjjlw2nUz_hSQ&usqp=CAU');
  background-size: cover;
  background-repeat: no-repeat;
  width: 100%;
  height: 100%; */
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<style scoped>
  .navbar.navbar-dark.bg-dark{
    background-color: black!important;
 }


 /* -------------------------------------------Footer------------------------------------------- */
 .footerWrap {
    width: 100%;
    height: 180px;
    background: black;
    
  }

  .footer {
    width: 1240px;
    height: 100%;
    margin: 0 auto;
  }

  .footer::after {
    display: block;
    clear: both;
    content: "";
  }

  .footer>.f1 {
    width: 70%;
    height: 100%;
    background: black;
    float: left;
    text-align: center;
  }
  .f1>img{
    padding-left: 20px;
    width: 50%;
    height: 100px;
    background-size: cover;
   
  }

  .f1>pre{
    padding-right: 20px;
    padding-top: 50px;
    color: white;
  }

  .footer>.f2 {
    width: 30%;
    height: 100%;
    background: black;
    float: left;
    position: relative;
  }

  /* .logo {
    background: url(img3/con1.jpg)no-repeat;
    background-size: cover;
    width: 260px;
    height: 80px;
    margin-bottom: 20px;
  } */


  .f2>ul::after {
    display: block;
    clear: both;
    content: "";
  }

  .f2>ul>li {
    width: 25%;
    float: left;   
    border-top: 1px #555 solid;
    border-bottom: 1px #555 solid;
    padding: 20px 0;
    list-style:none;
  }

  .f2>ul>li>a {
    color: #555;
    font-size: 20px;
      
  }

  .f2>ul {
    width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    text-align: center;
    padding: 0;
  }

  .f2>ul>li>a:hover {
    color: #fff;
  }

  /* .mgb {
    margin-bottom: 200px
  } */
</style>
