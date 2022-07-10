import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.sql import func

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class CardType(str, enum.Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    nickname = Column(String)
    encrypted_number = Column(String, nullable=False)
    expiration_year = Column(Integer, nullable=False)
    expiration_month = Column(Integer, nullable=False)
    csv_code = Column(Integer, nullable=False)
    card_type = Column(Enum(CardType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
