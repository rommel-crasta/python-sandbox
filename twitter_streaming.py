#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2983449373-pH31LSzmmrbgXrkZx08FWDnWqxNmWx74aMwLMt4"
access_token_secret = "Q41AgD2NdZ6n2UQWh8YM6nMosCKLENWrfqh1oiUNhp4R9"
consumer_key = "bxZ2ypZgrxusqKvUGnlv1KNew"
consumer_secret = "HiAk5tuYc657MNKSb8odAxnU33fm4nLAAXY10PkhM3uUxbP9XB"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
    	print("error")
    	print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['dubai', 'london', 'mumbai'])