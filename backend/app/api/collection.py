from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.database import get_db
from app.models.collection_item import CollectionItem
from app.models.user import User
from app.schemas.collection import (
    CollectionItemCreate,
    CollectionItemResponse,
)

router = APIRouter(
    prefix="/collection",
    tags=["Collection"],
)


@router.post("", response_model=CollectionItemResponse)
def add_card_to_collection(
    item: CollectionItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    collection_item = CollectionItem(
        user_id=current_user.id,
        card_id=item.card_id,
        grading_company_id=item.grading_company_id,
        grade=item.grade,
        quantity=item.quantity,
        purchase_price=item.purchase_price,
        purchase_marketplace=item.purchase_marketplace,
        notes=item.notes,
    )

    db.add(collection_item)
    db.commit()
    db.refresh(collection_item)

    return collection_item


@router.get("", response_model=list[CollectionItemResponse])
def get_my_collection(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    collection_items = (
        db.query(CollectionItem)
        .filter(CollectionItem.user_id == current_user.id)
        .all()
    )

    return collection_items