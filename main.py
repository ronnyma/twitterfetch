#!/usr/bin/env python

from datetime import date
from get_docker_secret import get_docker_secret

import tweepy as tw

from persistence import *

consumer_key = get_docker_secret('consumer_key', default=None)
consumer_secret = get_docker_secret('consumer_secret', default=None)
access_token = get_docker_secret('access_token', default=None)
access_token_secret = get_docker_secret('access_token_secret', default=None)


def init():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api


def get_tweet(api):
    search_words = "#dax18 OR #debatten OR #dagsrevyen"
    date_since = date.today()

    init = Persistence()
    it = 0

    tweets = tw.Cursor(api.search,
                       tweet_mode="extended",
                       q=search_words,
                       lang="no",
                       since=date_since).items(5000)

    for t in tweets:
        init.insert({'tweet': t._json, 'fulltext': t.full_text})
        it = it + 1

    print(f'{date_since}: Fetched {it} tweets.')
    init.close()


if __name__ == '__main__':
    get_tweet(init())
