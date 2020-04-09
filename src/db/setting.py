from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE_URL

DATABASE = DATABASE_URL

ENGINE = create_engine(
    DATABASE,
    encoding = 'utf-8'
)

# 操作ログ出力用
# ENGINE = create_engine(
#     DATABASE,
#     encoding = 'utf-8',
#     echo=True
# )

DBSession = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind = ENGINE
))

Base = declarative_base()
Base.query = DBSession.query_property()