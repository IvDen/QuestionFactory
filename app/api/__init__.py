from fastapi import APIRouter

from . import V1
from . import V2

router = APIRouter()

router.include_router(V1.router, prefix="/V1")
router.include_router(V2.router, prefix="/V2")
