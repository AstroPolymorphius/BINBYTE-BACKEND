from sqlalchemy.orm import Mapped, mapped_column 
from models.base import TimestampedModel, UUIDModel

class Tech(UUIDModel, TimestampedModel):
  TechUsed: Mapped[str]

  