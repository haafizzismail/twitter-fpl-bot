import tweepy

consumer_key = 'BsTCXHIphBfvRrcDxI20Hqii7'
consumer_secret = 'hABFLkjl9wk5Zu37B78wxUN1C3r3rfx8WSe7N4Y12bSBnVZtvf'
access_token = '1472919976914788353-fHOfR9kaWuzLyXOZ4EIWtmYidCQMhz'
access_token_secret = 'PZj3tHkHyFptgBqgtZ57Hllrbe0urss9oXi6ooX5q3a34'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

bot_id = int(api.verify_credentials().id_str)
user_id = 761568335138058240

class IDPrinter(tweepy.Stream):

    def on_status(self, tweet):
        print("Tweet found!")
        print(f"{tweet.user.screen_name} - {tweet.text}")
        if tweet.in_reply_to_status_id is None and tweet.user.id != bot_id and tweet.user.id == user_id:
            if not tweet.retweeted and "RT @" not in tweet.text and "Goal -" in tweet.text:
                    try:
                        print("Attempting to retweet...")
                        api.retweet(tweet.id)
                        print("Retweet successful.")
                    except Exception as err:
                        print(err)


printer = IDPrinter(consumer_key, consumer_secret, access_token, access_token_secret)
printer.filter(track=["Assist"], languages=["en"])

# on pythonanywhere

# import tweepy

# consumer_key = 'BsTCXHIphBfvRrcDxI20Hqii7'
# consumer_secret = 'hABFLkjl9wk5Zu37B78wxUN1C3r3rfx8WSe7N4Y12bSBnVZtvf'
# access_token = '1472919976914788353-fHOfR9kaWuzLyXOZ4EIWtmYidCQMhz'
# access_token_secret = 'PZj3tHkHyFptgBqgtZ57Hllrbe0urss9oXi6ooX5q3a34'


# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# bot_id = int(api.verify_credentials().id_str)
# user_id = 761568335138058240

# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, tweet):
#         print("Tweet found!")
#         print(f"{tweet.user.screen_name} - {tweet.text}")
#         if tweet.in_reply_to_status_id is None and tweet.user.id != bot_id and tweet.user.id == user_id:
#             if not tweet.retweeted and "RT @" not in tweet.text and "Goal -" in tweet.text:
#                     try:
#                         print("Attempting to retweet...")
#                         api.retweet(tweet.id)
#                         print("Retweet successful.")
#                     except Exception as err:
#                         print(err)

# stream_listener = MyStreamListener()
# stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
# stream.filter(track=["Assist"], languages=["en"])
