
import { RouterLink } from 'vue-router';
<template>
    <nav class="navbar bg-opacity-30 shadow-lg bg neutral ">
    <div class="container mx-auto">
      <div class="flex px-2  justify-between	">
        <div class="m-5">
          <router-link  :to="{name : 'home'}"><h3 class="text-xl font-mono hover:" >DEFECT LIST</h3>
          </router-link>
        </div>
        <div class="m-5">
          <a class="bg-white hover:bg-gray-100 text-gray-800 
          font-semibold py-2 px-4  border 
          border-gray-400 rounded shadow " href="/accounts/logout/"
              >Logout
            </a>
        </div>
      </div>
    </div>
</nav></template>

