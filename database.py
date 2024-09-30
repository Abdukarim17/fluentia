from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#dean replace with mysql url
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()