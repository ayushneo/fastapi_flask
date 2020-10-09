import uvicorn
from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/student/", response_model=schemas.StudentInfo)
def create_student(student: schemas.StudentInfo, db: Session = Depends(get_db)):

    return crud.create_student(db=db,stud=student)

@app.get("/student/", response_model=List[schemas.StudentInfo])
def read_student(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    students = crud.get_student(db, skip=skip, limit=limit)
    return students

@app.delete("/student/{id}", response_model=schemas.StudentInfo)
def delete_student(id: int,db: Session = Depends(get_db)):
    del_stud = crud.del_student(id=id, db=db)
    return del_stud
