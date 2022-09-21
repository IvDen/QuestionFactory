from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.dto import question_dto

from app.model import question_orm


engine = create_engine('postgresql://question_user:hackme@localhost:5555/QuestionFactory')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_question_from_db(question: question_dto.QuestionFromAPI, db: Session):
    return db.query(question_orm.Question).first()


async def get_first_question_from_db(db: Session):
    return db.query(question_orm.Question).first()


# async def get_questions_from_3rd_api(count: int, ctx: AppContext):
#     async with ctx.client.get(f"https://jservice.io/api/random?count={count}") as responce:
#         return await responce.text()


# async def create_question_in_db(questions_from_request: question_dto.QuestionBase, ctx: AppContext):
#     pass
#
#
# async def delete_question_in_db(questions_from_request: question_dto.QuestionBase, ctx: AppContext):
#     pass