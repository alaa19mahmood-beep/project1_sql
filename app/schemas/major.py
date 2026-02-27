from pydantic import BaseModel, ConfigDict


class MajorCreate(BaseModel):
    name: str


class MajorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str