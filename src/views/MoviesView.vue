<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetch_movies = () => {
  fetch("/api/v1/movies")
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch movies.');
        }
        // console.log(response);
        return response.json();
      })
      .then(data => {
        movies.value = data.movies;
        // console.log(data.message);
      })
      .catch(error => {
        console.error('Error fetching movies:', error);
      });
};

 const get_movie_poster_url = (poster_filename) => {
   return `${poster_filename}`;
 };


onMounted(fetch_movies);
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4" v-for="movie in movies" :key="movie.id">
        <div class="card">
          <img :src="get_movie_poster_url(movie.poster)" class="card-img-top" alt="Movie Poster">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
