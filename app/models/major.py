from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dbs.base import Base


class Major(Base):
    __tablename__ = "majors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    students = relationship("Student", back_populates="major", cascade="all, delete-orphan")