from fastapi import APIRouter, Depends, status
from schemas.song_schema import SongBase, SongsList, Song
from schemas.favourite_schema import FavouriteBase

from services.song_service import SongService
from services.favourite_service import FavouriteService

from utils.depends import get_song_service, get_favourite_service

router = APIRouter(prefix="/songs")

@router.get("/", response_model=SongsList, status_code=status.HTTP_200_OK)
async def get_songs(song_service: SongService = Depends(get_song_service)):
    songs = await song_service.get_songs()
    return SongsList(songs=songs)

@router.get("/{song_id}", response_model=Song, status_code=status.HTTP_200_OK)
async def get_song_by_id(song_id: int, song_service: SongService = Depends(get_song_service)):
    return await song_service.get_song_by_id(song_id)

@router.post("/", response_model=Song, status_code=status.HTTP_201_CREATED)
async def create_song(song_create: SongBase, song_service: SongService = Depends(get_song_service)):
    return await song_service.create_song(song_create)

@router.delete("/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_song(song_id: int, song_service: SongService = Depends(get_song_service)):
    await song_service.delete_song(song_id)
    return {"message": "User deleted successfully"}

@router.get("/search/{song_title}", response_model=SongsList, status_code=status.HTTP_200_OK)
async def get_song_by_name(song_title: str, song_service: SongService = Depends(get_song_service)):
    songs = await song_service.get_songs_by_name(song_title)
    return SongsList(songs=songs)




@router.post("/favourites", response_model=FavouriteBase, status_code=status.HTTP_201_CREATED)
async def add_favourite(song_add: FavouriteBase, favourite_service: FavouriteService = Depends(get_favourite_service)):
    return await favourite_service.add_favourites(song_add)

@router.get("/favourites/{user_id}", response_model=SongsList, status_code=status.HTTP_200_OK)
async def get_songs(user_id:int, favourite_service: FavouriteService = Depends(get_favourite_service)):
    songs = await favourite_service.get_favourites(user_id)
    return SongsList(songs=songs)

@router.delete("/favourites/{user_id}/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_favourite(user_id:int, song_id: int, favourite_service: FavouriteService = Depends(get_favourite_service)):
    await favourite_service.remove_favourites(song_id, user_id)
    return {"message": "Song removed successfully"}