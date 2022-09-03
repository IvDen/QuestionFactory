from fastapi import APIRouter, Depends, Query
from aiohttp import ClientSession
from app.model.request_question import QuestionRequest


# TODO extract router instance to some init file
router = APIRouter()


# @router.get("/question")
# async def get_questions_handler(commons: dict = Depends(dependency.common_parameters)):
#     return commons['q']


@router.post("/questions/")
async def get_questions_handler(questions_count: int = Query(gt=0, le=100)):
    # TODO refactor to level on_strartup and common data
    async with ClientSession() as client:
        async with client.get(f"https://jservice.io/api/random?count={questions_count}") as resp:
            return await resp.text()