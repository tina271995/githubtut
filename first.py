from bs4 import BeautifulSoup
from fastapi import FastAPI
import requests

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/profile")
async def profile(username: str):
    if username:
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_url = soup.find("meta", property="og:image")["content"]

        response = requests.get(img_url)
    
    return {"URL": response}