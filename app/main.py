from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.Example import router as example_router

from app.settings import Settings
from app.db.database import db

class App:
    def __init__(self):
        self.app = FastAPI()

    def include_routers(self, app: FastAPI):
        app.include_router(example_router, prefix="/example", tags=["example"])

    def create_app(self) -> FastAPI:
        settings = Settings()
        app = FastAPI(
            title=settings.service_name,
            version=settings.service_version,
            debug=settings.debug,
        )

        origins = ["*"]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        db.create_as_engine()
        db.create_as_session_maker()

        @app.on_event("shutdown")
        async def shutdown() -> None:
            await db.close_as_engine()

        self.include_routers(app)
        return app


    app = create_app()
