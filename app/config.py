from pydantic import BaseSettings, Field
from datetime import timedelta

db_user = '' # Postgres data base user
db_pass = '' # Postgres data base password
db_port = '' # Postgres data base port
db_name = '' # Postgres data base name

if not(db_user and db_pass and db_port and db_name):
    raise TypeError('Provide the db info!')

class Settings(BaseSettings):
    token_validity_period: timedelta = timedelta(
        days=7,
        hours=0,
        minutes=0,
        seconds=0
    )

class DockerSettings(Settings):
    db_url: str = Field(..., env='DATABASE_URL')
    endpoint: str = Field('http://0.0.0.0:8000')

class DefaultSettings(Settings):
    db_url: str = Field(f'postgresql+psycopg2://{db_user}:{db_pass}@{db_port}/{db_name}')
    endpoint: str = Field('http://127.0.0.1:8000')

try:
    settings = DockerSettings()
except:
    settings = DefaultSettings()