from fastapi import APIRouter

from . import V1


router = APIRouter()
router.include_router(V1.router, prefix="/V1")