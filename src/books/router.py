from fastapi import APIRouter

router = APIRouter()


@router.get("/books")
async def list_books():
    return {
        "books": [
            {"book_id": "1", "title": "The Great Gatsby", "author": "Some Author"},
            {"book_id": "2", "title": "The DaVinci Code", "author": "Some Author"},
        ]
    }


@router.post("/books")
async def add_book():
    return {"message": "Book has been added successfully."}


@router.put("/books/{book_id}")
async def update_book(book_id: int):
    return {"message": f"Book {book_id} has been updated successfully."}


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return {"message": f"Book {book_id} has been deleted successfully."}


@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"book_id": {book_id}, "title": "The Great Gatsby"}
