from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from uuid import UUID

from app.schemas import EmployeeBase, EmployeeDisplay
from app.db.database import get_db
from app.db import db_employee

router = APIRouter(
    prefix='/employee',
    tags=['employee']
)

@router.post('/', response_model=EmployeeDisplay, summary='Create a new employee')
def create_employee(request: EmployeeBase, db: Session = Depends(get_db)):
    """
    Creates a new employee, stores it in the DB and retrieves it.
    """
    return db_employee.create_employee(db, request)

@router.get('/{token}/', response_model=EmployeeDisplay, summary='Retrieve sensitive employee information')
def get_employee(token: UUID, db: Session = Depends(get_db)):
    """
    Authenticates the request by **token** and retrieves the employee's **salary** and **promotion date**.
    """
    return db_employee.get_employee(db, token)

@router.delete('/{username}/', summary='Delete an employee')
def delete_employee(username: str, password: str, db: Session = Depends(get_db)):
    """
    Deletes an employee from the database by **username**.
    """
    return db_employee.delete_employee(db, username, password)
