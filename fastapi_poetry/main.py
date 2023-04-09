"""
    Main
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Status(BaseModel):
    """ Status class """
    status: str = 'ok'


@app.get('/status')
async def status():
    """ Status endpoint """
    return Status()
