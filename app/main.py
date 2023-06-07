from fastapi import FastAPI

from app.routers import employee, token
from app.db import models
from app.db.database import engine

app = FastAPI()
app.include_router(employee.router)
app.include_router(token.router)

@app.get('/')
def index():
    return {'detail': 'check docs'}

models.Base.metadata.create_all(engine)