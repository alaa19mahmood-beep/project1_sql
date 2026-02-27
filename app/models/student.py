from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.dbs.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(100), nullable=False)

    major_id = Column(Integer, ForeignKey("majors.id"), nullable=False)
    major = relationship("Major", back_populates="students")

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())