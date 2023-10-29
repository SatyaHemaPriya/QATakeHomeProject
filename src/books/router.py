from random import randint

from fastapi import APIRouter, HTTPException

from src.books.schema import AddBookRequestSchema, BookResponseSchema, BookSchema, UpdateBookRequestSchema
from src.validate import validate

router = APIRouter(tags=["books"])
books = [
    {"unique_id": 1, "title": "The Great Gatsby", "author": "Some Author"},
    {"unique_id": 2, "title": "The DaVinci Code", "author": "Some Author"},
]


def _generate_unique_id():
    return randint(1, 30)


def _add_book(title, author):
    validate(title, author)
    book_id = _generate_unique_id()
    books.append({"unique_id": book_id, "title": title, "author": author})
    return book_id


def _remove_book(unique_id):
    book_removed = False
    for book in books:
        if book["unique_id"] == unique_id:
            books.remove(book)
            book_removed = True
    if not book_removed:
        raise HTTPException(status_code=404, detail="Book not found")


@router.get(
    path="/books",
    response_model=list[BookSchema],
    status_code=200,
    description="List books in the library",
    response_description="Books listed in the library",
)
async def list_books():
    return books


@router.post(
    path="/books",
    response_model=BookResponseSchema,
    status_code=200,
    description="Add book to the library",
    response_description="Book added to the library",
)
async def add_book(add_book_request: AddBookRequestSchema):
    book_id = _add_book(add_book_request.title, add_book_request.author)
    return BookResponseSchema(unique_id=book_id)


@router.put(
    path="/books/{book_id}",
    response_model=BookResponseSchema,
    status_code=200,
    description="Update book in the library",
    response_description="Book updated in the library",
    responses={404: {"description": "Book not found"}},
)
async def update_book(book_id: int, request_body: UpdateBookRequestSchema):
    return BookResponseSchema(unique_id=book_id)


@router.delete(
    path="/books/{book_id}",
    response_model=BookResponseSchema,
    status_code=200,
    description="Delete book in the library",
    response_description="Book deleted in the library",
    responses={404: {"description": "Book not found"}},
)
async def delete_book(book_id: int):
    _remove_book(book_id)
    return BookResponseSchema(unique_id=book_id)


@router.get(
    path="/books/{book_id}",
    response_model=BookSchema,
    status_code=200,
    description="Get book in the library",
    response_description="Book found in the library",
    responses={404: {"description": "Book not found"}},
)
async def get_book(book_id: int):
    result_book = [book for book in books if book["unique_id"] == book_id]
    if not result_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return result_book[0]
