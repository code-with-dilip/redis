import redis
import sys
import time

def optionsForUser():
    print('1 - addItem')
    print('2 - exit')

def getUserInput():
    selectedOption = input("Choose one of the above option: ")
    return selectedOption

def exitProgram():
    print('********** Exiting the Program **********')
    print('********** Bye **********')
    sys.exit()

conn = redis.Redis(host='127.0.0.1',port=6379)
token = '123'
conn.hset('login:',token, 'dilip123') # token -> user

def retrieveUser(token):
    return conn.hget('login:', token)

def get_login():
    user = retrieveUser(token)
    print('user is ' + user)

def update_token(token, user, item = None):
    timestamp = time.time()
    intToken = int(token)
    conn.hset('login:', token, user)
    conn.zadd('recent:', intToken, timestamp)
    if item:
        conn.zadd('viewed:'+token, item, timestamp)
        conn.zremrangebyrank('viewed:'+token, 0, -26)
        print('added item '+str(item))

#get_login()

def addItem():
    itemsTobeAdded = input("How many items to be added: ")
    for x in range(itemsTobeAdded):
        update_token(token, retrieveUser(token), x)
    print(conn.zcount('viewed:'+token, '-inf' , '+inf'))


while True:
    optionsForUser()
    option = getUserInput()
    if(option==2):
        exitProgram()
    else:
        addItem()
