from pydantic import BaseModel
from fastapi import APIRouter
from starlette import status
from models import Users
from passlib.context import CryptContext
from routers.todos import db_dependency

router = APIRouter()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, request: CreateUserRequest):
    model = Users(
        email=request.email,
        username=request.username,
        first_name=request.first_name,
        last_name=request.last_name,
        role=request.role,
        hashed_password=bcrypt_context.hash(request.password),
        is_active=True,
    )
    db.add(model)
    db.commit()
