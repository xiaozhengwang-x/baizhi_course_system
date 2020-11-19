import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register'
import Login from '../views/Login'
import Inde from '../views/Inde'
import Addemp from "@/views/Addemp"
import Emplist from "@/views/Emplist"
import Update from "@/views/Update"

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/Emplist'
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/inde',
        name: 'Inde',
        component: Inde
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/addemp',
        name: 'Addemp',
        component: Addemp
    },
    {
        path: '/emplist',
        name: 'Emplist',
        component: Emplist
    },
    {
        path: '/update',
        name: 'Update',
        component: Update
    },

]

const router = new VueRouter({
    routes
})

export default router
