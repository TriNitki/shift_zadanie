from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from uuid import UUID

from app.schemas import TokenGenerator, TokenDisplay
from app.db.database import get_db
from app.db import db_token

router = APIRouter(
    prefix='/employee/token',
    tags=['token']
)

@router.post('/', response_model=TokenDisplay, summary='Generate a new token')
def generate_token(request: TokenGenerator, db: Session = Depends(get_db)):
    """
    Generates a new authentication **token** by **username** and **password** and retrives it.
    """
    return db_token.generate_token(db, request)

@router.delete('/{token}/', summary='Delete a token')
def delete_token(token: UUID, db: Session = Depends(get_db)):
    """
    Deletes an token from the database by **token**.
    """
    return db_token.delete_token(db, token)