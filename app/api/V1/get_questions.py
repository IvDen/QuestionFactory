from fastapi import APIRouter, Depends, Query
from aiohttp import ClientSession


router = APIRouter()


# @router.get("/question")
# async def get_questions_handler(commons: dict = Depends(dependency.common_parameters)):
#     return commons['q']


@router.post("/questions/")
async def get_questions_handler(questions_count: int = Query(gt=0, le=100)):
    # crud.get_questions_from_3rd_api(questions_count,)
    # TODO refactor to level on_strartup and common data
    async with ClientSession() as client:
        async with client.get(f"https://jservice.io/api/random?count={questions_count}") as resp:
            return await resp.text()