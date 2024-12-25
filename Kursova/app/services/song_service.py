from db.models import Song
from schemas.song_schema import SongBase
from repository.song_repository import SongRepository
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

class SongService:
    def __init__(self, song_repository: SongRepository):
        self.song_repository = song_repository

    async def get_songs(self):
        songs = await self.song_repository.get_all()
        return list(songs)
    
    async def get_songs_by_name(self, title: str):
        songs = await self.song_repository.get_song_by_name(title)
        return list(songs)

    async def get_song_by_id(self, song_id: int):
        song = await self.song_repository.get_one(song_id)
        if song is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
        return song

    async def create_song(self, song_create: SongBase):
        if song_create is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data wasn`t given")
        db_song = Song(title=song_create.title, artist=song_create.artist, fileUrl=song_create.fileUrl, imageUrl=song_create.imageUrl, duration=song_create.duration)
        created_song = await self.song_repository.create(db_song)
        return created_song

    async def delete_song(self, song_id: int):
        song = await self.song_repository.get_one(song_id)
        if song is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
        await self.song_repository.delete(song)