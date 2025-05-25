import time
import sqlite3 
import functools

# Global query cache
query_cache = {}

# ✅ with_db_connection decorator to manage DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Your DB file
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ cache_query decorator to cache results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get("query") or (args[0] if args else None)
        if query in query_cache:
            print("[CACHE HIT] Returning cached result.")
            return query_cache[query]
        print("[CACHE MISS] Querying database...")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

# ✅ Function to fetch users with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ✅ First call caches the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# ✅ Second call uses the cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
