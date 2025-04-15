from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.session import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="ativo")
    created_at = Column(DateTime, default=datetime.utcnow)
