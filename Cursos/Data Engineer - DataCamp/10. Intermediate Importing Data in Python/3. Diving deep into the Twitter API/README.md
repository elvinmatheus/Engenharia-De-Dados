# Diving deep into the Twitter API

## The Twitter API and Authentication

### Using Tweepy: Authentication handler

`tw_auth.py`

```python
import tweepy, json
access_token = "..."
access_token_secret = "..."
consumer_key = "..."
consumer_secret = "..."
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
```

### Tweepy: define stream listener class

`st_class.py`

```python
class MyStreamListener(tweepy.StreamListener):
def __init__(self, api=None):
    super(MyStreamListener, self).__init__()
    self.num_tweets = 0
    self.file = open("tweets.txt","w")
def on_status(self, status):
    tweet = status._json
    self.file.write(json.dumps(tweet) + '\\n')
    tweet_list.append(status)
    self.num_tweets += 1
    if self.num_tweets < 100:
        return True
    else:
        return False
self.file.close()
```

### Using Tweepy: stream tweets!!

`tweets.py`

```python
# Create Streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)
# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['apples', 'oranges'])
```