from app.core.security import get_password_hash
from sqlalchemy.orm import Session

from .. import models
from ..schema.card import CardIn


def create_card(db: Session, card: CardIn) -> models.Card:
    hashed_card_number = get_password_hash(card.encrypted_number)
    db_card = models.Card(
        user_id=card.user_id,
        nickname=card.nickname,
        encrypted_number=hashed_card_number,
        expiration_year=card.expiration_year,
        expiration_month=card.expiration_month,
        csv_code=card.csv_code,
        card_type=card.card_type,
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card
