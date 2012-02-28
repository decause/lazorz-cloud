from sqlalchemy import *
from sqlalchemy.orm import relation


class Tile(DeclarativeBase):
    """Tile Map Model"""

    __tablename__ = 'tile'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tile_type = Column(Integer)
    game_id = Column(Integer, ForeignKey('game.id'))
