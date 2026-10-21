from collections.abc import Generator

from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine


from app.core.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind= engine,
    class_=Session,
    autoflush=False,
    expire_on_commit=False
)

def get_db()-> Generator[Session,None,None]:
    """Provide database session for each requests"""
    db = SessionLocal()

    try:
        yield db()
    finally:
        db.close()

    