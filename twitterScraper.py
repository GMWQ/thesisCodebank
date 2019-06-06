import codecs, json
import Tweepy

config = ConfigParser()
config.read('twitterauth.ini')
access_token = config.get('auth','ACCESS_TOKEN')
access_token_secret = config.get('auth', 'ACCESS_TOKEN_SECRET')
consumer_key = config.get('auth', 'CONSUMER_KEY')
consumer_secret = config.get('auth','CONSUMER_SECRET')

'''
print(access_token)
print(access_token_secret)
print(consumer_key)
print(consumer_secret)
'''

def twitter_init():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    return api
    
# Create Scraper
extractor = twitter_init()

tweets = tweepy.Cursor(extractor.search, q="Border Wall -filter:retweets", geocode="33.422558,-112.118664,75km").items(2000)
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(2000))

data.to_json(r'C:/Users/u180530/Desktop/FYP/Data/PHOBorderWall.json')
