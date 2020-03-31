import redis

def simpleRedisConnect():
    conn = redis.Redis(host='127.0.0.1',port=6379)
    conn.set("Redis", "Excellent Technology")
    print("Redis is an " + conn.get("Redis"))

simpleRedisConnect();
