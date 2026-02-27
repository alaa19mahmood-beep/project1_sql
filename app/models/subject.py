from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.dbs.base import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = mapped_column(Integer, primary_key=True)

    name = mapped_column(
        String(length=100),
        unique=True,
        index=True,
        nullable=False
    )

    major_id = mapped_column(
        ForeignKey("majors.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # العلاقة مع Major
    major: Mapped["Major"] = relationship(back_populates="subjects")

    # العلاقة مع Mark (واحد إلى متعدد)
    marks: Mapped[list["Mark"]] = relationship(
        back_populates="subject",
        cascade="all, delete-orphan"
    )