from fastapi import FastAPI
import os, psycopg2

app = FastAPI()
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME", "app"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", "5432"),
)
@app.get("/")
def read_msg():
    with conn.cursor() as cur:
        cur.execute("SELECT msg FROM greetings LIMIT 1;")
        row = cur.fetchone()
        return row[0] if row else "no data"
