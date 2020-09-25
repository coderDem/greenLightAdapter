from fastapi import APIRouter

from app.api.routers import rooms, users

api_router = APIRouter()

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

api_router.include_router(
    rooms.router,
    prefix="/rooms",
    tags=["rooms"],
    responses={404: {"description": "Not found"}},
)