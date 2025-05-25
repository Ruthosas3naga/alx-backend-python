import sqlite3

# Step 1: Create the class-based context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        print("[INFO] Connected to database.")
        return self.conn  # this is what you get in the 'as' part

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("[INFO] Database connection closed.")

        if exc_type:
            print(f"[ERROR] Something went wrong: {exc_val}")
            return False  # Let Python raise the error

# Step 2: Use it with the 'with' statement to run the query
with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("[RESULTS]")
    for row in results:
        print(row)
