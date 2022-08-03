from datetime import date

from app.core.auth import get_current_active_user
from app.db.schema.transaction import TransactionIn, TransactionOut
from app.db.service.transaction import create_transaction, get_total_amount
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


@r.get("/total_amount")
async def total_amount(
    start_date: date = None,
    end_date: date = None,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    get total amount
    """
    amount = get_total_amount(db, start_date=start_date, end_date=end_date)
    return "{:.2f}".format(amount)
