from sqlalchemy.orm import Session
from . import models, schemas


def get_student_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name)

def create_student(db: Session, stud: schemas.StudentCreate):
    db_user = models.Student(name = stud.name, s_class = stud.s_class, marks = stud.marks)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_student(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()
