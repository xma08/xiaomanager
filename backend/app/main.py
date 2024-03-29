import logging

import uvicorn
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.cards import cards_router
from app.api.api_v1.routers.rewards import rewards_router
from app.api.api_v1.routers.transactions import transactions_router
from app.api.api_v1.routers.users import users_router
from app.core import config
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from fastapi import Depends, FastAPI
from starlette.requests import Request

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")


# setup loggers
logging.config.fileConfig("app/logging.conf", disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
# This will get the root logger since no logger in the configuration has this name.


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    cards_router,
    prefix="/api/v1",
    tags=["cards"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    rewards_router,
    prefix="/api/v1",
    tags=["rewards"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    transactions_router,
    prefix="/api/v1",
    tags=["transactions"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
