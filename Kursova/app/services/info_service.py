from db.models import Album, Artist
from schemas.info_schema import AlbumBase, ArtistBase
from repository.info_repository import ArtistRepository, AlbumRepository
from repository.favourite_repository import FavouriteRepository
from fastapi import HTTPException, status

class AlbumService:
    def __init__(self, album_repository: AlbumRepository):
        self.album_repository = album_repository
        self.fav_repo = FavouriteRepository

    async def get_albums(self):
        albums = await self.album_repository.get_all()
        return list(albums)
    
    async def get_album_songs(self, album_id:int):
        songs = await self.album_repository.get_album_songs(album_id)
        return list(songs)
    
    async def get_albums_by_name(self, title: str):
        albums = await self.album_repository.get_album_by_name(title)
        return list(albums)

    async def get_album_by_id(self, album_id: int):
        album = await self.album_repository.get_one(album_id)
        if album is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
        return album

    async def create_album(self, album_create: AlbumBase):
        if album_create is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data wasn`t given")
        db_album = Album(title=album_create.title, artist_id=album_create.artist_id)
        created_album = await self.album_repository.create(db_album)
        return created_album

    async def delete_album(self, album_id: int):
        album = await self.album_repository.get_one(album_id)
        if album is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
        await self.album_repository.delete(album)

    async def add_album_to_favourite(self, album_id: int, user_id:int):
        album = await self.album_repository.get_one(album_id)
        if album is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found") 
        songs = await self.get_album_songs(album_id)
        return songs


class ArtistService:
    def __init__(self, artist_repository: ArtistRepository):
        self.artist_repository = artist_repository

    async def get_artists(self):
        artists = await self.artist_repository.get_all()
        return list(artists)
    
    async def get_artist_songs(self, artist_id:int):
        songs = await self.artist_repository.get_artist_songs(artist_id)
        return list(songs)
    
    async def get_artist_albums(self, artist_id:int):
        albums = await self.artist_repository.get_artist_albums(artist_id)
        return list(albums)
    
    async def get_artists_by_name(self, name: str):
        artists = await self.artist_repository.get_artist_by_name(name)
        return list(artists)

    async def get_artist_by_id(self, artist_id: int):
        artist = await self.artist_repository.get_one(artist_id)
        if artist is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
        return artist

    async def create_artist(self, artist_create: ArtistBase):
        if artist_create is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data wasn`t given")
        db_artist = Artist(name=artist_create.name, imageUrl=artist_create.imageUrl)
        created_artist = await self.artist_repository.create(db_artist)
        return created_artist

    async def delete_artist(self, artist_id: int):
        artist = await self.artist_repository.get_one(artist_id)
        if artist is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
        await self.artist_repository.delete(artist)