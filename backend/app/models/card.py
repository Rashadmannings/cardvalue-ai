from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    year = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    set_name = Column(String, nullable=True)
    card_number = Column(String, nullable=True)
    parallel = Column(String, nullable=True)
    rookie = Column(Boolean, default=False)

    player = relationship("Player", back_populates="cards")
    sales = relationship("Sale", back_populates="card")
    listings = relationship("Listing", back_populates="card")