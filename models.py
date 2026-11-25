from sqlalchemy import Integer, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Task(Base):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        server_default=text("'pending'")
    )
