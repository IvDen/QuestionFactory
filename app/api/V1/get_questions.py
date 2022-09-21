from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.dto import question_dto
from app.service.crud import get_first_question_from_db

# from app.context_app import context

router = APIRouter()


# @router.post("/questions/")
# async def get_questions_handler(questions: question_dto.QuestionBase, db: Session = Depends(dependency.db_session)):
#     # crud.get_questions_from_3rd_api(questions_count,)
#     # TODO refactor to level on_strartup and common data
#     async with ClientSession() as client:
#         async with client.get(f"https://jservice.io/api/random?count={questions.count}") as resp:
#             return await resp.text()


@router.get('/guestion/', tags=['test_db'], response_model=question_dto.QuestionFromDb)
async def get_first_question():
    engine = create_engine('postgresql://question_user:hackme@localhost:5555/QuestionFactory')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    result = await get_first_question_from_db(SessionLocal())
    return result
