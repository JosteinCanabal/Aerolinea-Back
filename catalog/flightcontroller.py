from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.core.schema.flightModel import FlightRequest, FlightResponse
from app.catalog import flightServices

flightRouter = APIRouter()


@flightRouter.post("/catalog")
def create(obj: FlightRequest, db: Session = Depends(get_db)):
    return flightServices.create_flight(db, obj)


@flightRouter.get("/catalog/", response_model=list[FlightResponse])
def get_catalog(departureAirportCode: str,
                arrivalAirportCode: str,
                departureDate: str, db: Session = Depends(get_db)):
    return flightServices.get_flight_depAir_arrAir_depDate(db, departureAirportCode, arrivalAirportCode, departureDate)
    # if data is None:
    #     raise HTTPException(status_code=404, detail="Flight not found")
    # return data


@flightRouter.get("/catalog/{airportCode}", response_model=list[FlightResponse])
def get_catalogAirportCode(airportCode: str, departureDate: str, db: Session = Depends(get_db)):
    return flightServices.get_flight_airportCode_departureDate(db, airportCode, departureDate)


# ELIMINAR
@flightRouter.delete("/catalog/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return flightServices.delete(db, id)

    # ACTUALIZAR
@flightRouter.put("/catalog/{id}", response_model=FlightResponse)
def update(id: int, flight: FlightRequest, db: Session = Depends(get_db)):
    return flightServices.update(db, id, flight)
