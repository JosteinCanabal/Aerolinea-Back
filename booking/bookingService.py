from sqlalchemy.orm import Session
from app.core.models.models import Booking
from app.core.schema.bookingModel import BookingRequest, BookingResponse


def create_booking(db: Session, booking: BookingRequest):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_by_id(db: Session, id: int):
    return  db.query(Booking).filter(Booking.id == id).first()
