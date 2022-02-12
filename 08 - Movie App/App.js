// APIS
const movieInfoUrl = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1"
const imgFinder = "https://image.tmdb.org/t/p/w1280"
const searchMovie = "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query="


// Get Movies Object
async function getMovies(url) {
    const movies = await fetch(url)
    const moviesData = await movies.json()
    loadMovies(moviesData.results)
}

// Get Movie Card HTML
function movieHTML(movie) {
    const {original_title, vote_average, poster_path, overview} = movie

    return (
        `
            <div class="movie">
                <img src="${imgFinder + poster_path}">
                <div class="movie-info">
                    <h3>${original_title}</h3>
                    <span class="rating ${ratingClass(vote_average)}">${vote_average}</span>
                </div>
                <div class="overview">
                    <h3>Overview:</h3>
                    <p>${overview}</p>
                </div>
            </div>

        `
    ) 
}

// Load movies in ui
function loadMovies(movies) {
    const endLocation = document.querySelector('.movies__list')
    endLocation.innerHTML = ""

    movies.forEach( movie => {
        endLocation.insertAdjacentHTML("beforeend",movieHTML(movie))
    })
}

// set class to ratings based on rating
function ratingClass(rating) {
    if (rating >= 8) {
        return "green";
    } else if (rating >= 5) {
        return "orange";
    } else {
        return "red";
    } 
}

// Load the complete ui when dom loaded
window.addEventListener('DOMContentLoaded', (event) => {
   getMovies(movieInfoUrl);
});

// Add Search Feature
const search = document.querySelector('.search-movie')

search.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    getMovies(searchMovie + search.value)
  }
});