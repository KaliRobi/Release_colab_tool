<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'

</script>



<template>
       <div  >
        <Navbar />
        <!-- <RouterLink to="/authenticate">This</RouterLink> -->
      </div>
  <RouterView />
</template>
