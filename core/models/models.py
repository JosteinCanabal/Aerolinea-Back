from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# from core.models.bookingStatus import BookingStatus

from app.database.database import Base


class Booking(Base):
    __tablename__ = "Booking"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    outboundFlight = Column(Integer, ForeignKey("Flight.id"))
    outboundFlight_flight = relationship("Flight", foreign_keys=[outboundFlight])
    paymentToken = Column(String)
    checkedIn = Column(Boolean)
    customer = Column(Integer, ForeignKey("User.id"))
    customer_user = relationship("User", foreign_keys=[customer])
    createdAt = Column(String)
    bookingReference = Column(String)

    def dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "outboundFlight": self.outboundFlight,
            "paymentToken": self.paymentToken,
            "checkedIn": self.checkedIn,
            "customer": self.customer,
            "createdAt": self.createdAt,
            "bookingReference": self.bookingReference
        }


class Flight(Base):
    __tablename__ = "Flight"
    id = Column(Integer, primary_key=True, index=True)
    departureDate = Column(String, index=True)
    departureAirportCode = Column(String, index=True)
    departureAirportName = Column(String)
    departureCity = Column(String)
    departureLocale = Column(String)
    arrivalDate = Column(String)
    arrivalAirportCode = Column(String, index=True)
    arrivalAirportName = Column(String)
    arrivalCity = Column(String)
    arrivalLocale = Column(String)
    ticketPrice = Column(Integer)
    ticketCurrency = Column(String)
    flightNumber = Column(Integer)
    seatCapacity = Column(Integer)

    # booking = relationship("Booking", back_populates="outboundFlight")

    def dict(self):
        return {
            # "id": self.id,
            "departureDate": self.departureDate,
            "departureAirportCode": self.departureAirportCode,
            "departureAirportName": self.departureAirportName,
            "departureCity": self.departureCity,
            "departureLocale": self.departureLocale,
            "arrivalDate": self.arrivalDate,
            "arrivalAirportCode": self.arrivalAirportCode,
            "arrivalAirportName": self.arrivalAirportName,
            "arrivalCity": self.arrivalCity,
            "arrivalLocale": self.arrivalLocale,
            "ticketPrice": self.ticketPrice,
            "ticketCurrency": self.ticketCurrency,
            "flightNumber": self.flightNumber,
            "seatCapacity": self.seatCapacity,
            # "booking": self.booking
        }


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    # booking_id = Column(Integer, ForeignKey("Booking.id"))
    # bookin = relationship("Booking", back_populates="customer")

    # def dict(self):
    #     return {
    #         "id": self.id,
    #         "fullname": self.fullname,
    #         "username": self.username,
    #         "password": self.password
    #
    #     }
