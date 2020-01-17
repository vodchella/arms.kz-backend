from pkg.config import CONFIG
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


_pg_host = CONFIG['postgres']['host']
_pg_port = CONFIG['postgres']['port']
_pg_user = CONFIG['postgres']['user']
_pg_pass = CONFIG['postgres']['pass']
_pg_pool = int(CONFIG['postgres']['pool'])
_pg_db = CONFIG['postgres']['db']

SQLALCHEMY_DATABASE_URL = f'postgresql://{_pg_user}:{_pg_pass}@{_pg_host}:{_pg_port}/{_pg_db}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=_pg_pool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
