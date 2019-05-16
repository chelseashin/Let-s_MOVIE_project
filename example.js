function javascriptCode(data, user){
    // const {sample, CF, evaluation} = require('nodeml');
    const movie = data
    console.log(data)
    let train = [], test = [];
    for (let i = 0; i < movie.length; i++) {
        if (Math.random() > 0.8) test.push(movie[i]);
        else train.push(movie[i]);
    }

    const cf = new CF();

    cf.maxRelatedItem = 10;
    cf.maxRelatedUser = 10;

    cf.train(train, 'user_id', 'movie_id', 'rating');

    let gt = cf.gt(test, 'user_id', 'movie_id', 'rating');
        
    return cf.recommendToUser(user,10)
}