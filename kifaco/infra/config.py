import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Config:
    APP_NAME = "kifaco"
    CACHED_TTL = int(os.getenv("CACHED_TTL", 10))
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", 'mysql+pymysql://root:admin@localhost:3306/kifaco')
    AMOUNT_PROCESS = int(os.getenv("AMOUNT_PROCESS", 1))
    DATABASE_POOL_RECYCLE = int(os.getenv("DATABASE_POOL_RECYCLE", 3600))
    DATABASE_POOL_SIZE = int(os.getenv("DATABASE_POOL_SIZE", 2))


class Conn:
    engine = create_engine(
        Config.SQLALCHEMY_DATABASE_URI,
        pool_recycle=Config.DATABASE_POOL_RECYCLE,
        pool_size=Config.DATABASE_POOL_SIZE,
        pool_pre_ping=True,
        max_overflow=1,
        pool_timeout=10
    )
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
