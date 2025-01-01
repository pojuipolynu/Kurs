from fastapi import APIRouter, Depends, status

from schemas.song_schema import SongsList
from schemas.info_schema import Artist, Album, AlbumList, ArtistList, ArtistBase, AlbumBase

from services.info_service import AlbumService, ArtistService

from utils.depends import get_artist_service, get_album_service

router = APIRouter(prefix="/other")

# Альбоми
@router.get("/albums", response_model=AlbumList, status_code=status.HTTP_200_OK)
async def get_albums(album_service: AlbumService = Depends(get_album_service)):
    albums = await album_service.get_albums()
    return AlbumList(albums=albums)

@router.post("/albums", response_model=Album, status_code=status.HTTP_201_CREATED)
async def create_album(album_create:AlbumBase, album_service: AlbumService = Depends(get_album_service)):
    return await album_service.create_album(album_create)

@router.get("/albums/songs/{album_id}", status_code=status.HTTP_200_OK)
async def get_album_songs(album_id:int, album_service: AlbumService = Depends(get_album_service)):
    songs = await album_service.get_album_songs(album_id)
    return SongsList(songs=songs)

@router.delete("/albums/search/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id:int, album_service: AlbumService = Depends(get_album_service)):
    return await album_service.delete_album(album_id)

@router.get("/albums/search/{album_id}", response_model=Album, status_code=status.HTTP_200_OK)
async def get_album_by_id(album_id: int, album_service: AlbumService = Depends(get_album_service)):
    album = await album_service.get_album_by_id(album_id)
    return album

@router.get("/albums/search_name/{title}", response_model=AlbumList, status_code=status.HTTP_200_OK)
async def get_albums_by_name(title:str, album_service: AlbumService = Depends(get_album_service)):
    albums = await album_service.get_albums_by_name(title)
    return AlbumList(albums=albums)



# Виконавці
@router.get("/artists", response_model=ArtistList, status_code=status.HTTP_200_OK)
async def get_artists(artist_service: ArtistService = Depends(get_artist_service)):
    artists = await artist_service.get_artists()
    return ArtistList(artists=artists)

@router.post("/artists", response_model=Artist, status_code=status.HTTP_201_CREATED)
async def create_artist(artist_create:ArtistBase, artist_service: ArtistService = Depends(get_artist_service)):
    return await artist_service.create_artist(artist_create)

@router.get("/artists/songs/{artist_id}", status_code=status.HTTP_200_OK)
async def get_artist_songs(artist_id:int, artist_service: ArtistService = Depends(get_artist_service)):
    songs = await artist_service.get_artist_songs(artist_id)
    return SongsList(songs=songs)

@router.get("/artists/albums/{artist_id}", response_model=AlbumList, status_code=status.HTTP_200_OK)
async def get_artist_albums(artist_id:int, artist_service: ArtistService = Depends(get_artist_service)):
    albums = await artist_service.get_artist_albums(artist_id)
    return AlbumList(albums=albums)

@router.delete("/artists/search/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_artist(artist_id:int, artist_service: ArtistService = Depends(get_artist_service)):
    return await artist_service.delete_artist(artist_id)

@router.get("/artists/search/{artist_id}", response_model=Artist, status_code=status.HTTP_200_OK)
async def get_artist_by_id(artist_id: int, artist_service: ArtistService = Depends(get_artist_service)):
    artist = await artist_service.get_artist_by_id(artist_id)
    return artist

@router.get("/artists/search_name/{name}", response_model=ArtistList, status_code=status.HTTP_200_OK)
async def get_artists_by_name(name:str, artist_service: ArtistService = Depends(get_artist_service)):
    artists = await artist_service.get_artists_by_name(name)
    return ArtistList(artists=artists)


