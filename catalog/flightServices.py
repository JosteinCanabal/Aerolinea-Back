from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.schema.flightModel import FlightRequest, FlightResponse
from app.core.models.models import Flight


def create_flight(db: Session, flight: FlightRequest):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


def get_all(db: Session):
    return db.query(Flight).offset(0).limit(100).all()


def get_flight_depAir_arrAir_depDate(db: Session,
                                     departureAirportCode: str,
                                     arrivalAirportCode: str,
                                     departureDate: str):
    return db.query(Flight).filter(Flight.arrivalAirportCode == arrivalAirportCode,
                                   Flight.departureAirportCode == departureAirportCode,
                                   Flight.departureDate == departureDate).all()


def get_flight_airportCode_departureDate(db: Session, airport: str, departureDate: str):
    return db.query(Flight).filter(Flight.departureAirportCode == airport,
                                   Flight.departureDate == departureDate).all()


def delete(db: Session, id: int):
    db_flight = db.query(Flight).get(id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found ")
    db.delete(db_flight)
    db.commit()
    return {"delete": True}


def update(db: Session, id: int, flight: FlightRequest):
    db_flight = db.query(Flight).filter(Flight.id == id).first()
    if not db_flight:
        return None
    flight_data = flight.dict(exclude_unset=True)
    for key, value in flight_data.items():
        setattr(db_flight, key, value)
    db.add(db_flight)
    db.commit()
    return db_flight
