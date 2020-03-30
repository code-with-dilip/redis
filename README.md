# REDIS

- Redis is a very fast non-relational database that stores a mapping of keys to five different types of values
- Redis supports the writing of its data to disk automatically in two different ways, and can store data in four structures in addition to plain string keys as memcached does.

**“What happens when my server gets turned off?”**  

- Redis has two different forms of persistence available for writing in-memory data to disk in a compact format.
  - The first method is a point-in-time dump either when certain conditions are met (a number of writes in a given period) or when one of the two dump-to-disk commands is called.
  - Uses an append-only file that writes every command that alters data in Redis to disk as it happens
  - Redis supports master/slave replication where slaves connect to the master and receive an initial copy of the full database. As writes are performed on the master, they’re sent to all connected slaves for updating the slave datasets in real time.

## REDIS Data Structure

- Redis allows us to store keys that map to any one of five different data structure types; STRINGs, LISTs, SETs, HASHes, and ZSETs.

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
