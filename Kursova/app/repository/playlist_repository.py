from repository.base_repository import BaseRepository
from db.models import Playlist, List, Song
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, join
from sqlalchemy.orm import joinedload


class PlaylistRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=Playlist)
        self.list = List
        self.song = Song

    async def get_playlist_songs(self, playlist_id: int):
        stmt = (
            select(self.song)
            .join(self.list, self.song.id == self.list.song_id)
            .join(self.model, self.list.playlist_id == self.model.id)
            .filter(self.model.id == playlist_id)
        )
        result = await self.db.execute(stmt)
        songs = result.scalars().all()
        return songs
    
    async def get_user_playlists(self, user_id: str):
        result = await self.db.execute(select(self.model).filter(self.model.user_id == user_id))
        playlists = result.scalars().all()
        return playlists
    
    async def add_song(self, song_add):
        self.db.add(song_add)
        await self.db.commit()
        await self.db.refresh(song_add)
        return song_add
    
    async def get_one_song(self, song_id:int, playlist_id:int):
        result = await self.db.execute(select(self.list).filter(self.list.song_id == song_id, self.list.playlist_id == playlist_id))
        song = result.scalars().first()
        if song is None:
            return
        return song
    
