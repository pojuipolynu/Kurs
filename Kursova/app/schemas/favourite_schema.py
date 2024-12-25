from pydantic import BaseModel
from typing import List

class FavouriteBase(BaseModel):
    user_id: int
    song_id: int