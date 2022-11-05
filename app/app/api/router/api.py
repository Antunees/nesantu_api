from app.api.router.endpoints import (devices, devices_manager, login, users_admin_manager,
                                      organization, subscription, users,
                                      users_manager, users_subscriptions,
                                      users_subscriptions_manager)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, prefix="", tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])


