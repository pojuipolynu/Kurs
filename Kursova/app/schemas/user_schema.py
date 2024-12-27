from pydantic import BaseModel
from typing import List

class StatusUpdate(BaseModel):
    status: str

class Status(StatusUpdate):
    user_id:str  

class PlaylistCreate(BaseModel):
    title: str

class Playlist(PlaylistCreate):
    user_id: str

class PlaylistList(BaseModel):
    playlists: List[Playlist]

class ListModel(BaseModel):
    playlist_id: int
    song_id: int