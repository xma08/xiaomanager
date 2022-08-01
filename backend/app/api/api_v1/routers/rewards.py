from app.core.auth import get_current_active_user
from app.db.schema.reward import RewardIn, RewardOut
from app.db.service.reward import create_reward
from app.db.session import get_db
from fastapi import APIRouter, Depends, Request

rewards_router = r = APIRouter()


@r.post("/rewards", response_model=RewardOut)
async def reward_create(
    request: Request,
    reward: RewardIn,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new reward
    """
    return create_reward(db, reward)
