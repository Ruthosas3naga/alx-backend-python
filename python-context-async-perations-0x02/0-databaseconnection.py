from contextlib import contextmanager

@contextmanager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name=db_name
        self.conn=None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        print("[INFO] Database connected.")
        return self.conn  # gives the connection to the 'with' block

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("[INFO] Database connection closed.")

        if exc_type:
            print(f"[ERROR] An error occurred: {exc_val}")
            # Returning False means any error is still raised
            return False

