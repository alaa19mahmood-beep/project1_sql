from pydantic import BaseModel


class SubjectCreate(BaseModel):
    name: str
    major_id: int


class SubjectOut(BaseModel):
    subject_id: int
    name: str
    major_id: int

    class Config:
        from_attributes = True