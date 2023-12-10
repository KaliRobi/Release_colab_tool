<template>
<form method="POST" id="login-form" @submit.prevent="onSubmit" >
        <div class="bg-blue-500 text-white">
        <label for="floatingUsername">Username</label>
        <input type="text" id="text" v-model="userName" placeholder="Enter userName...">
        </div>
        <div class="form-floating mb-3">
        <label for="floatingPassword">Password</label>
        <input type="text" id="text" v-model="password" placeholder="Enter password...">
        </div>
            <div class="text-danger my-3">
         </div>
             <div class="d-grid gap-2">
          <button type="submit" class="btn btn-lg btn-primary">Login</button>
        </div>
    </form>
</template>

<script setup>
import {ref} from 'vue';


const userName = ref('')
const password = ref('')


const onSubmit = async () => {
  console.log(userName.value)
  console.log(password.value)

const loginDetails = {
    "username" : userName.value,
    "password" : password.value
}  

 await fetch('http://127.0.0.1:8000/accounts/login/', {
  method : 'POST',
  headers: {
    "Content-Type": "application/json"
  },
  body : JSON.stringify(loginDetails)
 }).then( response => {
   console.log(response)
 })

}





</script>