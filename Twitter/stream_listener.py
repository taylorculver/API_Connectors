import tweepy
import json


class MyStreamListener(tweepy.StreamListener):
    """Class to pull data into csv"""
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        tweet_list = []
        tweet_list.append(status)
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()  # what the hell is this bug


access_token = '950943314907459584-C61QPIG15DuJ7ctjzp000mkBjmGQERC'
access_token_secret = 'G8l4bYmyeTBJ9sEXUAoAVqxpKF2GwnfRYf4MUbn4xTTo5'
consumer_key = 'm8E5LTWzKPltrBwJaYqeR3O7j'
consumer_secret = '18aOpPDEXD4FZHQ5whMxc3kiIBJhRly8X4u712de37t1nzmDmC'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['trump'])
