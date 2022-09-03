from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def root_handler():
    return {"root_handler": "rootv1"}
