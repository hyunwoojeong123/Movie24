import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VuePlayerPlugin from 'vue-youtube-iframe-api'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'swiper/swiper-bundle.css' 

import router from './router'
import VueAwesomeSwiper from 'vue-awesome-swiper'
Vue.use(BootstrapVue)
Vue.use(VueAwesomeSwiper)
Vue.use(VuePlayerPlugin)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
