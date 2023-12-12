import { createRouter, createWebHistory } from 'vue-router'
import AuthenticationView from '../views/AuthenticationView.vue'

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/authenticate',
      name: 'auth',
      component: AuthenticationView
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/HomeView.vue')
    // }
  ]
})

export default router
