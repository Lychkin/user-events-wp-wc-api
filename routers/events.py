from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas.event import EventCreate
from crud.event import create_event, get_events

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/")
def read_events(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return get_events(db, page, per_page)


@router.post("/")
def add_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)
