import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


  
class TwitterClient(object): 
    def __init__(self): 
        access_token= "1048066110577205250-Eicf5cmeNSX52kE5Gf36uhMhyjVZwZ"
        access_token_secret="r3q0GlD2gE59NxfuwfEXvsjT1mE84zxiqnwqghjAfCAUY"
        consumer_key="NNddksf8K3t1VlSkVLumQvhMZ"
        consumer_secret="mVnTX838n0DRgp8iejXY8Iz3jr9FY52C4VhrJw05ypytFjJuIz"
  
        
        try: 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            self.auth.set_access_token(access_token, access_token_secret) 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 

         
        tweets = [] 
  
          
        fetched_tweets = self.api.search(q = query, count = count) 
        if len(fetched_tweets) !=0:
             
            for tweet in fetched_tweets: 
                 
                parsed_tweet = {}  
                parsed_tweet['text'] = tweet.text 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                
                if tweet.retweet_count > 0: 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
             
            return tweets 
  
        else: 
             
            print("NO tweets found")
            return 0
  
def aditya(X): 
     
    connection = TwitterClient() 
    
    tweets = connection.get_tweets(query =X, count = 2000) 
  
    if tweets!=0:
    
        positivetweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        print("Positive tweets percentage: {} %".format(100*len(positivetweets)/len(tweets))) 
        
        negativetweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        print("Negative tweets percentage: {} %".format(100*len(negativetweets)/len(tweets))) 
        
        print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(negativetweets) - len(positivetweets))/len(tweets))) 
        try:
            x=int(input("Do you Want to Show Top Tweets Enter 1 for Yes else press Enter"))
            if x==1:
                print("\n\nPositive tweets:") 
                for tweet in positivetweets[:10]: 
                    print(tweet['text'].translate(non_bmp_map))
                    print('\n')
              

                print("\n\nNegative tweets:") 
                for tweet in negativetweets[:10]: 
                    print(tweet['text'].translate(non_bmp_map)) 
                    print('\n')
        except:
            quit()
