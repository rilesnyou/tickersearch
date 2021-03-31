from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()
#date you want to search from
start_time = int(datetime.datetime(2021, 1, 30).timestamp())

res = list(api.search_submissions(after=start_time,
                                  subreddit='wallstreetbets',
                                  filter=['url', 'author', 'title', 'subreddit'],
                                  #amount of posts you want to look at
                                  limit=20))
for res in res:
    print(res.created_utc)
    print(res.title)
    print(res.url)