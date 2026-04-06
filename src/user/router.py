from fastapi import APIRouter

user_routes = APIRouter(prefix = "/user")

@user_routes.post("")