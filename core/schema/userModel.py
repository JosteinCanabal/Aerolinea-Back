from pydantic import BaseModel


class userRequest(BaseModel):
    username: str
    fullname: str
    password: str


class User(userRequest):
    id: int
    fullname: str
    username: str
    password: str

    class Config:
        orm_mode = True
