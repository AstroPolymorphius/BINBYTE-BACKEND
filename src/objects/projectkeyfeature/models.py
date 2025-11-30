from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import Base
import uuid 
from sqlalchemy.dialects.postgresql import UUID

class ProjectKeyFeatures(Base):
    __tablenames__ = "Product key features"
    keyfeaturesID = Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    keyfeature= Column(String, nullable = False)
    projectID =  Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4) #(FK)
