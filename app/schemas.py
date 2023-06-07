from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from uuid import UUID

class EmployeeBase(BaseModel):
    username: str
    password: str
    salary: Decimal
    promotion_date: datetime

class EmployeeDisplay(BaseModel):
    id: int
    username: str
    salary: Decimal
    promotion_date: datetime
    class Config():
        orm_mode = True

class TokenBase(BaseModel):
    token: UUID
    expiration_date: datetime
    employee_id: int

class TokenDisplay(BaseModel):
    token: UUID
    expiration_date: datetime
    class Config():
        orm_mode = True

class TokenGenerator(BaseModel):
    username: str
    password: str