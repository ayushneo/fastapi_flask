from pydantic import BaseModel

class StudentInfoBase(BaseModel):
    name: str
    s_class: str

class StudentCreate(StudentInfoBase):
    marks: int

class StudentInfo(StudentInfoBase):
    s_roll: int

    class Config:
        orm_mode = True

