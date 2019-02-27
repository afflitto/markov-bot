module.exports.tweet = (event, context, callback) => {
  const Twitter = require('twitter');
  const config = require('./config.js');
  const T = new Twitter(config);
  const Markov = require('markov-strings').default;
  const fs = require('fs');

  //list to hold tweets
  let sentences = [];

  fs.readFile('./tweets.json', (err, data) => {
    if(err) throw err;
    else {
      console.log("loaded file")

      sentences = JSON.parse(data);

      //statesize is 2 by default. For small amount of tweets, may want to change this to 1
      const stateSize = 2;
      console.log('stateSize',stateSize);

      //setup markov chain
      const markov = new Markov(sentences, {stateSize: stateSize});
      markov.buildCorpus();

      //try up to 50 times, make sure it's long enough and has a high score
      const options = {
        maxTries: 50,
        filter: (result) => result.string.split(' ').length >= 5 && result.score > 10
      }

      //generate new tweet
      const result = markov.generate(options);
      console.log("markov output:", result);

      if(!process.env.IS_LOCAL) { //don't tweet if running via serverless invoke local
        T.post('statuses/update', {status: result.string}, (err, data, response) => { //send tweet
          if(err) {
            console.error(err);
          } else {
            console.log("successfully sent tweet");
          }
        });
      }
    }
  });
}
