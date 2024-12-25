from repository.base_repository import BaseRepository
from db.models import Favourite, Song
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class FavouriteRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Favourite)

    async def get_user_favourites(self, user_id: int):
        query = (
            select(Song)
            .join(Favourite, Song.id == Favourite.song_id)
            .filter(Favourite.user_id == user_id)
        )
        songs = await self.db.execute(query)
        result = songs.scalars().all()
        return result
    
    async def get_favourite(self, user_id: int, song_id:int):
        song = await self.db.execute(select(self.model).filter(self.model.user_id == user_id, self.model.song_id == song_id))
        variable = song.scalars().first()
        if variable is None:
            return
        return variable

    