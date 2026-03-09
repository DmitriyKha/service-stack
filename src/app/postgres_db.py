from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.models import Base

DATABASE_URL = "postgresql+psycopg2://user:class@postgres:5432/test"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)

def init_db():
    Base.metadata.create_all(bind=engine)