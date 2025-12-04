from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
class ProjectMember(UUIDModel, TimestampedModel):
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    tech_used: Mapped[str] = mapped_column(String, nullable=False)
    
    
