from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    grading_company_id = Column(Integer, ForeignKey("grading_companies.id"), nullable=False)

    grade = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    shipping = Column(Float, nullable=True)

    marketplace = Column(String, nullable=False)
    sold_date = Column(DateTime, nullable=False)
    url = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    card = relationship("Card", back_populates="sales")
    grading_company = relationship("GradingCompany", back_populates="sales")