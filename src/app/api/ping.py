from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/ping")
async def pong():
    return {"ping":"pong!"}