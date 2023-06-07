import requests
from fastapi import status
from sqlalchemy import create_engine

from app.schemas import EmployeeBase, TokenGenerator
from app.config import settings

ENDPOINT = settings.endpoint
DB_URL = settings.db_url

# Basic employee model for testing
basic_employee = EmployeeBase(
    username='for_test_purposes',
    password='1234',
    salary=1000,
    promotion_date='2024-01-01 00:00:00'
)

# Basic token generation model for testing
token_gen = TokenGenerator(
    username=basic_employee.username,
    password=basic_employee.password
)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == status.HTTP_200_OK

def test_can_create_employee():
    payload = basic_employee
    
    # Tests the creation of a new employee
    response = requests.post(ENDPOINT + "/employee", data=payload.json())
    assert response.status_code == status.HTTP_200_OK
    
    delete_user(payload.username, payload.password)

def test_can_generate_token():
    emp_payload = basic_employee
    requests.post(ENDPOINT + "/employee", data=emp_payload.json())
    
    # Tests the generation of a new token
    token_payload = token_gen
    gen_token_request = requests.post(ENDPOINT + "/employee/token", data=token_payload.json())
    assert gen_token_request.status_code == status.HTTP_200_OK
    
    token = gen_token_request.json()['token']
    
    # Tests receipt of sensitive employee information by token
    get_emp_request = requests.get(ENDPOINT + f"/employee/{token}")
    assert get_emp_request.status_code == status.HTTP_200_OK
    
    delete_user(emp_payload.username, emp_payload.password)
    delete_token(token)

def delete_user(username: str, password: str):
    return requests.delete(ENDPOINT + f"/employee/{username}", params={'password': password})

def delete_token(token: str):
    return requests.delete(ENDPOINT + "/employee/token", params={'token': token})