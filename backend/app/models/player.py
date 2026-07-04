from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    team = Column(String, nullable=True)
    position = Column(String, nullable=True)

    cards = relationship("Card", back_populates="player")