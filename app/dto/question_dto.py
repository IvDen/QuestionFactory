import datetime
from pydantic import BaseModel, Field


class QuestionBase(BaseModel):
    count: int = Field(gt=0, le=100)


class QuestionFromAPI(BaseModel):
    id: int
    question: str
    answer: str
    airdate: datetime.datetime


class QuestionFromDb(QuestionFromAPI):
    class Config:
        orm_mode = True
