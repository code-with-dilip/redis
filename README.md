# REDIS

- Redis is a very fast non-relational database that stores a mapping of keys to five different types of values
- Redis supports the writing of its data to disk automatically in two different ways, and can store data in four structures in addition to plain string keys as memcached does.

**“What happens when my server gets turned off?”**  

- Redis has two different forms of persistence available for writing in-memory data to disk in a compact format.
  - The first method is a point-in-time dump either when certain conditions are met (a number of writes in a given period) or when one of the two dump-to-disk commands is called.
  - Uses an append-only file that writes every command that alters data in Redis to disk as it happens
  - Redis supports master/slave replication where slaves connect to the master and receive an initial copy of the full database. As writes are performed on the master, they’re sent to all connected slaves for updating the slave datasets in real time.

## REDIS Data Structure

- Redis allows us to store keys that map to any one of five different data structure types;
  - STRINGs,
  - LISTs,
  - SETs,
  - HASHes, and
  - ZSETs.

### String

- In Redis, STRINGs are similar to strings that we see in other languages or other key-value stores.

```
GET - Fetches the data stored at the given key
SET - Sets the value stored at the given key
DEL - Deletes the value stored at the given key (works for all types)
```

  **Example**  

```
~/Dilip/study/codewithdilip/redis » redis-cli
127.0.0.1:6379> SET dilip 32
OK
127.0.0.1:6379> get dilip
"32"
127.0.0.1:6379> del dilip
(integer) 1
127.0.0.1:6379>
```

### LISTS

- In the world of redis, we can have a list against a key.
- You are allowed to have duplicate values for a given key
- LISTs in **Redis** store an ordered sequence of strings

```
RPUSH	Pushes the value onto the right end of the list
LRANGE	Fetches a range of values from the list
LINDEX	Fetches an item at a given position in the list
LPOP	Pops the value from the left end of the list and returns it
```

#### Example

```
127.0.0.1:6379> clear
127.0.0.1:6379> lpush java java1 // adds an element to the left of the key
(integer) 1
127.0.0.1:6379> rpush java java2 // adds an element to the right of the key
(integer) 2
127.0.0.1:6379> lrange java 0 -1 // retrieves all the elements starting from 0 Index
1) "java1"
2) "java2"
127.0.0.1:6379> lpop java  // returns and removes an element from the left side of the list
"java1"
127.0.0.1:6379> rpop java  // returns and removes an element from the right side of the list
"java2"
```

### SETS

- Sets are very similar to LISTS.
- Duplicates are not allowed
- **SETS** in Redis store an unordered sequence of strings

#### Commands:

```
SADD	Adds the item to the set
SMEMBERS	Returns the entire set of items
SISMEMBER	Checks if an item is in the set
SREM	Removes the item from the set, if it exists
```

#### Example

```
127.0.0.1:6379> sadd java java1 // adds a member to the set
(integer) 1
127.0.0.1:6379> sadd java java2 // adds a member to the set
(integer) 1
127.0.0.1:6379> smembers java // returns all the members in the set
1) "java2"
2) "java1"
127.0.0.1:6379> sismember java java1 // returns 1 if the members exist in the set
(integer) 1
127.0.0.1:6379> sREM java java1 // removes a member from the set
```

### HASH

- Redis HASHes store a mapping of keys to values.
- When using hash, we cannot set the key as a plain string.

| Hash-Key  | Hash-Value |
| ------------- | ------------- |
| key(Not a plain String)  | subkey-value|      

#### Example

| Hash-Key  | Hash-Value |
| ------------- | ------------- |
| java:language  | java1 2000|      


#### Commands

```
HSET	Stores the value at the key in the hash
HGET	Fetches the value at the given hash key
HGETALL	Fetches the entire hash
HDEL	Removes a key from the hash, if it exists
```

#### Example

```
127.0.0.1:6379> hset java:language java2 2000 //sets a new hash
(integer) 1
127.0.0.1:6379> hset java:language java1 1999 //add a new value hash to the existing key
(integer) 0
127.0.0.1:6379> hget java:language java1 //gets a value for a given hashkey and subkey existing key
"1999"
127.0.0.1:6379> hgetall java:language //retrieves all the values for a given hashkey
1) "java1"
2) "1999"
3) "java2"
4) "2000"
127.0.0.1:6379> hdel java:language java1 // deletes a hash value for the given hashkey and subkey
(integer) 1
```
