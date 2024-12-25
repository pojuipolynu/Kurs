from pydantic import BaseModel
from typing import List

class SongBase(BaseModel):
    title: str
    artist: str
    fileUrl: str
    imageUrl: str
    duration: str

class Song(SongBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class SongsList(BaseModel):
    songs: List[Song]

class SongDetail(BaseModel):
    song: Song