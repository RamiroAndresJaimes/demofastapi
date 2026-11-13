from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from user import User
from sqlalchemy import select
from database import get_db
from sqlalchemy.orm import Session


class UserCreate(BaseModel):
    name: str
    email: EmailStr


router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    stmt = select(User.id).where(User.email == user.email)
    matches = db.scalar(stmt) 

    if matches is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = select(User)
    users = db.scalars(stmt).all()
    return users

@router.delete("/{user_id}")
def delete_users(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404, 
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return None

