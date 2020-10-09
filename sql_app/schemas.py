from pydantic import BaseModel

class StudentInfoBase(BaseModel):
    name: str
    s_class: str
    marks: int

class StudentInfo(StudentInfoBase):
    s_roll: int

    class Config:
        orm_mode = True

