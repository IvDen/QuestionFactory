from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/")
async def root_handler():
    return {"v2": "v2"}
