from sqlalchemy import String, Boolean, ForeignKey, Text, Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects import postgresql
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass

class BaseId(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Song(BaseId):
    __tablename__ = "songs"
    title = mapped_column(String, nullable=False)
    duration = mapped_column(String, nullable=False) 
    fileUrl = mapped_column(String, nullable=False)
    imageUrl = mapped_column(String, nullable=False)
    artist_id = mapped_column(Integer, ForeignKey("artists.id"), nullable=False)
    album_id = mapped_column(Integer, ForeignKey("albums.id"), nullable=False)

    album = relationship("Album")
    artist = relationship("Artist")
    favourites = relationship("Favourite", back_populates="song")
    lists = relationship("List", back_populates="song")

class Favourite(BaseId):
    __tablename__ = "favourites"
    song_id = mapped_column(Integer, ForeignKey("songs.id"), nullable=False)
    user_id = mapped_column(String, nullable=False) 

    song = relationship("Song", back_populates="favourites")


class Playlist(BaseId):
    __tablename__ = "playlists"
    title = mapped_column(String, nullable=False)
    user_id = mapped_column(String, nullable=False) 

    lists = relationship("List", back_populates="playlist")


class List(BaseId):
    __tablename__ = "lists"
    playlist_id = mapped_column(Integer, ForeignKey("playlists.id"), nullable=False)
    song_id = mapped_column(Integer, ForeignKey("songs.id"), nullable=False)

    playlist = relationship("Playlist")
    song = relationship("Song")

class Status(BaseId):
    __tablename__ = "statuses"
    user_id = mapped_column(String, nullable=False) 
    status = mapped_column(String, nullable=False) 

class Artist(BaseId):
    __tablename__ = "artists"
    name = mapped_column(String, nullable=False) 
    imageUrl = mapped_column(String, nullable=False)

    song = relationship("Song", back_populates="artist")
    album = relationship("Album", back_populates="artist")

class Album(BaseId):
    __tablename__ = "albums"
    title = mapped_column(String, nullable=False)
    artist_id = mapped_column(Integer, ForeignKey("artists.id"), nullable=False)

    artist = relationship("Artist")
    songs = relationship("Song", back_populates="album")
