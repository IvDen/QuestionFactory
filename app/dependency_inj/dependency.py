# from fastapi import APIRouter, Depends
# import main
# from app.context.init_context import AppContext
#
#
# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100, ctx: AppContext = main.context):
#     return {"q": q, "skip": skip, "limit": limit, "ctx": ctx}