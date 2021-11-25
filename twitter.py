# coding: UTF-8

import tweepy
import time

# consumer　第一引数に(consumer　key)　第二引数に(consumer　secret) #
auth = tweepy.OAuthHandler('***','***')
# ACCESS_TOKEN_KEY 第一引数に(Access token)　第二引数に(Access token secret) #
auth.set_access_token('***', '***')

# wait_on_rate_limit = レート制限が補充されるのを自動的に待つかどうか #
# wait_on_rate_limit_notify = Tweepyがレート制限の補充を待っているときに通知を出力するかどうか #
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# '#ブログ, #旅行'をそれぞれ３件ずついいね #
# 取得したいキーワード #
search_list = ['#カレー','#スープカレー']
# ツイート数10件 #
tweet_count = 10

for search in search_list:
    print('Searching... {}' .format(search))
    # サーチ結果 #
    search_result = api.search(q=search, count=tweet_count)
    for tweet in search_result:
        tweet_id = tweet.id
        try:
            # いいねの処理 #
            api.create_favorite(id=tweet_id)
            print('Tweet_liked')
            time.sleep(4)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
