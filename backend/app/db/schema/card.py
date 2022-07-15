from datetime import datetime

from pydantic import BaseModel

from ..models import CardType


class CardBase(BaseModel):
    user_id: int
    nickname: str
    encrypted_number: str
    expiration_year: int
    expiration_month: int
    csv_code: int
    card_type: CardType


class CardOut(CardBase):
    created_at: datetime

    class Config:
        orm_mode = True


class CardIn(CardBase):
    pass
