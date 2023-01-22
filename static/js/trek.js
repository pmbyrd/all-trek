
// const apiKey = await getApiKey() //?Why is this code working?
// console.log('Hello World');
// // get the json response of an api_key from my server
// async function getApiKey(){
//     const res = await axios.get('/api_key')
//     console.table(res.data)
//     return res.data.api_key
// }
const Base_URL = 'https://api.themoviedb.org/3'
const 

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
    console.table(results)
    const 
    return results
    
}


