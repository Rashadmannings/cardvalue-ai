from pydantic import BaseModel


class CardResponse(BaseModel):
    id: int
    player: str
    year: int
    brand: str
    set_name: str | None = None
    card_number: str | None = None
    parallel: str | None = None
    rookie: bool

    class Config:
        from_attributes = True