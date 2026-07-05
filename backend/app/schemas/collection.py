from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CollectionItemCreate(BaseModel):
    card_id: int
    grading_company_id: int
    grade: Optional[str] = None
    quantity: int = 1

    purchase_price: Optional[float] = None
    purchase_marketplace: Optional[str] = None
    notes: Optional[str] = None


class CollectionItemResponse(BaseModel):
    id: int

    card_id: int
    grading_company_id: int

    grade: Optional[str]
    quantity: int

    purchase_price: Optional[float]
    purchase_marketplace: Optional[str]
    notes: Optional[str]

    created_at: datetime

    class Config:
        from_attributes = True