from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import json

tweet_json_open = open('dummytweet.json', 'r')
tweet_json_load = json.load(tweet_json_open)

user_json_open = open('dummyuser.json', 'r')
user_json_load = json.load(user_json_open)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/tweets")
def get_tweets():
    return tweet_json_load

@app.get("/user")
def get_user():
    return user_json_load 
