import sqlite3 
import functools
from datetime import datetime

# ✅ 1. Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] Executing SQL Query: {query}")
        else:
            print(f"[LOG] No SQL query found.")
        return func(*args, **kwargs)
    return wrapper

# ✅ 2. Connection manager
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Database file
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ 3. Transaction manager (used only for updates/inserts)
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper

# ✅ 4. Function to get a user by ID (fixed indentation!)
@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

# ✅ 5. Call the function
user = get_user_by_id(user_id=1)
print(user)
