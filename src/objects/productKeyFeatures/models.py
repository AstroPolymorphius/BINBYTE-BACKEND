from typing import Optional
from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column


class ProjectKeyFeatures(UUIDModel, TimestampedModel):
    keyfeature: Mapped[str] = mapped_column(String, nullable=False)


