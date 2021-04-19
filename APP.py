import tweepy
import tkinter
import time
import random, os

#Twitter API keys
consumer_key = "your key"
consumer_secret = "your secret"
access_token = "your token"
access_token_secret = "your token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
print (user.name)

x = 0

def nagitotime():
    path="C:\\Users\\Nora\\Desktop\\s\\"  #change to your own path
    files=os.listdir(path)
    img=random.choice(files)
    ok = str(x)
    api.update_with_media (img, "Day " + ok + " of me loving #Nagitokomaeda ❤ ")

while True:
    x = x+1
    nagitotime()
    time.sleep(86400)
