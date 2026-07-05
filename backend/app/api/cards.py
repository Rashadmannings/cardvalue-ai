from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.card import Card
from app.models.player import Player
from app.schemas.card import CardResponse

router = APIRouter(
    prefix="/cards",
    tags=["Cards"],
)


@router.get("", response_model=list[CardResponse])
def get_cards(
    search: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Card)

    if search:
        query = query.join(Card.player).filter(
            Card.player.has(Player.name.ilike(f"%{search}%"))
        )

    cards = query.all()

    return [
        CardResponse(
            id=card.id,
            player=card.player.name,
            year=card.year,
            brand=card.brand,
            set_name=card.set_name,
            card_number=card.card_number,
            parallel=card.parallel,
            rookie=card.rookie,
        )
        for card in cards
    ]