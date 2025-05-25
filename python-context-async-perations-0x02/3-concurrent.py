import asyncio
import aiosqlite

# Async function to fetch all users and return them
async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        return users  # ✅ returning result

# Async function to fetch users older than 40 and return them
async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        older_users = await cursor.fetchall()
        return older_users  # ✅ returning result

# Run both queries concurrently and print the results
async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All Users:")
    for user in users:
        print(user)

    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)

# Start the asynchronous process
asyncio.run(fetch_concurrently())
