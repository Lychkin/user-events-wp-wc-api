from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class EventCreate(BaseModel):
    item_id: int
    user_id: int
    event: Literal["view", "add_to_cart"]


class EventResponse(BaseModel):
    item_id: int
    user_id: int
    timestamp: datetime
    event: str

    class Config:
        from_attributes = True
