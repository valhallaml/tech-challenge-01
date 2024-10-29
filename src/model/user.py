from sqlalchemy import Integer, String, Column
from src.core.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256), nullable=True)
    mail = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
