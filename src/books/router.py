from fastapi import APIRouter, Request
from random import randint
from src.schema import AddBookRequestSchema
from src.validate import validate

router = APIRouter()
books = [
    {"unique_id": 1, "title": "The Great Gatsby", "author": "Some Author"},
    {"unique_id": 2, "title": "The DaVinci Code", "author": "Some Author"},
]

def _generate_unique_id():
    return randint(1, 30)


def _add_book(title, author):
    validate(title, author)
    books.append({"unique_id": _generate_unique_id(), "title": title, "author": author})


def _remove_book(id):
    for book in books:
        if book["unique_id"] == id:
            books.remove(book)


@router.get("/books")
async def list_books():
    return books


@router.post("/books")
async def add_book(add_book_request: AddBookRequestSchema):
    _add_book(add_book_request.title, add_book_request.author)
    return {"message": "Book has been added successfully."}


@router.put("/books/{book_id}")
async def update_book(book_id: int):
    return {"message": f"Book {book_id} has been updated successfully."}


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    _remove_book(book_id)
    return {"message": f"Book {book_id} has been deleted successfully."}


@router.get("/books/{book_id}")
async def get_book(book_id: int):
    result_book = None
    for book in books:
        if book["unique_id"] == book_id:
            result_book = book
    return result_book
