from __future__ import absolute_import, print_function
import tweepy
import json
from pprint import pprint

import random
consumer_key=""
consumer_secret = ""
access_token = ""
access_token_secret = ""

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)
tweets = []
tmpTweets = api.user_timeline()
kelime=list()
sansur=["@","http","►","RT"]

for i in api.home_timeline():
    for alt in str(i.text).split():
        if not alt.startswith("@"):
            if not alt.startswith("http"):
                if not alt.startswith("►"):
                    if alt.replace("."," "):
                        if alt.replace("$",""):
                            kelime.append(alt.lower())



m=""
sayı=random.randrange(3,10)
while sayı<9:
    m+=kelime[random.randrange(0,len(kelime))]+" "

    sayı+=1
print(m)