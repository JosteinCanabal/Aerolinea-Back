from enum import Enum


class BookingStatus(str, Enum):
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
