<template>
  <div class="mb-3 bgblack text-white" style="width: auto;">
    <div class="col-md-4" >
      <br>
      <img :src="getImage" alt=""  
      style = "margin-left: 80px;">
    </div>
    <hr>
    <iframe v-if="videoURI" :src="videoURI" frameborder="0" style = "width: 700px; height: 350px"></iframe>
    <div class="row no-gutters" style="display: inline-block;">
      <div class="card-body">
        <br>
        <h1 class="card-title">{{ title }}</h1>
        <br>
        <h5>개봉일: {{ release_date }} / 평점: {{ vote_average }}</h5>
        <br>
        <p class="card-text">{{ overview }}</p>
        <br>
        <!-- <button @click="getYoutubeReview" class="btn btn-danger">Youtube Review</button> -->
      </div> 
    </div>
    
    <form @submit="commentSubmit">
      <div class="form-group">
        <!-- <h3>평점</h3>
        <input type="number" min="0" max="10" class="form-control" id="rating" v-model="myrating"> -->
        <label for="star">별점</label>
        <star-rating
          id="star" 
          v-bind:increment="0.5"
          v-bind:max-rating="5"
          v-bind:show-rating="false"
          inactive-color="#000"
          active-color="#ff0"
          border-color="#ff0"
          v-bind:padding="8"
          v-bind:border-width="2"
          v-bind:star-size="50"
          @rating-selected="setRating">
        </star-rating>
        <hr>
        <label for="comment">댓글을 입력하세요.</label>
        <textarea class="form-control" id="comment" rows="2" v-model="mycomment" @keypress.enter="commentSubmit"></textarea>
      </div>
      <button class="btn btn-primary">제출</button>
    </form>
    <hr>
    <MovieComment 
      v-for="(comment, idx) in paginatedData"
      :key="idx"
      :comment="comment"
      :movie_pk="movie_pk"
      @onParentDeleteComment="onParentDeleteComment"
    />
    <br>
    <div class="btn-cover">
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
import jwt_decode from 'jwt-decode'
import StarRating from 'vue-star-rating'
// import _ from 'lodash'
import MovieComment from '../components/MovieComment.vue'
export default {
  components: {
    MovieComment,
    StarRating
  },
  data() {
    return {
      id:'',
      poster_path:'',
      title:'',
      vote_average:'',
      overview:'',
      release_date:'',
      mycomment:'',
      myrating:'',
      comments:[],
      videoURI:'',
      pageNum: 0,
      pageSize: 5,
    }
  },
  props: {
    movie_pk: Number,
     
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    commentSubmit(event) {
      event.preventDefault()
      if (this.mycomment.length !== 0) {
        const movie_pk = this.movie_pk
        console.log("무비 피케이",movie_pk)
        const token = localStorage.getItem('jwt')
        console.log(jwt_decode(token))
        const user = jwt_decode(token).user_id
        // console.log(user)
        axios({
          url: `http://127.0.0.1:8000/movies/${movie_pk}/reviews/`,
          method: 'POST',
          data: {
            user: user,
            content: this.mycomment,
            rating: this.myrating,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          // console.log(res.data)
          axios({
            url: `http://127.0.0.1:8000/movies/${movie_pk}/reviews/`,
            method: 'GET',
          }).then((res)=>{
              const temp = []
              res.data.forEach((element)=>{
                temp.push(element)
              })
              this.comments = temp
              // this.comments = _.sortBy(temp,
          }).catch((err)=>{
            console.error(err)
          })
        }).catch((err)=>{
          console.error(err)
        })
        this.mycomment = ''
      } else {
        alert("댓글을 입력하세요.")
      }
    },
    onParentDeleteComment: function() {
      const movie_pk = this.movie_pk
      axios({
        url: `http://127.0.0.1:8000/movies/${movie_pk}/reviews/`,
        method: 'GET',
      }).then((res)=>{
          const temp = []
          res.data.forEach((element)=>{
            temp.push(element)
          })
          this.comments = temp
      }).catch((err)=>{
        console.error(err)
      })
    },
    setRating(rating) {
      // console.log(rating)
      this.myrating = rating * 2
    }
  },
  computed: {
    getImage: function() {
      return 'http://image.tmdb.org/t/p/w500'+this.poster_path
    },
    pageCount () {
      let listLeng = this.comments.length,
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
      // const sortedComments = _.sortBy(this.comments, 'id').reverse()
      return this.comments.slice(start, end);
    },
  },
  beforeUpdate(){
    const API_KEY = 'AIzaSyAJTGiQJZHAcZqcj-rUmJ3NR_NL1FIAXjU'
    const API_URL = 'https://www.googleapis.com/youtube/v3/search'
    const inputValue = `${this.title} review`
    console.log(inputValue)
    const params = {
      key: API_KEY,
      part: 'snippet',
      type: 'video',
      q: inputValue,
    }

    axios.get(API_URL, {
      params,
    })
    .then((res) => {
      // console.log(res)
      console.log('이거',res.data.items)
      const videoId = res.data.items[0].id.videoId
      console.log('저거', videoId)
      this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=1&mute=1&autoplay=1&controls=0&frameborder=0`
      console.log('비디오주소', this.videoURI)
    })
    .catch((err) => {
      console.log(err)
    })
  },
  created() {
    const movie_pk = this.movie_pk
    

    axios({
      url: `http://127.0.0.1:8000/movies/${movie_pk}/`,
      method: 'GET',
      
    }).then((res)=>{
      console.log(res.data)  
      this.id = res.data.id
      this.poster_path = res.data.poster_path
      this.title = res.data.title
      this.vote_average = res.data.vote_average
      this.overview = res.data.overview
      this.release_date = res.data.release_date
    }).catch((err)=>{
      console.error(err)
    })
    axios({
      url: `http://127.0.0.1:8000/movies/${movie_pk}/reviews/`,
      method: 'GET',
    }).then((res)=>{
        const temp = []
        res.data.forEach((element)=>{
          temp.push(element)
        })
        this.comments = temp
    }).catch((err)=>{
      console.error(err)
    })
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    const username = jwt_decode(token).username
    this.currentName = username
  },     
}
  
</script>


<style scoped>

</style>
