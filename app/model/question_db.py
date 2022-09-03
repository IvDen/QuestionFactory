import dataclasses
import datetime


@dataclasses.dataclass
class Question:
    id: int
    question_body: str
    answer: str
    air_date: datetime.datetime
