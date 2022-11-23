from fastapi import APIRouter, FastAPI


def init_routers(app: FastAPI) -> None:
    routers: list[APIRouter] = []

    for router in routers:
        app.include_router(router)
