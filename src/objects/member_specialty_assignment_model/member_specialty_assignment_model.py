from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import Column, String

from src.models.base import UUIDModel

#Defines the member specialty assignment class
class MemberSpecialtyAssignment(UUIDModel):
    pass
