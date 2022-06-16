from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.models.bookingStatus import BookingStatus
from app.booking.bookingService import create_booking, get_by_id
from app.core.schema.bookingModel import BookingRequest, Booking, BookingResponse
from typing import Union

from app.database.database import get_db

bookingRouter = APIRouter()


@bookingRouter.post("/booking/flight/{idflight}/user/{iduser}")
def create(idflight: int, iduser: int, bookingRequest: BookingRequest, db: Session = Depends(get_db)):
    booking = Booking(customer=iduser, outboundFlight=idflight, **bookingRequest.dict())
    return create_booking(db, booking)


@bookingRouter.get("/booking/{id}", response_model=BookingResponse)
def getById(id: int, db: Session = Depends(get_db)):
    booking_obj = get_by_id(db, id)
    if booking_obj is None:
        raise HTTPException(status_code=404, detail="No se encontró")
    return booking_obj


@bookingRouter.get("/booking/")
def get_booking_status_customer_name(status: Union[BookingStatus, None] = None, customerName: Union[str, None] = None,
                                     db: Session = Depends(get_db)):
    print(status, customerName)

@bookingRouter.delete("/booking/{id}")
def delete(id:int):
    pass

