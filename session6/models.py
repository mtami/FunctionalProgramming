from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime


class InvoiceChoice(Enum):
    inv1 = auto()
    inv2 = auto()
    inv3 = auto()
    inv4 = auto()
    inv5 = auto()


class ShippingChoice(Enum):
    ship1 = auto()
    ship2 = auto()
    ship3 = auto()


class FreightChoice(Enum):
    fr1 = auto()
    fr2 = auto()
    fr3 = auto()
    fr4 = auto()
    fr5 = auto()
    fr6 = auto()


class AvailabilityChoice(Enum):
    av1 = auto()
    av2 = auto()
    av3 = auto()
    av4 = auto()


class ShippingDateChoice(Enum):
    sd1 = auto()
    sd2 = auto()
    sd3 = auto()
    sd4 = auto()
    sd5 = auto()


@dataclass
class ShippingDate:
    date: datetime


@dataclass
class Availability:
    date: datetime


@dataclass
class Freight:
    cost: float = 0


@dataclass
class Shipping:
    id: int
    cost: float = 0


@dataclass
class Invoice:
    cost: float = 0


@dataclass
class Customer:
    name: str


@dataclass
class Order:
    customer: Customer
    date: datetime
    cost: float


@dataclass
class ProcessConfiguration:
    invoice_choice: InvoiceChoice
    shipping_choice: ShippingChoice
    freight_choice: FreightChoice
    availability_choice: AvailabilityChoice
    shipping_date_choice: ShippingDateChoice
