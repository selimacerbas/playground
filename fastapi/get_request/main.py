from fastapi import Body, FastAPI, Query
from pydantic_core.core_schema import tuple_positional_schema

app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Selim", "category": "kubernetes"},
    {"title": "Title Two", "author": "Kumar", "category": "docker"},
]


@app.get("/")
# async is not needed with FastAPI but we will add it here explicitly.
async def first_api():
    return {"message": "Hello from Selim!"}


@app.get("/books")
async def get_books():
    return BOOKS


# if you change the order with the function below, it will activate the dynamic path api first because fast api applies in order.
@app.get("/books/mybook")
async def read_all_mybooks():
    return {"book_title": "My favorite book!"}


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {"dynamic_param": dynamic_param}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    result = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            result.append(book)
    return result


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str = Query(...)):
    result = []

    for book in BOOKS:
        author = (book.get("author") or "").casefold()
        cat = (book.get("category") or "").casefold()
        if author == book_author.casefold() and cat == category.casefold():
            result.append(book)
    return result


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == updated_book.get("author").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        title = (BOOKS[i].get("title") or "").casefold()
        if title == book_title.casefold():
            BOOKS.pop(i)
            break
