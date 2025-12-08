from typing import Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import String, Integer, Integer, DateTime
from src.models.base import UUIDModel, TimestampedModel


##ProjectTech Assignment Model

class ProjectTechAssignment(UUIDModel, TimestampedModel):
   
   pass 
    