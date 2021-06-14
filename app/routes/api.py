from fastapi import APIRouter, Depends

from app.routes import auth, user

from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

router = APIRouter()
router.include_router(auth.router, tags=['auth'], prefix='/auth')
router.include_router(user.router, tags=['user'], prefix='/user', dependencies=[Depends(JWTBearer())])