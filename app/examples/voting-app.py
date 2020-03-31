import redis

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
conn = redis.Redis(host='127.0.0.1',port=6379)

def article_vote(user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS
