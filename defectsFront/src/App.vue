<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import './assets/styles.css'
</script>

<template>
       <div class="text-3xl" >
        <Navbar />
        <!-- <RouterLink to="/authenticate">This</RouterLink> -->
      </div>
  <RouterView />
</template>
