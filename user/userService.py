from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.schema.userModel import User as userRequest
from app.core.models.models import User
from app.core.security import verify_password, get_password_hash


def create_user(db: Session, user1: userRequest):
    fake_psw = get_password_hash(user1.password)
    db_user = User(fullname=user1.fullname, password=fake_psw, username=user1.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, email: str, password: str):
    user = db.query(User).filter(User.username == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def find_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def update(db: Session, id: int, obj: userRequest):
    # db_user = User(id=id, password=obj.password, fullname=obj.fullname, username=obj.username)
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return None
    user_data = obj.dict(exclude_unset=True)

    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete(db: Session, id: int):
    obj = db.query(User).filter(User.id == id).first()
    if obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(obj)
    db.commit()
    return {"ok": True}
