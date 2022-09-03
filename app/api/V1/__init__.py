from fastapi import APIRouter

from . import root
from . import get_questions

router = APIRouter()

router.include_router(root.router)
router.include_router(get_questions.router)
