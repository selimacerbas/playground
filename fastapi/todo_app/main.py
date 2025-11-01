from routers import auth, todos
from fastapi import FastAPI
from models import base
from db import engine

app = FastAPI()
base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
