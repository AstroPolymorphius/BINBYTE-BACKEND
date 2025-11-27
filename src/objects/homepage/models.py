from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import Base
import uuid 
from sqlalchemy.dialects.postgresql import UUID

class homepage(Base):
    __tablename__ = "Homepage"
    carouselID = Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    title = Column(String, nullable = False)
    subtitle = Column(String, nullable = False)
