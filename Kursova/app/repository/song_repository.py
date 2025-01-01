from repository.base_repository import BaseRepository
from db.models import Song, Album, Artist
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class SongRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Song)

    async def get_song_by_name(self, title: str):
        query = (
            select(
                self.model.id,
                self.model.title,
                self.model.artist_id,
                self.model.fileUrl,
                self.model.imageUrl,
                self.model.duration,
                self.model.album_id,
                Album.title.label("album"),
                Artist.name.label("artist")
            )
            .join(Album, self.model.album_id == Album.id)
            .join(Artist, self.model.artist_id == Artist.id)
            .filter(self.model.title.ilike(f"%{title}%"))
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
    
    async def get_all_songs(self):
        query = (
            select(
                self.model.id,
                self.model.title,
                self.model.artist_id,
                self.model.fileUrl,
                self.model.imageUrl,
                self.model.duration,
                self.model.album_id,
                Album.title.label("album"),
                Artist.name.label("artist")
            )
            .join(Album, self.model.album_id == Album.id)
            .join(Artist, self.model.artist_id == Artist.id)
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
    
    async def get_one_song(self, id):
        query = (
            select(
                self.model.id,
                self.model.title,
                self.model.artist_id,
                self.model.fileUrl,
                self.model.imageUrl,
                self.model.duration,
                self.model.album_id,
                Album.title.label("album"),
                Artist.name.label("artist")
            )
            .join(Album, self.model.album_id == Album.id)
            .join(Artist, self.model.artist_id == Artist.id)
            .filter(self.model.id == id)
        )
        
        result = await self.db.execute(query)
        variable = result.first()  
        if variable is None:
            return None

        return {
            "id": variable.id,
            "title": variable.title,
            "artist_id": variable.artist_id,
            "fileUrl": variable.fileUrl,
            "imageUrl": variable.imageUrl,
            "duration": variable.duration,
            "album_id": variable.album_id,
            "album": variable.album,
            "artist": variable.artist,
        }
