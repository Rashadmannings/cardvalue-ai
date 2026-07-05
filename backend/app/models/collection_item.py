import uuid

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class CollectionItem(Base):
    __tablename__ = "collection_items"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    grading_company_id = Column(Integer, ForeignKey("grading_companies.id"), nullable=False)

    status = Column(String, nullable=False, default="owned")
    grade = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False, default=1)

    purchase_price = Column(Float, nullable=True)
    purchase_date = Column(DateTime, nullable=True)
    purchase_marketplace = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User")
    card = relationship("Card")
    grading_company = relationship("GradingCompany")