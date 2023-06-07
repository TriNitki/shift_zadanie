from sqlalchemy import Column, Integer, String, Numeric, DateTime, UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class DbEmployee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    salary = Column(Numeric)
    promotion_date = Column(DateTime)
    tokens = relationship("DbTokens", back_populates='employee')

class DbTokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(UUID(as_uuid=True), unique=True)
    expiration_date = Column(DateTime)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship("DbEmployee", back_populates='tokens')