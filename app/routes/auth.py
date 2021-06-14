from fastapi import APIRouter, Response, Request, Cookie, Header
from typing import Optional
from app.core.config import settings
import json
from pydantic import BaseModel
from app.auth.auth_handler import token_response, signJWT, decodeJWT

class Item(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    token: str

router = APIRouter()


@router.post('/')
# async def read_items(item: Optional[str] = Cookie(None)):
# async def read_items(request: Request):
async def read_items(cookie: Optional[str] = Header(None)):
    # print(request.headers)
    print(cookie)
    # print('this is cookie', item)
    return { 'data' : 'auth route ping'}

# header ref: user_agent: Optional[str] = Header(None)

@router.post('/login')
async def master_login(item: Item, response: Response):
    print('this is item: ', item)
    email = item.email
    password = item.password
    print('this is item email: ', email)

    master_email = settings.MASTER_EMAIL
    master_password = settings.MASTER_PASSWORD

    if email == master_email and password == master_password:
        # create a token
        access_token = signJWT(master_email)
        print(access_token)

        # set token into cookies
        response.set_cookie(key="ACCESS_TOKEN", value=access_token, httponly=True)
        return { 'message' : 'do you like cookies?'}
    else:
        return False

@router.post('/decode')
# async def decode_access_token(item: Token):
async def decode_access_token():
    # print('hello')
    print('this is item: ', item)
    token = item.token
    print('this is token: ', token)
    decoded = decodeJWT(token)
    return decoded