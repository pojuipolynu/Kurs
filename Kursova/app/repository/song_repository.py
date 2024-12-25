from repository.base_repository import BaseRepository
from db.models import Song
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class SongRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Song)

    async def get_song_by_name(self, title: str):
        songs = await self.db.execute(select(self.model).filter(self.model.title.ilike(f"%{title}%")))
        variable = songs.scalars().all()
        return variable