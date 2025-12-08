from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import Column, String, Date
from datetime import date

from src.models.base import UUIDModel, TimestampedModel

#Defines the project model in the database
class Project(UUIDModel, TimestampedModel):
    projectname : Mapped[str] = mapped_column(String, nullable= False)
    category : Mapped[str] = mapped_column(String, nullable= False)
    status : Mapped[str] = mapped_column(String, nullable= False)
    completed : Mapped[date] = mapped_column(Date, nullable= True)
    duration : Mapped[str] = mapped_column(String, nullable= True)
    about : Mapped[str] = mapped_column(String, nullable= True)
    githubURL : Mapped[str] = mapped_column(String, unique = True, nullable= True)
    websiteURL : Mapped[str] = mapped_column(String, nullable= True)
