"""This file contains the information collected in the program using classes."""

import random


class Traveller:
    """Contains the information of the client."""

    def __init__(self, name: str, age: int, date_of_flight: str):
        """Collect information about the client."""
        self.name = name
        self.age = age
        self.date_of_flight = date_of_flight


class Flight:
    """Contains the information for the flight itself."""

    def __init__(self, departure: str, destination: str, base_fare: float, seats_available: int):
        """Take in flight information."""
        self.departure = departure
        self.destination = destination
        self.base_fare = base_fare
        self.seats_available = seats_available
        self.flight_number = self.generate_flight_number()

    def generate_flight_number(self) -> str:
        """Generate a flight number for the client's flight."""
        return f"WA{random.randint(100, 999)}"


class Booking:
    """Contains the booking details."""

    def __init__(self, traveller: Traveller, flight: Flight, discount: float):
        """Combine the other classes and apply discount for email purposes."""
        self.traveller = traveller
        self.flight = flight
        self.discount = discount[0]
        self.discount_type = discount[1]
        self.final_fare = flight.base_fare - discount[0]
