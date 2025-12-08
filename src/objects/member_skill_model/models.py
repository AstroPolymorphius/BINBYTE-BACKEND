from sqlalchemy.orm import Mapped, mapped_column 
from models.base import TimestampedModel, UUIDModel 

class member_skill_assignment_model(UUIDModel, TimestampedModel):
  skill:Mapped[str] = mapped_column(nullable = False)