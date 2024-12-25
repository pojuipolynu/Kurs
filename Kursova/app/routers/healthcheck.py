from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from db.session import postgres_db
from sqlalchemy import select

router = APIRouter(prefix="/healthcheck")

@router.get("/app", tags=["app"])
async def health_check():
    return {"result": "working"}


@router.get("/postgres", tags=["postgres"])
async def db_healthcheck(db: Annotated[AsyncSession, Depends(postgres_db)]) -> dict:
    try:
        await db.execute(select(1))
        return {"status": "working"}
    except Exception as e:
        return {"status": "not working", "status_code": 503}
    