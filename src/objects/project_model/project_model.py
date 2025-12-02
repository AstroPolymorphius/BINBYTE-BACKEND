#Importing the base model and uuid for the primary key
from sqlalchemy import Column, String
from database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

#Defines the project model in the database
class Project(Base):
    __tablename__ = "projects"

    projectID = Column(UUID(as_uuid = True), primary_key = True, index = True, default = uuid.uuid4, nullable= False)
    projectname = Column(String, index = True, nullable= False)
    category = Column(String, index = True, nullable= False)
    status = Column(String, index = True, nullable= False)
    completed = Column(String, nullable= True)
    duration = Column(String, nullable= True)
    about = Column(String, nullable= True)
    githubURL = Column(String, index = True, unique = True, nullable= True)
    websiteURL = Column(String, index = True, nullable= True)
