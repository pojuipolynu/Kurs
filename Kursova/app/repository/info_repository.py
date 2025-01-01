from repository.base_repository import BaseRepository
from db.models import Album, Artist, Song
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class AlbumRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Album)
        self.song = Song

    async def get_album_songs(self, album_id: int):
        result = await self.db.execute(
            select(self.song.id,
                self.song.title,
                self.song.artist_id,
                self.song.fileUrl,
                self.song.imageUrl,
                self.song.duration,
                self.song.album_id,
                Album.title.label("album"),
                Artist.name.label("artist"))
            .join(Album, self.song.album_id == Album.id)
            .join(Artist, self.song.artist_id == Artist.id).filter(self.song.album_id == album_id)
        )
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
    
    async def get_album_by_name(self, title: str):
        albums = await self.db.execute(select(self.model).filter(self.model.title.ilike(f"%{title}%")))
        variable = albums.scalars().all()
        return variable


class ArtistRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Artist)
        self.song = Song
        self.album = Album

    async def get_artist_songs(self, artist_id: int):
        result = await self.db.execute(
            select(self.song.id,
                self.song.title,
                self.song.artist_id,
                self.song.fileUrl,
                self.song.imageUrl,
                self.song.duration,
                self.song.album_id,
                Album.title.label("album"),
                Artist.name.label("artist"))
            .join(Album, self.song.album_id == Album.id)
            .join(Artist, self.song.artist_id == Artist.id)
            .filter(self.song.artist_id == artist_id)
        )
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
    
    async def get_artist_albums(self, artist_id: int):
        result = await self.db.execute(
            select(self.album).filter(self.album.artist_id == artist_id)
        )
        albums = result.scalars().all()
        return albums
    
    async def get_artist_by_name(self, name: str):
        artists = await self.db.execute(select(self.model).filter(self.model.name.ilike(f"%{name}%")))
        variable = artists.scalars().all()
        return variable