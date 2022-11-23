from fastapi import FastAPI

from app.middlewares import init_middlewares
from app.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPI Base',
        description='FastAPI Base Project',
        version='0.1.0',
    )

    init_routers(app)
    init_middlewares(app)

    return app


app = create_app()
