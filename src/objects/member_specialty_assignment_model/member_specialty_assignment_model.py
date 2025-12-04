from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import Column, String

from src.models.base import UUIDModel

class MemberSpecialtyAssignment(UUIDModel):
    __tablename__ = "Member Specialty Assignments"
    
    MemberId = Mapped[str] = mapped_column(String, nullable = False)
    SpecialtyId = Mapped[str] = mapped_column(String, nullable = False)
