from repository.base_repository import BaseRepository
from db.models import Favourite, Song, Album, Artist
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class FavouriteRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Favourite)

    async def get_user_favourites(self, user_id: str):
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
                Artist.name.label("artist"))
            .join(self.model, Song.id == self.model.song_id)
            .join(Album, self.model.album_id == Album.id)
            .join(Artist, self.model.artist_id == Artist.id)
            .filter(self.model.user_id == user_id)
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
    
    async def get_favourite(self, user_id: str, song_id:int):
        song = await self.db.execute(select(self.model).filter(self.model.user_id == user_id, self.model.song_id == song_id))
        variable = song.scalars().first()
        if variable is None:
            return
        return variable

    