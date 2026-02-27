from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.dbs.deps import get_db
from app.models.major import Major
from app.schemas.major import MajorCreate, MajorOut

router = APIRouter(prefix="/majors", tags=["majors"])


@router.post("/", response_model=MajorOut, status_code=status.HTTP_201_CREATED)
def create_major(payload: MajorCreate, db: Session = Depends(get_db)):
    major = Major(name=payload.name)
    db.add(major)

    try:
        db.commit()
        db.refresh(major)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Major already exists",
        )

    return major


@router.get("/", response_model=list[MajorOut])
def get_majors(db: Session = Depends(get_db)):
    return db.query(Major).all()


@router.get("/{major_id}", response_model=MajorOut)
def get_major(major_id: int, db: Session = Depends(get_db)):
    major = db.get(Major, major_id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")
    return major


@router.delete("/{major_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_major(major_id: int, db: Session = Depends(get_db)):
    major = db.get(Major, major_id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")

    db.delete(major)
    db.commit()