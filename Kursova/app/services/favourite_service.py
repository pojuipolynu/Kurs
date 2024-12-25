from db.models import Favourite
from schemas.favourite_schema import FavouriteBase
from repository.favourite_repository import FavouriteRepository
from fastapi import HTTPException, status

class FavouriteService:
    def __init__(self, favourite_repository: FavouriteRepository):
        self.favourite_repository = favourite_repository

    async def get_favourites(self, user_id: int):
        favourites = await self.favourite_repository.get_user_favourites(user_id)
        return list(favourites)

    async def add_favourites(self, favourite_add: FavouriteBase):
        if favourite_add is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data wasn`t given")
        db_favourite = Favourite(user_id=favourite_add.user_id, song_id=favourite_add.song_id)
        added_favourite = await self.favourite_repository.create(db_favourite)
        return added_favourite

    async def remove_favourites(self, favourite_id: int, user_id: int):
        favourite = await self.favourite_repository.get_favourite(favourite_id, user_id)
        if favourite is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
        await self.favourite_repository.delete(favourite)