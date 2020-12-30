<template>
  <div class="container">
    <h1 class="pagetitle"><b>영화</b></h1>
    <hr>
    <hr>
    <ul class="row">
      <MoviesCard 
        v-for="(movie, idx) in paginatedData"
        :key="idx"
        :movie="movie"
        class="col-lg-3 col-md-4 col-sm-6 col-xs-12"
      />
    </ul>
    <div class="row">
      <form @submit="searchSome" class="form-inline ml-auto mr-2">
        <input class="form-control mr-sm-2" v-model="search" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
      <form>
        <button class="btn btn-primary ml-auto mr-4" onClick="history.go(0)">Refresh</button>
      </form>
    </div>
    <br>
    <div class="ml-4 btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MoviesCard from '../components/MoviesCard.vue'
export default {
  components: {
    MoviesCard,  
  },
  data() {
    return {
      movies: [],
      pageNum: 0,
      pageSize: 9,
      search: '',
    }
  },
  methods:{
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    searchSome(event) {
      event.preventDefault()
      const keyword = this.search
      const temp = []
      
      this.movies.forEach((element)=>{
        // console.log(element.title)
        const title = element.title
        if (title.indexOf(keyword) !== -1) {
          temp.push(element)   
        }
        this.movies = temp  
      })
       
      this.search = ''
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.movies.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      const sortedMovies = this.movies
      return sortedMovies.slice(start, end);
    }
  },
  created() {
    axios({
      url: 'http://127.0.0.1:8000/movies/',
      method: 'GET',
    }).then((res)=>{
      const temp = []
      res.data.forEach(function(element){
        temp.push(element)
      })
      // console.log(temp)
      this.movies = temp
      // console.log(this.movies)
    }).catch((err)=>{
      console.error(err)
    })
  }
}
</script>

<style>
 
</style>