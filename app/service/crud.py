from app.dto.question_dto import QuestionBase, QuestionFromAPI, Question
from app.context.context import AppContext


async def get_questions_from_3rd_api(count: int, ctx: AppContext):
    async with ctx.client.get(f"https://jservice.io/api/random?count={count}") as responce:
        return await responce.text()


async def create_question_in_db(questions_from_request: QuestionBase, ctx: AppContext):
    pass


async def delete_question_in_db(questions_from_request: QuestionBase, ctx: AppContext):
    pass


async def get_question_from_db(questions_from_request: QuestionBase, ctx: AppContext):
    with ctx.db() as session:
        pass