from repository.base_repository import BaseRepository
from db.models import Song, Album, Artist
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class SongRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Song)

from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

class SongRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Song)

    async def get_song_by_name(self, title: str):
        query = (
            select(
                Song.id,
                Song.title,
                Song.artist_id,
                Song.fileUrl,
                Song.imageUrl,
                Song.duration,
                Song.album_id,
                Album.title.label("album"),
                Artist.name.label("artist")
            )
            .join(Album, Song.album_id == Album.id)
            .join(Artist, Song.artist_id == Artist.id)
            .filter(Song.title.ilike(f"%{title}%"))
        )

        result = await self.db.execute(query)
        songs = result.mappings().all()  

        return [
            {
                "id": song["id"],
                "title": song["title"],
                "artist_id": song["artist_id"],
                "fileUrl": song["fileUrl"],
                "imageUrl": song["imageUrl"],
                "duration": song["duration"],
                "album_id": song["album_id"],
                "album": song["album"],
                "artist": song["artist"],
            }
            for song in songs
        ]

  

