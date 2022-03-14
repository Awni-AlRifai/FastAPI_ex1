from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/crud'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@db:5432/crud'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
