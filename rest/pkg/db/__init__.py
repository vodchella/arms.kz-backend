import databases
from pkg.config import CONFIG
from sqlalchemy.ext.declarative import declarative_base


_pg_host = CONFIG['postgres']['host']
_pg_port = CONFIG['postgres']['port']
_pg_user = CONFIG['postgres']['user']
_pg_pass = CONFIG['postgres']['pass']
_pg_pool = int(CONFIG['postgres']['pool'])
_pg_db = CONFIG['postgres']['db']

DATABASE_URL = f'postgresql://{_pg_user}:{_pg_pass}@{_pg_host}:{_pg_port}/{_pg_db}'

Base = declarative_base()

db = databases.Database(DATABASE_URL)

