from sqlalchemy import Column, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = 'student'

    s_roll = Column(Integer, primary_key=True)
    name = Column(String(30))
    s_class = Column(String(10))
    marks = Column(Integer)
