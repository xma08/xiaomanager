from datetime import date

from sqlalchemy.orm import Session

from .. import models
from ..schema.transaction import TransactionIn


def create_transaction(db: Session, transaction: TransactionIn) -> models.Transaction:
    db_transaction = models.Transaction(
        card_id=transaction.card_id,
        price=transaction.price,
        category=transaction.category,
        transaction_at=transaction.transaction_at,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_total_amount(db: Session, start_date: date = None, end_date: date = None):
    transactions = (
        db.query(models.Transaction)
        .filter(models.Transaction.transaction_at >= start_date)
        .filter(models.Transaction.transaction_at >= end_date)
        .all()
    )
    return sum([transaction.price for transaction in transactions])
