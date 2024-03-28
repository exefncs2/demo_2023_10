from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base  # 假设你的 database.py 文件中定义了 Base

class Vector(Base):
    __tablename__ = "vectors"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String, index=True)
    value: Mapped[float] = mapped_column(Float, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer, index=True, nullable=True)

