<template>
  <div class="container">
    <h1><b>내가 찜한 콘텐츠</b></h1>
    <ul class="row">
      <MoviesCard 
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
        class="col-lg-3 col-md-4 col-sm-6 col-xs-12"
      />
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import MoviesCard from '../components/MoviesCard.vue'
export default {
  components: {
    MoviesCard,  
  },
  data() {
    return {
      movies: []
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    const user = jwt_decode(token).user_id
    // console.log(user)
    axios({
      url: 'http://127.0.0.1:8000/movies/',
      method: 'GET',
    }).then((res)=>{
      const temp = []
      res.data.forEach(function(element){
        console.log(element.like_users)
        if (element.like_users.includes(user)) {
          temp.push(element)
        }
      })
      // console.log(temp[8].like_users)
      this.movies = temp
      console.log(this.movies)
    }).catch((err)=>{
      console.error(err)
    })
  }
}
</script>

<style>

</style>