//SEARCH FOR A GIF
function getSearchFromApi(){
    var endpoint = 'https://api.giphy.com/v1/gifs/search?'
    
    var inputElement = document.getElementById('search')
    var value = inputElement.value
    
    var searchTerm = `q=${value.replace(" ", "+")}&`
    var rating = 'rating=pg13&'
    var api_key = 'api_key=bb95615371524c4a9af8c5bbb91155d2'
    var url = endpoint + searchTerm + rating + api_key
    // looks like this: api.giphy.com/v1/gifs/search?q=panda&api_key=ea182799688a4011b13298529a6d0642
    // get JSON data from url endpoint
    // JSON - JavaScript Object Notation
    fetch(url) // Fetch issues GET requests
    .then(function(data){
        return data.json()
    })
    .then(function(json){
        console.log(json)
        
        var finalHTML = ''
        
        json.data.forEach(function(item){
            finalHTML += `<img src="${item.images.fixed_height.url}" />`
        })
        
        var resultDiv = document.getElementById('result')
        resultDiv.innerHTML = finalHTML
        
    })
    .catch(function(error){
        console.log(error)
    })
}

//RANDOM GIF
function getRandomFromApi(){
    var endpoint = 'https://api.giphy.com/v1/gifs/random?'
    var api_key = 'api_key=dc6zaTOxFJmzC&'
    var tag = 'tag=random'
    var url = endpoint + api_key + tag
    // looks like this: api.giphy.com/v1/gifs/search?q=panda&api_key=ea182799688a4011b13298529a6d0642
    // get JSON data from url endpoint
    // JSON - JavaScript Object Notation
    fetch(url) // Fetch issues GET requests
    .then(function(data){
        return data.json()
    })
    .then(function(json){
        console.log(json)
        
        var finalHTML = ''
        
        json.data.forEach(function(item){
            finalHTML += `<img src="${item.images.fixed_height.url}" />`
        })
        
        var resultDiv = document.getElementById('result')
        resultDiv.innerHTML = finalHTML
        
    })
    .catch(function(error){
        console.log(error)
    })
}
