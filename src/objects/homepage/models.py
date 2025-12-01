from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
import uuid 
from sqlalchemy.dialects.postgresql import UUID

class Homepage(UUIDModel, TimestampedModel):
    __tablenames__ = "Homepages"
    carouselID: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    title:Mapped[str] 
    subtitle =Mapped[str]
