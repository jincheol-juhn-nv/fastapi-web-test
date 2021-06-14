import time
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.api import router as api_router #routing

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router((api_router))

    return _app

app = get_application()

router = APIRouter()

#connection test
@app.get('/')
def ping():
    return { 'data': 'connection ok' }

#middleware test
@app.middleware('http')
async def middleware_test(request: Request, call_next):
    start_time = time.time()
    print('start time', start_time)
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response




#structure reference: https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/main.py