import urllib.parse
import os
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from aiohttp import ClientSession
from app import api


class AppContext:
    def __init__(self):
        self.appl: FastAPI | None = None
        self.db: sessionmaker | None = None
        self.client: ClientSession | None = None

    # TODO why async here broke the API
    def on_startup(self):
        # TODO get dsn from file that will be in docker secrets
        self.appl = FastAPI()
        self.appl.include_router(api.router)

        db_dsn_str = ""
        dir_path = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(dir_path, 'secrets\\postgres_dsn')
        if os.path.exists(file_path):
            print(True)
            with open(file_path, 'r', encoding='utf-8') as dsn_file:
                db_dsn_str = dsn_file.readline()
        else:
            print('There is no dsn string at ../secrets/postgres_dsn')
            db_dsn_str = input('enter dsn string here:')

        parsing_dsn_result = urllib.parse.urlparse(db_dsn_str)
        username_raw = parsing_dsn_result.username
        password_raw = parsing_dsn_result.password

        username_safe = urllib.parse.quote_plus(username_raw)
        password_safe = urllib.parse.quote_plus(password_raw)

        parsing_dsn_result._replace(netloc=f'{username_safe}:{password_safe}@{parsing_dsn_result.hostname}:{parsing_dsn_result.port}')
        db_dsn_str_safe = urllib.parse.urlunparse(parsing_dsn_result)
        self.db = sessionmaker(create_engine(db_dsn_str_safe))

        self.client = ClientSession()

    async def on_shutdown(self):
        await self.db.close()
        await self.client.close()
