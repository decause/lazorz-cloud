from sqlalchemy import *
from sqlalchemy.orm import relation, backref


class Game(DeclarativeBase):
    """ Game Model """
    __tablename__ = 'game'

    id = Column(Integer, autoincrement=True, primary_key=True)
    #tiles = relation(tiles, ...)

    def __init__(self, **kw):
        """automatically mapping attributes """
        for key, value in kw.iteritems():
            setattr(self, key, value)

    def __repr__(self):
        return "<Game %r>" % (self.id)
