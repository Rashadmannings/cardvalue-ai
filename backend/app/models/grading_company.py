from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class GradingCompany(Base):
    __tablename__ = "grading_companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    abbreviation = Column(String, nullable=False, unique=True)

    sales = relationship("Sale", back_populates="grading_company")
    listings = relationship("Listing", back_populates="grading_company")