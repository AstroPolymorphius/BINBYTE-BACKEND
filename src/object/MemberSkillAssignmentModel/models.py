from sqlalchemy import Column,String,Integer,Float, DateTimE
from sqlalchemy.dialects.postgresql import UUID 
from datetime import datetime 
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column 
from models.base import UUIDModel, TimestampedModel

#Member skill model 
class Member_skill_assignment_model(UUIDModel, TimestampedModel):

  skill:Mapped[String] = mapped_column(nullable = False)
  
  
    UUID(as_uuid = True),
    nullable = False, 
    default = uuid.uuid4
  )
