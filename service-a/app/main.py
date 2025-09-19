from fastapi import FastAPI
import os, requests

app = FastAPI()
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b:8081")

@app.get("/")
def get_value():
    r = requests.get(f"{SERVICE_B_URL}/", timeout=5)
    r.raise_for_status()
    return r.text
