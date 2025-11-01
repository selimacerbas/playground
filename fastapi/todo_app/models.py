"""DB Tables"""

from db import Base
from typing import Optional
from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Integer, String, Boolean, Text, ForeignKey, DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

# If you’re on Postgres and want case-insensitive email uniqueness:
# from sqlalchemy.dialects.postgresql import CITEXT


class Role(str, PyEnum):
    USER = "user"
    ADMIN = "admin"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)  # index=True not needed
    # For Postgres with CITEXT:
    # email: Mapped[str] = mapped_column(CITEXT(), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=sa.text("true"),  # "1" for MySQL/SQLite
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role, name="user_role"), nullable=False, server_default=sa.text("'user'")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"Users(id={self.id!r}, email={self.email!r}, role={self.role!r})"


class Todos(Base):
    __tablename__ = "todos"

    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String)
    # description = Column(String)
    # priority = Column(Integer)
    # priority = Column(Boolean, default=False)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    priority: Mapped[int] = mapped_column(Integer)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
