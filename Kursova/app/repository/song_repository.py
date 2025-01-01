from repository.base_repository import BaseRepository
from db.models import Song, Album, Artist
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class SongRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Song)

    async def get_song_by_name(self, title: str):
        # songs = await self.db.execute(select(self.model).filter(self.model.title.ilike(f"%{title}%")))
        # variable = songs.scalars().all()
        query = (
            select(
                self.model.id,
                Album.title.label("album"),
                Artist.name.label("artist")
            )
            .join(Album, Song.album_id == Album.id)
            .join(Artist, Song.artist_id == Artist.id)
            .filter(Song.title.ilike(f"%{title}%"))
        )

        result = await self.db.execute(query)
        return result.scalars().all()
  

