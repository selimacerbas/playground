from typing import Annotated

from fastapi.routing import APIRouter

from pydantic import Field
from pydantic import BaseModel
from starlette import status
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from sqlalchemy.orm import Session

from models import Todos
from db import session_local

router = APIRouter()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    # Normally we are defining id as well at the db models. But thanks to sqlalchemy this ids are automatically atteched to dbs.
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/", status_code=status.HTTP_200_OK)
# This part is simply dependency injection.
async def read_all(db: db_dependecy):
    return db.query(Todos).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependecy, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependecy, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    # this adds
    db.add(todo_model)
    # this flushed to db
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# At the argument passing, we have to make sure that Request is coming before the id.

async def update_todo(
    db: db_dependecy,
    todo_request: TodoRequest,
    todo_id: int,
):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependecy, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
