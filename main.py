from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import json
json_open = open('dummytweet.json', 'r')
json_load = json.load(json_open)

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
    return json_load

