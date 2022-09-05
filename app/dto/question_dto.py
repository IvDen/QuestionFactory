import datetime
from pydantic import BaseModel


class QuestionBase(BaseModel):
    count: int


class QuestionFromAPI(QuestionBase):
    id: int
    question: str
    answer: str
    airdate: datetime.datetime


class Question(QuestionFromAPI):
    # id: int

    class Config:
        orm_mode = True
