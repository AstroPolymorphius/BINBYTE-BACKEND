from typing import Optional
from sqlalchemy import Column, Integer, String,Float
from src.models.base import UUIDModel,TimestampedModel
from uuid import UUID # for generating unique IDs(this is from python standard library)
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import  Mapped, mapped_column

class Member(UUIDModel,TimestampedModel):
    __tablename__ = 'Members'

    id = Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), primary_key=True)
    firstname =Mapped[str] = mapped_column(String, nullable=False)
    lastname =Mapped[str] = mapped_column(String, nullable=False)
    role =Mapped[str] = mapped_column(String, nullable=False)
    connections =Mapped[str] = mapped_column(String, nullable=False)
    experience =Mapped[int] = mapped_column(Integer, nullable=False)
    bio =Mapped[Optional[str]] = mapped_column(String, nullable=True)
    date_joined =Mapped[str] = mapped_column(String, nullable=False)
    