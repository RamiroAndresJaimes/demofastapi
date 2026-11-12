from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from users_router import router as user_router

# Automatically creates tables in PostgreSQL if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Main App API"}
