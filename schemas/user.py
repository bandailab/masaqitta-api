from pydantic import BaseModel

class User(BaseModel):
    name: str
    userName: str
    greeting: str
    imageURL: str
    follow: str
    follower: str
