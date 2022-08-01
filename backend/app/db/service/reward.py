from sqlalchemy.orm import Session

from .. import models
from ..schema.reward import RewardIn


def create_reward(db: Session, reward: RewardIn) -> models.Reward:
    db_reward = models.Reward(
        card_id=reward.card_id,
        name=reward.name,
        discount=reward.discount,
        category=reward.category,
        valid_from=reward.valid_from,
        valid_to=reward.valid_to,
    )
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return db_reward
