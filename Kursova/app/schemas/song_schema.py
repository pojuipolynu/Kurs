from pydantic import BaseModel
from typing import List

class SongBase(BaseModel):
    title: str
    artist_id: int
    fileUrl: str
    imageUrl: str
    duration: str
    album_id: int

class Song(SongBase):
    id: int
    album: str
    artist: str
    class Config:
        orm_mode = True
        from_attributes = True

class SongsList(BaseModel):
    songs: List[Song]

class SongDetail(BaseModel):
    song: Song