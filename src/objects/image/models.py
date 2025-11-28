from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import Base
import uuid 
from sqlalchemy.dialects.postgresql import UUID

class Images(Base):
    __tablenames__ = "Images"
    imageID = Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    URL = Column(String, nullable = False)
    alttext= Column(String, nullable = True)
    