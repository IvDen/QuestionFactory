from app.utils.dsn_validation import get_valid_dsn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from aiohttp import ClientSession
from app import api


class AppContext:
    def __init__(self):
        self.appl: FastAPI = FastAPI()
        #TODO for bind at models.metadata.create_all need a engine instance not only session
        self.engine_db: Engine | None = None
        self.session_maker_db: sessionmaker | None = None
        self.client: ClientSession | None = None

    def __call__(self, *args, **kwargs):
        print('call context instance')
        return self

    async def on_startup(self):
        print('On startup')
        # TODO get dsn from file that will be in docker secrets
        self.appl.include_router(api.router)
        db_dsn_valid = get_valid_dsn()
        self.engine_db = create_engine(db_dsn_valid, execution_options={"isolation_level": "REPEATABLE READ"})
        self.session_maker_db = sessionmaker(self.engine_db, autoflush=False, expire_on_commit=False)
        self.client = ClientSession()

    async def on_shutdown(self):
        print('On shutdown')
        self.engine_db.dispose()
        await self.client.close()
