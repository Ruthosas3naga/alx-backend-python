import sqlite3 
import functools


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



# ✅ 4. Function to get a user by ID (fixed indentation!)
@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

# ✅ 5. Call the function
user = get_user_by_id(user_id=1)
print(user)
