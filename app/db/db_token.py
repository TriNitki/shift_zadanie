from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from uuid import uuid4
from datetime import datetime
from uuid import UUID

from app.schemas import TokenGenerator
from app.db.models import DbEmployee, DbTokens
from app.db.hash import Hash
from app.config import settings

def generate_token(db: Session, request: TokenGenerator):
    employee = db.query(DbEmployee).filter(DbEmployee.username == request.username).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Employee with username {request.username} not found'
            )
    
    if not Hash.verify(employee.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Incorrect password'
            )
    
    new_token = DbTokens(
        token = uuid4(),
        expiration_date = datetime.now() + settings.token_validity_period,
        employee_id = employee.id
    )
    
    db.add(new_token)
    db.commit()
    db.refresh(new_token)
    return new_token

def delete_token(db: Session, token: UUID):
    token = db.query(DbTokens).filter(DbTokens.token == token).first()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='The token was not found '
        )
    
    db.delete(token)
    db.commit()
    return 'ok'