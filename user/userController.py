from fastapi import APIRouter, Depends, HTTPException
from app.database.database import engine, SessionLocal, get_db
from app.core.schema.userModel import userRequest, User as userResponse
from app.user.userService import create_user, find_by_id, get_users, update, delete
from sqlalchemy.orm import Session

userRouter = APIRouter()


@userRouter.post("/users", response_model=userResponse)
def create(post: userRequest, db: Session = Depends(get_db)):
    return create_user(db=db, user1=post)


@userRouter.get("/users/{id}", response_model=userResponse)
def getUser(id: int, db: Session = Depends(get_db)):
    db_user = find_by_id(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user


@userRouter.get("/users", response_model=list[userResponse])
def get_all(db: Session = Depends(get_db)):
    db_users = get_users(db)
    if db_users is None:
        raise HTTPException(status_code=404, detail="")
    return db_users


@userRouter.put("/users/{id}", response_model=userResponse)
def update_user(id: int, obj: userRequest, db: Session = Depends(get_db)):
    obj = update(db, id, obj)
    if obj is None:
        raise HTTPException(status_code=404, detail="Error al actualizar")
    return obj


@userRouter.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return delete(db, id)
