import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Community from '../views/Community.vue'
import CreateArticle from '../views/CreateArticle.vue'
import UpdateArticle from '../views/UpdateArticle.vue'
import Movies from '../views/Movies.vue'
import MovieDetail from '../components/MovieDetail.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import ArticleDetail from '../components/ArticleDetail.vue'
import Profile from '../views/Profile.vue'
import LikedMovies from '../views/LikedMovies.vue'
import MainPage from '../views/MainPage.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/create-article',
    name: 'CreateArticle',
    component: CreateArticle
  },
  {
    path: '/update-article',
    name: 'UpdateArticle',
    component: UpdateArticle,
    props: true
  },
  {
    path: '/article-detail/',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/liked-movies',
    name: 'LikedMovies',
    component: LikedMovies,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
