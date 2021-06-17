from fastapi import APIRouter
from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator

from app.core.config import settings
import pymysql

router = APIRouter()
test = settings.PROJECT_NAME

# for database
db_info = pymysql.connect(
    host=settings.DB_HOST,
    user=settings.DB_USER,
    passwd=settings.DB_PASSWORD,
    db=settings.DB_NAME,
    charset='utf8'
)

cursor = db_info.cursor(pymysql.cursors.DictCursor)


@router.get('/')
def ping():
    return { 'data': 'user route ping'}

@router.get("/users")
async def read_users():
    return [{"username": "Ricky"}, {"username": "Morty"}]

@router.get("/me")
async def read_user_me():
    print('test', test)
    return {"username": "fakecurrentuser"}

@router.get('/department')
async def get_department_list():
    query = 'select * from departments'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    return result    

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}    