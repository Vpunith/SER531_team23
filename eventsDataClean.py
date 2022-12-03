import pandas as pd

tweetData = pd.read_csv('previousTweetData.csv')
tweetData1 = tweetData.dropna(axis=0, subset=["Date", "Tweet_Text", "Source", "User_ID", "Lat", "Lng"])
tweetData2 = tweetData1[~tweetData1['Tweet_Text'].str.contains(r'[^\x00-\x7F]+')]
tweetData3 = tweetData2[~tweetData2['Source'].str.contains(r'[^\x00-\x7F]+')]
newTweetData = tweetData3.to_csv('ObtainedTweet.csv', index=False)

userData = pd.read_csv('previousUserData.csv')
userData1 = userData.dropna(axis=0, subset=["ID", "Name", "Screen_Name", "User_Location"])
userData2 = userData1[~userData1['Name'].str.contains(r'[^\x00-\x7F]+')]
userData3 = userData2[~userData2['User_Location'].str.contains(r'[^\x00-\x7F]+')]
newUserData = userData3.to_csv('ObtainedUsers.csv', index=False)

eventData = pd.read_csv('previousEventData.csv')
eventCols= ["event_id", "start_time", "city", "state", "country", "lat", "lng"]
newEventData = eventData[eventCols]
newEventData = newEventData.dropna(axis=0, subset=['event_id', 'start_time', 'city'])
newEventData.to_csv("ObtainedEvents.csv", index=False)

newuserData = pd.read_csv('previousUsers.csv')
newEventData1 = newuserData.dropna(axis=0, subset=['user_id', 'birthyear', 'location', 'timezone'])
newEventData1.to_csv("ObtainedUsers_id.csv", index=False)
