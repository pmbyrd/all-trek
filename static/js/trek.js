
// const apiKey = await getApiKey() //?Why is this code working?
// console.log('Hello World');
// // get the json response of an api_key from my server
// async function getApiKey(){
//     const res = await axios.get('/api_key')
//     console.table(res.data)
//     return res.data.api_key
// }
const Base_URL = 'https://api.themoviedb.org/3'
// const 

async function getApiKey(){
    const res = await axios.get('/api_key')
    console.table(res.data)
    // const apiKey = JSON.parse(res.data.api_key)
    const data = res.data.api_key
    return data
}

// test the api_key
// todo make a function call to tmdb
async function getMovie(movie){
    const apiKey = await getApiKey()
    const res = await axios.get(`${Base_URL}/search/movie/?api_key=${apiKey}&query=${movie}`)
    // console.log(res.data)
    return res.data
}

// todo make a function to display the movies
async function displayMovies(){
    const res = await getMovie("star trek")
    const results = res.results
    // map over the results to display the movies
    // *get the container from the page
    const $movies = $(".movies")
    //*append the results to the container 
    // for each result I want it to be its own card
    // !critical on the backend side I will feed the data that the movie is going to be displayed
    // const $result = results.map(r => {
    //     return `
    //     <div class="col-4">
    //         <div class="card" style="width: 18rem;">
    //             <img src="https://image.tmdb.org/t/p/w500${r.poster_path}" class="card-img-top" alt="...">
    //             <div class="card-body">
    //                 <h5 class="card-title text-center">${r.title}</h5>
    //                 <p class="card-text">${r.overview}</p>
    //                 <a href="#" class="btn btn-primary">Go somewhere</a>
    //             </div>`
    // })

    console.table(results)
    // const 
    return results
    
}

// Todo make function here that will call the database to retieve the movies



