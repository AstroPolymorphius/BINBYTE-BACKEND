from typing import Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import String, Integer, Integer, DateTime

from src.models.base import UUIDModel, TimestampedModel


##Testimonial Model

class Testimonial(UUIDModel, TimestampedModel):
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    feedback: Mapped[str] = mapped_column(String, nullable=False)  
    rating: Mapped[int] = mapped_column(Integer, nullable=False)   
    fields_of_training: Mapped[str] = mapped_column(String, nullable=False)    
    date_of_testimonial:  Mapped[datetime] =mapped_column(DateTime,nullable=True, default=datetime.utcnow)     


