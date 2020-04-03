import Vue from 'vue'
import App from './App.vue'
import Home from './components/Home'
import StudentCreate from './components/StudentCreate'
import StudentEdit from './components/StudentEdit'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'


Vue.config.productionTip = false

Vue.use(VueRouter)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

Vue.use(VueAxios, axios)

const routes = [
    {
        path: '/',
        component: Home,
        name: 'home',
        meta: {
            title: 'Главная'
        }
    },
    {
        path: '/students/add',
        component: StudentCreate,
        name: 'student_create',
        meta: {
            title: 'Внесение данных студента'
        }
    },
    {
        path: '/students/edit/:id',
        component: StudentEdit,
        name: 'student_edit',
        meta: {
            title: 'Изменение данных студента'
        }
    }
]

const router = new VueRouter({
  routes,
  mode: 'history',
  scrollBehavior() {
    return {x: 0, y: 0}
  }
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

new Vue({
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
