from sqlalchemy import Column, Boolean, Integer, String, Text, PrimaryKeyConstraint, UniqueConstraint, DateTime
from app.context_app.database import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    airdate = Column(DateTime, nullable=False)
