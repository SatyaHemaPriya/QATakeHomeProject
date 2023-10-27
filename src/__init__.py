from fastapi import APIRouter

from src.books.router import router as books_router

router = APIRouter(prefix="/api")
router.include_router(router=books_router)
