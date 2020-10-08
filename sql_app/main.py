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
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_name(db, name=student.name)
    if db_student:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_student(db=db,s_name=student)


@app.get("/student/", response_model=List[schemas.StudentInfo])
def read_student(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students= crud.get_student(db, skip=skip, limit=limit)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)