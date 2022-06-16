from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.user.userService import authenticate

auth = APIRouter()


# @auth.get("/login/")
@auth.post("/login/")
def authenticated(username: str, password: str, db: Session = Depends(get_db)):
    return authenticate(db, username, password)
