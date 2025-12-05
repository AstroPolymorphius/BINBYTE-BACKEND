
from sqlalchemy import Column, Integer, String,Float
from src.models.base import UUIDModel,TimestampedModel
from uuid import UUID # for generating unique IDs(this is from python standard library)
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import  Mapped, mapped_column

class Member(UUIDModel,TimestampedModel):
    firstname =Mapped[str] = mapped_column(String, nullable=False)
    lastname =Mapped[str] = mapped_column(String, nullable=False)
    role =Mapped[str] = mapped_column(String, nullable=False)
    connections =Mapped[str] = mapped_column(String, nullable=False)
    experience =Mapped[int] = mapped_column(Integer, nullable=False)
    bio =Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    