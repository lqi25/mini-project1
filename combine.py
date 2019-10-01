#!/usr/bin/env python
# encoding: utf-8
# Author - Xiaoyu An


import tweepy  # https://github.com/tweepy/tweepy
import json
import TwitterSearch
from TwitterSearch import *




# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if (len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    # write tweet objects to JSON
    file = open('tweet.json', 'w')
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)

    # close the file
    print ("Done")
    file.close()

    for tweet in tweepy.Cursor(api.search,q='BBC').items(20):
        print('Tweet by: @' + tweet.user.screen_name)

    # key word for search in BBC new
    key_word = input("type in the keyword in BBC news to search: \n")

    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords(['BBC News',key_word])  # let's define all words we would like to have a look for
        tso.set_language('en')  #only English tweets
        tso.set_include_entities(False)  # and don't give us all those entity information

        # exclude the retweet!!!

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            # Twitter API credentials
            # warning!!!!
            # Before upload to GIthub, replace them!!!
            consumer_key="",
            consumer_secret="",
            access_token="",
            access_token_secret="")

        file = open('TweetOutput.txt', 'w+')
        print("Writing tweet objects to txt, please wait...")

        number = 0;  # record for number of tweets we have
        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            if number <= 100:
                # file.write('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
                file.write('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
                number += 1
            else:
                file.write("100 tweets we have now!")
                print("100 tweets we have now!")
                break

        print("Done")
        file.close()

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@BBCWorld")
