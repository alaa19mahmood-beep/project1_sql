from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import ConfigDict


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    phone: PhoneNumber
    major_id: int


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    age: int
    phone: str
    major_id: int