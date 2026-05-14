from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC

from app.database import Base


class UserEvent(Base):
    __tablename__ = "user_events"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, nullable=False, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    timestamp = Column(
        DateTime, default=datetime.now(UTC).replace(microsecond=0)
    )
    event = Column(String, nullable=False)  # "view" | "add_to_cart"
