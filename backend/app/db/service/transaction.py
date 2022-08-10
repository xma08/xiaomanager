import logging
from datetime import date

from sqlalchemy.orm import Session

from .. import models
from ..schema.transaction import TransactionIn

logger = logging.getLogger(__name__)


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


def get_total_amount(db: Session, start_date: date = None, end_date: date = None, category: models.TransactionCategory = None):
    query = db.query(models.Transaction)
    if start_date:
        query = query.filter(models.Transaction.transaction_at >= start_date)
    if end_date:
        query = query.filter(models.Transaction.transaction_at <= end_date)
    if category:
        query = query.filter(models.Transaction.category == category)
    transactions = query.all()
    return sum([transaction.price for transaction in transactions])


def get_total_rewards(db: Session, start_date: date = None, end_date: date = None):
    query = db.query(models.Transaction)
    if start_date:
        query = query.filter(models.Transaction.transaction_at >= start_date)
    if end_date:
        query = query.filter(models.Transaction.transaction_at <= end_date)
    transactions = query.all()
    logger.info(f"total transactions={len(transactions)}")
    total_rewards = 0
    for transaction in transactions:

        rewards = transaction.card.rewards
        for reward in rewards:
            if transaction.category.value == reward.category.value:
                reward = transaction.price * reward.discount * 0.01
                break
        else:
            reward = transaction.price * 0.01
        total_rewards += reward
    return total_rewards
