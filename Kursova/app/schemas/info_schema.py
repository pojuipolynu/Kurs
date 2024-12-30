from pydantic import BaseModel
from typing import List

class AlbumBase(BaseModel):
    title: str
    artist_id: int

class Album(AlbumBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class AlbumList(BaseModel):
    albums: List[Album]

class ArtistBase(BaseModel):
    name: str
    imageUrl: str

class Artist(ArtistBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class ArtistList(BaseModel):
    artists: List[Artist]
