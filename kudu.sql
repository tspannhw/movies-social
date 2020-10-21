select tweet_id, unixtime, sentiment, `location`, `timestamp`, `geo`, `placename`,`coordinates`, friends_count, statuses_count
from sentiment_tweets
where sentiment is not null
order by sentiment desc
