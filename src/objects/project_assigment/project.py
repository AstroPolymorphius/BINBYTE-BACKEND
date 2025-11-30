#  project member assignment model
class project_member() :
    # giving the table a name
    __tablename__ = "project_assigned"
    # defining relevant colums in the table
    member_id = Column(UUID(as_uuid=True),primary_key=True,index = True,defualt=uuid.uuid4)
    email = Column(String,unique=True,index = True,index=True,defualt=uuid.uuid4)
    project_id = Column(String,unique=True)
    description = Column(string,nullable=False)
    role = Column(String,nullable=False)
    tech_used = Column(String,nullable=False)
    start_date = Column(DateTime, defualt=datetime.now)
    end_date = Column(DateTime,nullable=False)
    
     
    
    
