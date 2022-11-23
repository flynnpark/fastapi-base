from fastapi import FastAPI


def init_middlewares(app: FastAPI) -> None:
    middlewares = []

    for middleware in middlewares:
        app.add_middleware(middleware)
