from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_pwd = os.getenv('DB_PWD')
db_port = os.getenv('DB_PORT')

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = db_host,
        dbname = db_name,
        user = db_username,
        password = db_pwd,
        port = db_port,
    )

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Write scripts here


except Exception as e:
    print(str(e))

finally:
    if conn is not None:
        conn.close()

    if cur is not None:
        cur.close()