"""This file contains the definitions and action entities of the program."""

import datetime
from typing import List, Dict
import data


class EmailGenerator:
    """Generates the email to send to the client."""

    @staticmethod
    def generate_email(booking: data.Booking) -> str:
        """Compiles the body and subject of the email and returns it."""
        email = (
            f"Subject: Your Waikato Air Flight Details – {booking.flight.flight_number}\n\n"
            f"Dear {booking.traveller.name},\n\n"
            "Thank you for booking your flight with Waikato Air. Here are your flight details:\n\n"
            f"Flight Number: {booking.flight.flight_number}\n"
            f"Route: {booking.flight.departure} to {booking.flight.destination}\n"
            f"Original Fare: ${booking.flight.base_fare:.2f}\n"
        )
        if booking.discount > 0:
            percentage = (booking.discount / booking.flight.base_fare) * 100
            email += f"Discount: {percentage:.0f}%\n"
        email += f"Final Fare: ${booking.final_fare:.2f}\n\n"
        email += (
            "We look forward to flying you safely and comfortably.\n\n"
            "Kind regards,\nWaikato Air Customer Services"
        )
        return email


def get_valid_city(prompt: str, valid_cities: List[str]) -> str:
    """Make sure the user's city input is valid."""
    while True:
        city = input(prompt).strip().title()
        if city in valid_cities:
            return city
        else:
            print(f"Please choose from: {', '.join(valid_cities)}")


def get_valid_date(prompt: str) -> str:
    """Make sure the user's date input is valid."""
    while True:
        date_input = input(prompt).strip()
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Please use YYYY-MM-DD.")


def get_valid_age(prompt: str) -> int:
    """Make sure the user's client age input is valid, and that the client isn't a Vampire."""
    while True:
        age_input = input(prompt).strip()
        if age_input.isdigit() and int(age_input) > 0 and int(age_input) < 160:
            return int(age_input)
        else:
            print("Please enter a valid age.")


def get_valid_seat_count(prompt: str) -> int:
    """Make sure overbooking is a thing of the past, and prevents float entries."""
    while True:
        seat_input = input(prompt).strip()
        if seat_input.isdigit() and int(seat_input) > 0 and int(seat_input) < 200:
            return int(seat_input)
        else:
            print("Please re-enter the number of remaining seats.")


def apply_discount(flight: data.Flight, date_str: str, age: int) -> (float, str): # type: ignore
    """Return the reduction quantity from the final price with age, date, and seat considerations."""
    try:
        flight_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        days_until_flight = (flight_date - today).days
        discount_percentage_decimal = 0

        if age <= 16:
            discount_percentage_decimal = discount_percentage_decimal + 0.15
        elif age >= 65:
            discount_percentage_decimal = discount_percentage_decimal + 0.25
        if days_until_flight < 20 or flight.seats_available < 50:
            discount_percentage_decimal = discount_percentage_decimal + 0.20
        elif days_until_flight < 50:
            discount_percentage_decimal = discount_percentage_decimal + 0.10

        return flight.base_fare * discount_percentage_decimal
    except ValueError:
        print("Please use YYYY-MM-DD.")
        return 0.0, ""


def main():
    """Retrieve client info and compiles previous definitions."""
    name = input("\nEnter traveller's full name: ").strip().title()
    while not name.replace(" ", "").isalpha():
        print("Please enter the Traveller's name correctly.")
        name = input("Enter traveller's full name: ").strip().title()

    age = get_valid_age("Enter traveller's age: ")
    date_of_flight = get_valid_date("Please enter your date of flight (YYYY-MM-DD): ")

    valid_cities = ["Hamilton", "Rotorua", "Auckland"]
    departure = get_valid_city("Please enter your departure city (Hamilton, Rotorua, Auckland): ", valid_cities)

    # Prevent user from entering repeat input
    destination_choices = [city for city in valid_cities if city != departure]
    destination = get_valid_city(f"Please enter your destination city ({', '.join(destination_choices)}): ", destination_choices)

    route = (departure, destination)
    if route not in ROUTES:
        print("Sorry, unfortunately there are no flights available on that route.")
        return

    base_fare = ROUTES[route]
    seats_available = get_valid_seat_count("How many seats are left on this flight?: ")

    traveller = data.Traveller(name, age, date_of_flight)
    flight = data.Flight(departure, destination, base_fare, seats_available)
    discount = apply_discount(flight, date_of_flight, traveller.age)

    booking = data.Booking(traveller, flight, discount)
    email = EmailGenerator.generate_email(booking)

    # Store booking
    bookings.append({
        "name": name,
        "age": age,
        "date": date_of_flight,
        "departure": departure,
        "destination": destination,
        "flight_number": flight.flight_number,
        "base_fare": base_fare,
        "discount": discount,
        "final_fare": booking.final_fare
    })

    print("\n--- Email Output ---\n")
    print(email)


ROUTES = {
    ("Hamilton", "Auckland"): 120.0,
    ("Hamilton", "Rotorua"): 100.0,
    ("Auckland", "Rotorua"): 140.0,
    ("Rotorua", "Hamilton"): 100.0,
    ("Auckland", "Hamilton"): 120.0,
    ("Rotorua", "Auckland"): 140.0
}

bookings: List[Dict] = []
