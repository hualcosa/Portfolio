consumer_key ='hQUKQ9WYLQtQKkfKaJeFnGgVB'
consumer_secret='cdjbrK256fwABwosF4EdTTB3VE74bljLuMwmrrSMRxYY5ORLNC'

auth = tweepy.OAuthHandler(
   consumer_key, consumer_secret
)
api = tweepy.API(auth,
                 retry_delay=1,
                 retry_count=3,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

pages = []
next_page = api.search("%23TheLastUnicorn%20OR%20%23TheUnicornChronicles%20OR%20%23Intothelandofunicorns%20OR%20%40WishUponUnicorn%20OR%20%23unicornmovie%20OR%20%23wishuponaunicorn", result_type='mixed')
pages.append(next_page)
next_result = next_page.next_results

while next_result:
    next_page = api.search(next_result)
    pages.append(next_page)
    
    # Iterate until there are no more pages left
    try:
        next_result = next_page.next_results
    except:
        next_result = None               

# tests

next_page = api.search("%23TheLastUnicorn", count=500)
tweet = next_page[0]
tweet.user.id
next_page.next_results
next_page = api.search("%23TheLastUnicorn", count=500)
pprint(next_page[0]._json)


# convertendo o json em pandas dataframe
tweets_df = [] 
for page in pages:
    for status in page:
        json = status._json        
        date = json['created_at']
        parrot_id = 'mentions of ecuavisa account'
        userid = json['user']['id']
        title = json['user']['name']
        comment = json['text'],
        language = json['lang']
        
        tweets_df.append([date, parrot_id, userid, title, comment, language])
tweets_df = pd.DataFrame(tweets_df, columns=['postedtime', 'parrot_id', 'userid', 'title', 'body', 'language'])

tweets_df.body = tweets_df.body.apply(lambda t: t[0])