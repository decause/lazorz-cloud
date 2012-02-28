# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tg2app.model import DeclarativeBase, metadata, DBSession


class Tile(DeclarativeBase):
    """Tile Map Model"""

    __tablename__ = 'tile'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tile_type = Column(Integer)
    game_id = Column(Integer, ForeignKey('game.id'))

    def __init__(self, **kw):
        """automatically mapping attributes """
        for key, value in kw.iteritems():
            setattr(self, key, value)

    def __repr__(self):
        return "<Game %r>" % (self.id)
