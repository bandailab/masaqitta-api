from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user_router
from routes.tweet import tweet_router

# App object
app = FastAPI()

origins = [
  'http://localhost:3000',
  'http://localhost',
  ]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(tweet_router)
