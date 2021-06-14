from fastapi import APIRouter
from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator

from app.core.config import settings


router = APIRouter()
test = settings.PROJECT_NAME

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

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}