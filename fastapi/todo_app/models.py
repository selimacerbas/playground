"""DB Tables"""

from db import base
from typing import Optional
from sqlalchemy import Integer, String, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column


class Todos(base):
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
