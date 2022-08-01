from datetime import datetime

from pydantic import BaseModel

from ..models import RewardType


class RewardBase(BaseModel):
    card_id: int
    name: str
    discount: int
    category: RewardType
    valid_from: datetime
    valid_to: datetime


class RewardOut(RewardBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class RewardIn(RewardBase):
    pass
