# markov-bot
Quick Twitter bot using Markov chains and AWS Lambda. Using the downloader script, you can download a dataset of tweets from a given account. The bot will tweet a generated tweet every 4 hours.

Live example: [@imalsoblackbear](https://twitter.com/imalsoblackbear)

### Requirements
- Node.js
- Python
- aws-cli: [Install via Amazon's guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- Serverless: `npm install -g serverless`

### Setup
1. Run the following in the command line:
```
git clone https://github.com/afflitto/markov-bot && cd markov-bot/bot
npm install
cp config.js.template config.js

cd ../downloader
sudo pip install tweepy
cp config.py.templage config.py
```

2. (optional) Modify `serverless.yml`
  * You may want to change the service name if you plan on running more than one bot.
  * You can change the rate to determine how often the bot will run.

3. Create a Twitter app on [developer.twitter.com](developer.twitter.com)
  * You probably want to create a new Twitter account and apply to be a developer (otherwise the bot will tweet from your account). Then you can create an app and generate consumer and access tokens.
  * Fill in config.js and config.py with your app's consumer and access token keys/secrets.

4. Download tweets: `python downloader.py {username}`, filling in `{username}` with a twitter username.

5. Copy the tweets to the bot directory: `cp tweets*.json ../bot/tweets.json`

6. Deploy: `cd ../bot && serverless deploy`

The twitter bot will automatically run every 4 hours (or whatever you changed the rate to in `serverless.yml`). To run it manually, run `serverless invoke -f tweet`.
