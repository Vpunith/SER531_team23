import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import time


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            csvFile = open('EventData.csv', 'a')
            csvFile.write(data)
            csvFile.write('\n')
            csvFile.close()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)
        return True


auth = tweepy.OAuthHandler("jSYOQvmz9lmZco947OWVVgdze",
                           "ri08DWJdyuInIPLAkwxj2Sc3T5RL5M1tjaFkRyQvD7hpLgA9Yb")
auth.set_access_token("1458707545774706695-hEyjIWrJcu855PknNJqmQQEsKkU34E",
                      "TREA0Bxx61KDIQvKD6R7amxWRJbhusholIRTN1Y0KF0in")

api = tweepy.API(auth)

events =["Music", "Dance", "Soccer", "Cricket", "Sundevils", "ComputerScience"]

TweetList = Stream(auth, MyListener())
TweetList.filter(track=['events', 'event'])


for tweetdata in api.search(q="Python", lang="en", rpp=10, geocode="33.4246° N, 111.9224° W"):
    print(f"{tweetdata.user.name}:{tweetdata.text}")

location = api.geo_search(query="USA", granularity="country")
location_id = location[0].id

TweetList = api.search(q="place:%s" % location_id, limit=900, lang="en")
for tweetls in TweetList:
    print(f"{tweetls.text} : {tweetls.place.name}")