from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status

# Body is not letting us data validation. So instead, we prefer to use pydantic.
from pydantic import BaseModel, Field

# BOOKS = [
#     {"title": "Title One", "author": "Selim", "category": "kubernetes"},
#     {"title": "Title Two", "author": "Kumar", "category": "docker"},
# ]

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed to create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_digits=100)
    rating: int
    model_config = {
        "json_schema_extra": {
            "exmaple": {
                "title": "A new book",
                "author": "selim",
                "description": "This book is awesome",
                "rating": 5,
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "Selim", "A very cool book", "5"),
    Book(2, "IaC Enterprise Scae", "Kumar", "A very great book", "4"),
    Book(3, "Kubernetes", "Seim", "A very awesome book", 5),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return BOOKS


# path parameter
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


# query parameter
@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    result = []
    for book in BOOKS:
        if book.rating == book_rating:
            result.append(book)
    return result


@app.post("/books/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookRequest):
    # ** operator will pass the key/value from BookRequest() into the Book() constructor
    new_book = Book(**book.model_dump())
    BOOKS.append(find_book_id(new_book))


# we want all ids to be unique and in order
def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            new_book = Book(**book.model_dump())
            BOOKS[i] = new_book

    if not changed:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
