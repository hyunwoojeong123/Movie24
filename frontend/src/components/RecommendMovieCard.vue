<template>
  <swiper-slide>
    <div class="card bgblack" style="width: 18rem;" @click=getMovieDetail()>
      <div class="card-img"><img  :src="getImage" class="card-img-top" alt=""></div>
      
      <div class="card-body">
        
        <h5 class="card-title" v-for="(item,idx) in getTitle" :key="idx"><b>{{ item }}</b></h5>
        
        <!-- <div v-html="getTitle"></div> -->
      </div>
      <b-modal 
      ref="detail" 
      size="lg" 
      class="bg-black" 
      :header-bg-variant="black"
      :body-bg-variant="black"
      :footer-bg-variant="black"
      hide-footer hide-header>
        <MovieDetail
          :movie_pk = this.movie.movie_id
        />
      </b-modal>
    </div>
  </swiper-slide>
  
</template>

<script>
import MovieDetail from '../components/MovieDetail.vue'
export default {
  props: {
    movie:Object
  },
  components: {
    MovieDetail
  },
  data(){
    return {
      black : 'black'
    }
  },
  computed: {
    getImage: function() {
      return 'http://image.tmdb.org/t/p/w185'+this.movie.poster_path
    },
    getTitle: function() {
      const t = this.movie.title
      // const len = length(t)
      const temp = t.split(' ')
      // let res= ''
      // temp.foreach(function(element){
        // if (length(res) + length(element) > 12){
        // res =  res+ element
        // } else {
        //   res = res + 'x' + element
        // }
      // })
      let res = []
      let tp = ''
      for(let i = 0; i < temp.length; i++){
        if(tp.length + temp[i].length < 12 ){ 
          tp += ' ' + temp[i]
        }else{
          res.push(tp)
          tp = temp[i]
        }
      }
      res.push(tp)
      return res
    },
    getOverview: function() {
      return this.movie.overview
    },
    
  },
  methods: {
    getMovieDetail() {
      // console.log(this.movie.title)
      console.log('TQ',this.movie.title)
      // this.$bvModal.show('detail')
      this.$refs['detail'].show()
      // console.log(this.movie)
      // this.$router.push({name: 'MovieDetail', params: {movie_pk: this.movie.movie_id}})
    },
  },
}
</script>

<style>
.bgblack {
  background-color: black;
}
.modal_content
.modal_header
.modal_body {
  background-color: black;
}



</style>

