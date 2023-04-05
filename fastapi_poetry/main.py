"""
    Main
"""
from fastapi import FastAPI
from pydantic import BaseModel
# from .settings import settings

app = FastAPI()


class Status(BaseModel):
    """ Status class """
    status: str = 'ok'


@app.get('/status')
async def status():
    """ Status endpoint """
    return Status()
