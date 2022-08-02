from app.core.auth import get_current_active_user
from app.db.schema.transaction import TransactionIn, TransactionOut
from app.db.service.transaction import create_transaction
from app.db.session import get_db
from fastapi import APIRouter, Depends, Request

transactions_router = r = APIRouter()


@r.post("/transactions", response_model=TransactionOut)
async def transaction_create(
    request: Request,
    transaction: TransactionIn,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new transaction
    """
    return create_transaction(db, transaction)
