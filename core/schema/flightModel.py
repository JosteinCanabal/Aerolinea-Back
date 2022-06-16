from pydantic import BaseModel


class FlightRequest(BaseModel):
    # id: int
    departureDate: str
    departureAirportCode: str
    departureAirportName: str
    departureCity: str
    departureLocale: str
    arrivalDate: str
    arrivalAirportCode: str
    arrivalAirportName: str
    arrivalCity: str
    arrivalLocale: str
    ticketPrice: int
    ticketCurrency: str
    flightNumber: int
    seatCapacity: int


#
# class Config:
#     orm_mode = True


class FlightResponse(FlightRequest):
    id: int

    class Config:
        orm_mode = True
