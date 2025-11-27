from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import Base
import uuid 
from sqlalchemy.dialects.postgresql import UUID

class homepage(Base):
    