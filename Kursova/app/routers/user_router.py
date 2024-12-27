from fastapi import APIRouter, Depends, status
from schemas.song_schema import SongsList
from schemas.user_schema import Status, Playlist, PlaylistList, PlaylistCreate, ListModel

from services.user_service import StatusService, PlaylistService

from utils.depends import get_playlist_service, get_status_service

router = APIRouter(prefix="/user")

# Статуси користувача
@router.get("/status/{user_id}", response_model=Status, status_code=status.HTTP_200_OK)
async def get_status(user_id:str, status_service: StatusService = Depends(get_status_service)):
    status = await status_service.get_status(user_id)
    return status

@router.patch("/status/{user_id}/change", status_code=status.HTTP_200_OK)
async def change_status(user_id:str, status_service: StatusService = Depends(get_status_service)):
    return await status_service.update_user_status(user_id)

@router.post("/status/{user_id}/set", status_code=status.HTTP_200_OK)
async def set_status(user_id:str, status_service: StatusService = Depends(get_status_service)):
    return await status_service.set_user_status(user_id)


# Плейлисти

@router.post("/create/playlist/{user_id}", response_model=Playlist, status_code=status.HTTP_201_CREATED)
async def create_playlist(user_id: str, playlist_create: PlaylistCreate, playlist_service: PlaylistService = Depends(get_playlist_service)):
    return await playlist_service.create_playlist(user_id, playlist_create)

@router.get("/playlists/{user_id}", response_model=PlaylistList, status_code=status.HTTP_200_OK)
async def get_playlists(user_id: str, playlist_service: PlaylistService = Depends(get_playlist_service)):
    playlists = await playlist_service.get_playlists(user_id)
    return PlaylistList(playlists=playlists)

@router.get("/playlists/{user_id}/{playlist_id}", response_model=Playlist, status_code=status.HTTP_200_OK)
async def get_one_playlist(playlist_id:int, playlist_service: PlaylistService = Depends(get_playlist_service)):
    playlist = await playlist_service.get_one_playlist(playlist_id)
    return playlist

@router.get("/playlist/{playlist_id}/songs", response_model=SongsList, status_code=status.HTTP_200_OK)
async def get_playlists_songs(playlist_id:int,  playlist_service: PlaylistService = Depends(get_playlist_service)):
    songs = await playlist_service.get_playlist_songs(playlist_id)
    return SongsList(songs=songs)

@router.post("/playlist/{playlist_id}/songs/{song_id}", response_model=ListModel, status_code=status.HTTP_201_CREATED)
async def add_song(playlist_id:int, song_id:int, playlist_service: PlaylistService = Depends(get_playlist_service)):
    return await playlist_service.add_song_to_playlist(playlist_id, song_id)

@router.delete("/playlist/{playlist_id}/songs/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_song(playlist_id:int, song_id:int, playlist_service: PlaylistService = Depends(get_playlist_service)):
    return await playlist_service.remove_song_from_playlist(playlist_id, song_id)


