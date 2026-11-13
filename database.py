from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Format: postgresql+psycopg://<user>:<password>@<host>:<port>/<database_name>
DATABASE_URL = "postgresql+psycopg://postgres:password2128@localhost:5432/demo"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()