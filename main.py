import tweepy as tw
from datetime import date
import persistence as p
consumer_key= 'gCaaWlM7VvKNJOjkZbubTMTST'
consumer_secret= 'nB4syMYO7WpyXcFkXjfgbT9ePHPm5O3E1Go5RHO8X1paiTJ4P8'
access_token= '4287816021-jQxCWgqXpl3PuueFFMpTqEQ3fUt2oUSQwmEqBRz'
access_token_secret= 'wblNZe49Rwh6v78TgqLv0Il5V1bTdJq0Zj74JUt0BD2UV'

def init():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api

def get_tweet(api):
    search_words = "#dax18"
    date_since = date.today()
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="no",
                       since=date_since).items(2500)
    db = p.init()
    it = 0
    for t in tweets:
        p.insert(db, t._json)
        it = it + 1

    print(it)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_tweet(init())
