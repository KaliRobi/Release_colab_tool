import { createRouter, createWebHistory} from 'vue-router'
import AuthenticationView from '../views/AuthenticationView.vue'
import HomeView from '../views/HomeView.vue'
 
const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/authenticate',
      name: 'auth',
      component: AuthenticationView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView.vue
    }
    
  ]
})

export default router
