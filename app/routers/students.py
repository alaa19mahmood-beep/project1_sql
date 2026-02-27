from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dbs.deps import get_db
from app.models import Student, Major
from app.schemas.student import StudentCreate, StudentRead

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    major = db.get(Major, payload.major_id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")

    student = Student(
        name=payload.name,
        email=str(payload.email),
        age=payload.age,
        phone=str(payload.phone),
        major_id=payload.major_id,
    )

    db.add(student)
    db.commit()
    db.refresh(student)
    return student