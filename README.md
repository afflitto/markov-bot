# markov-bot
Quick Twitter bot using Markov chains and AWS Lambda

### Setup
1. Run the following in the command line:
```
git clone https://github.com/afflitto/markov-bot && cd markov-bot/bot
npm install
npm install serverless -g
cp config.js.template config.js

cd ../downloader
pip install tweepy
cp config.py.templage config.py
```

2. (optional) Modify `serverless.yml`
..* You may want to change the service name if you plan on running more than one bot.
..* You can change the rate to determine how often the bot will run.

3. Create a Twitter app on [developer.twitter.com](developer.twitter.com)
..* Fill in config.js and config.py with your app's consumer and access token keys/secrets.

4. Download your tweets: `python downloader.py {username}`, filling in `{username}` with a twitter username.

5. Copy the tweets to the bot directory: `cp tweets*.json ../bot/tweets.json`

6. Deploy: `cd ../bot && serverless deploy`
