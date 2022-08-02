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
