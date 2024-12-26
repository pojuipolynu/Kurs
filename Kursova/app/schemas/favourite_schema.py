from pydantic import BaseModel
from typing import List

class FavouriteBase(BaseModel):
    user_id: str
    song_id: int