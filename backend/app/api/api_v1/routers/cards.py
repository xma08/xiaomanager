from app.core.auth import get_current_active_user
from app.db.schema.card import CardIn, CardOut
from app.db.service.card import create_card
from app.db.session import get_db
from fastapi import APIRouter, Depends, Request

cards_router = r = APIRouter()


@r.post("/cards", response_model=CardOut)
async def card_create(
    request: Request,
    card: CardIn,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new card
    """
    return create_card(db, card)
