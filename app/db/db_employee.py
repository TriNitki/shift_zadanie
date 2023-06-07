from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from datetime import datetime
from uuid import UUID

from app.schemas import EmployeeBase
from app.db.models import DbEmployee, DbTokens
from app.db.hash import Hash

def create_employee(db: Session, request: EmployeeBase):
    new_employee = DbEmployee(
        username = request.username,
        password = Hash.bcrypt(request.password),
        salary = request.salary,
        promotion_date = request.promotion_date
    )
    
    same_username_employee = db.query(DbEmployee).filter(DbEmployee.username == new_employee.username).first()
    if same_username_employee:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Employee with this username already exists'
        )
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employee(db: Session, token: UUID):
    token = db.query(DbTokens).filter(DbTokens.token == token).first()
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'The token was not found'
        )
    
    if datetime.now() >= token.expiration_date:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail=f'The expiration date has already passed'
        )
    
    employee = db.query(DbEmployee).filter(DbEmployee.id == token.employee_id).first()
    return employee

def delete_employee(db: Session, username: str, password: str):
    employee = db.query(DbEmployee).filter(DbEmployee.username == username).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Employee with username {username} not found'
            )
    
    if not Hash.verify(employee.password, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Incorrect password'
            )
    
    db.delete(employee)
    db.commit()
    return 'ok'