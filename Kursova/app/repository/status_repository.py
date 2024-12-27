from repository.base_repository import BaseRepository
from db.models import Status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class StatusRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Status)
    
    async def get_user_status(self, user_id: str):
        result = await self.db.execute(select(self.model).filter(self.model.user_id == user_id))
        variable = result.scalars().first()
        if variable is None:
            return
        return variable