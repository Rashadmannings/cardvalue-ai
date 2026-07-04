from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)

    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    grading_company_id = Column(Integer, ForeignKey("grading_companies.id"), nullable=False)

    grade = Column(String, nullable=True)
    price = Column(Float, nullable=False)

    marketplace = Column(String, nullable=False)
    seller = Column(String, nullable=True)
    url = Column(String, nullable=True)

    last_seen = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    card = relationship("Card", back_populates="listings")
    grading_company = relationship("GradingCompany", back_populates="listings")