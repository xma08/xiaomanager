from datetime import datetime

from pydantic import BaseModel

from ..models import TransactionCategory


class TransactionBase(BaseModel):
    card_id: int
    price: float
    category: TransactionCategory
    transaction_at: datetime


class TransactionOut(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TransactionIn(TransactionBase):
    pass
