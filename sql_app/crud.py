from sqlalchemy.orm import Session
from . import models, schemas




def create_student(db: Session, stud: schemas.StudentInfo):
    db_user = models.Student(name = stud.name, s_class = stud.s_class, marks = stud.marks)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_student(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def del_student(db: Session, id: int):
    student = db.query(models.Student).filter(models.Student.s_roll == id).first()
    db.delete(student)
    db.commit()
