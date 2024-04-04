<script setup>
import {ref, onMounted} from "vue";
let csrf_token = ref("");
let title = ref("");
let description = ref("");

const successMessage = ref('');
const errorMessages = ref([]);
const displayMessage = ref(false);

onMounted(() => {
  getCsrfToken();
});

const saveMovie = () => {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);


  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  }).then(function (response) {
          // console.log(response);
          return response.json();
      })
      .then(function (data) {
        // console.log('data', data);
        successMessage.value = data.message;
        displayMessage.value = true;
        errorMessages.value = data.errors;
      })
      .catch(function (error) {
        errorMessages.value = error.message;
      });
}

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      })

}
</script>

<template>
<div class="container col-md-10">
  <form @submit.prevent="saveMovie" id="movieForm">
    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>
    <div v-if="errorMessages.length > 0" class="alert alert-danger" role="alert">
      <ul>
        <li v-for="error in errorMessages" :key="error">{{ error }}</li>
      </ul>
    </div>
    <div class="form-group col-md-8 mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" v-model="title">
    </div>
    <div class="form-group col-md-8 mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" v-model="description"></textarea>
    </div>

    <div class="form-group col-md-8 mb-3">
      <label for="poster" class="form-label">Photo Upload</label>
      <input type="file" name="poster" class="form-control">
    </div>
    <button type="submit" name="submit" class="btn btn-primary">
      Submit
    </button>
  </form>
</div>
</template>

<style scoped>

</style>
