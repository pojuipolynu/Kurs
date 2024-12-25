from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import postgres_db
from services.song_service import SongService
from repository.song_repository import SongRepository

from services.favourite_service import FavouriteService
from repository.favourite_repository import FavouriteRepository

from typing import Annotated

def get_song_service(db: Annotated[AsyncSession, Depends(postgres_db)]):
    song_repository = SongRepository(db)
    return SongService(song_repository)

def get_favourite_service(db: Annotated[AsyncSession, Depends(postgres_db)]):
    user_repository = FavouriteRepository(db)
    return FavouriteService(user_repository)