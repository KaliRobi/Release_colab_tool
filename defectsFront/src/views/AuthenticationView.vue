<template>
  <form method="POST" id="login-form" @submit.prevent="onSubmit">
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
import axios from 'axios';
import { ref } from 'vue';


const userName = ref('')
const password = ref('')


const onSubmit = async () => {

  try {
    const response = await axios.get('http://localhost:8000/api/v1/csrf_token_provider_endpoint')
    const cookie = getCookie('csrftoken')
    const loginData = {
      "username": userName.value,
      "password": password.value
    };
    console.log(loginData)
    axios.defaults.headers.common['X-CSRFToken'] = response.data.csrfToken;
    await axios.post('http://localhost:8000/api/v1/login_endpoint/', loginData, {
      headers: {
        "X-CSRFToken": cookie,
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true, // Send cookies along with the request
    }).then(res => {
      console.log(res)
    });


  } catch (error) {
    console.log(error)
  }


}








//  await fetch('http://127.0.0.1:8000/accounts/login/', {
//   method : 'POST',
//   credentials: 'include',
//   headers: headers,
//   body : JSON.stringify(loginDetails)
//  }).then( response => {
//    console.log(response)
//  }).catch(error => {
//     console.error(error);
//   });



// const getCRSFToken = async () =>{

// await fetch('http://127.0.0.1:8000/api/v1/csrf_token_provider_endpoint/', {
//   method : 'GET',
//   headers: {
//     "Content-Type": "application/json"
//   }

// }).then (response => response.json()
// ).then(data =>{const csrfToken = data
//   localStorage.setItem('csrfToken', csrfToken['csrfToken'])
// }).catch(error => {
//     console.error(error);
//   });


// }

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}




</script>