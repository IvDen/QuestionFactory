from fastapi import FastAPI, Depends
from aiohttp import ClientSession
from app import api


class AppContext:
    def __init__(self):
        self.appl = FastAPI()
        self.db = None
        self.client = None

    # TODO why async here broke the API
    def on_startup(self):
        self.appl.include_router(api.router)
        self.client = ClientSession()

    async def on_shutdown(self):
        await self.client.close()