from sqlalchemy.orm import Session
from datetime import datetime, UTC

from models.event import UserEvent
from schemas.event import EventCreate


def create_event(db: Session, event: EventCreate):
    db_event = UserEvent(
        item_id=event.item_id,
        user_id=event.user_id,
        event=event.event,
        timestamp=datetime.now(UTC).replace(microsecond=0),
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def get_events(db: Session, page: int, per_page: int):
    offset = (page - 1) * per_page

    query = db.query(UserEvent)

    total = query.count()

    events = (
        query.order_by(UserEvent.timestamp.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    return {"page": page, "per_page": per_page, "total": total, "data": events}
