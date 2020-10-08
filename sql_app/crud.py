from sqlalchemy.orm import Session
from . import models, schemas


def get_student_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name)

def create_student(db: Session, s_name: schemas.StudentCreate):
    db_user = models.Student(name = s_name.name, s_class = s_name.s_class, marks = s_name.marks)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

