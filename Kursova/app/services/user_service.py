from db.models import Status, Playlist, List
from schemas.user_schema import StatusUpdate, PlaylistCreate
from repository.status_repository import StatusRepository
from repository.playlist_repository import PlaylistRepository
from fastapi import HTTPException, status
from pydantic import parse_obj_as


class StatusService:
    def __init__(self, status_repository: StatusRepository):
        self.status_repository = status_repository

    async def get_status(self, user_id: str):
        status = await self.status_repository.get_user_status(user_id)
        if status is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Something gone wrong")
        return status
    
    async def set_user_status(self, user_id: str):
        status = await self.status_repository.get_user_status(user_id)
        if status is None:
            user_status = Status(user_id=user_id, status="FREE")
            created_status = await self.status_repository.create(user_status)
            return created_status
        return status
    
    async def update_user_status(self, user_id: str):
        status = await self.status_repository.get_user_status(user_id)
        if status is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Something gone wrong")
        if status.status == "FREE":
            await self.status_repository.update(status, StatusUpdate(**{"status": "PAID"}))
        else:
            await self.status_repository.update(status, StatusUpdate(**{"status": "FREE"}))
        return
    
class PlaylistService:
    def __init__(self, playlist_repository: PlaylistRepository):
        self.playlist_repository = playlist_repository

    async def get_playlists(self, user_id: str):
        playlists = await self.playlist_repository.get_user_playlists(user_id)
        return parse_obj_as(List[Playlist], playlists)
    
    async def get_one_playlist(self, playlist_id:int):
        playlist = await self.playlist_repository.get_one(playlist_id)
        if playlist is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
        return playlist
    
    async def get_playlist_songs(self, playlist_id:int):
        songs = await self.playlist_repository.get_playlist_songs(playlist_id)
        return list(songs)
    
    async def create_playlist(self, user_id:str, playlist_create:PlaylistCreate):
        if playlist_create is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data wasn`t given")
        db_playlist = Playlist(title=playlist_create.title, user_id=user_id)
        created_playlist = await self.playlist_repository.create(db_playlist)
        return created_playlist

    async def delete_playlist(self, playlist_id: int):
        playlist = await self.playlist_repository.get_one(playlist_id)
        if playlist is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
        await self.playlist_repository.delete(playlist)

    async def add_song_to_playlist(self, playlist_id:int, song_id:int):
        song_to_add= List(playlist_id=playlist_id, song_id=song_id)
        added_song = await self.playlist_repository.add_song(song_to_add)
        return added_song
    
    async def remove_song_from_playlist(self, playlist_id:int, song_id:int):
        song = await self.playlist_repository.get_one_song(song_id, playlist_id)
        if song is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
        await self.playlist_repository.delete(song)
