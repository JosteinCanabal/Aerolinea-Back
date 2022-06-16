from pydantic import BaseModel
from app.core.schema.userModel import User
from app.core.models.bookingStatus import BookingStatus
from app.core.schema.flightModel import FlightResponse as Flight


class BookingRequest(BaseModel):
    status: BookingStatus
    paymentToken: str
    checkedIn: bool
    createdAt: str
    bookingReference: str


class Booking(BookingRequest):
    outboundFlight: int
    customer: int


class BookingResponse(Booking):
    id: int

    class Config:
        orm_mode = True
