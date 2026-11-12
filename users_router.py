from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from user import User
from database import get_db
from sqlalchemy.orm import Session


class UserCreate(BaseModel):
    name: str
    email: EmailStr


router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_all_users():
    return users


