"""This file contains the definitions and action entities of the program."""

import datetime
import ast
import csv
from typing import List, Dict
import data
import webbrowser
import urllib.parse


class EmailGenerator:
    """Generates the email to send to the client."""

    @staticmethod
    def generate_email(booking: data.Booking) -> str:
        """Compiles the body and subject of the email and returns it."""
        email_subject = (
            f"Your Waikato Air Flight Details – {booking.flight.flight_number}\n\n"
        )
        email_body = (
            f"Dear {booking.traveller.name},\n\n"
            "Thank you for booking your flight with Waikato Air. Here are your flight details:\n\n"
            f"Flight Number: {booking.flight.flight_number}\n"
            f"Route: {booking.flight.departure} to {booking.flight.destination}\n"
            f"Original Fare: ${booking.flight.base_fare:.2f}\n"
        )
        if booking.discount > 0:
            percentage = (booking.discount / booking.flight.base_fare) * 100
            email_body += f"Discount Applied: {percentage:.0f}% ({booking.discount_type})\n"
        email_body += f"Final Fare: ${booking.final_fare:.2f}\n\n"
        email_body += (
            "We look forward to flying you safely and comfortably.\n\n"
            "Kind regards,\nWaikato Air Customer Services"
        )
        return email_body, email_subject


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
            input_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            if input_date > datetime.date.today():
                return date_input
            else:
                print("Too late, please enter a date beyond today.")
        except ValueError:
            print("Please use YYYY-MM-DD.")


def get_valid_name(prompt: str) -> int:
    """Make sure the user's name parts are both concise and non-numerical."""
    while True:
        name = input(prompt).strip().title()
        if len(name) > 25:
            print("Name must be 25 characters or fewer.")
            continue
        if not name.replace(" ", "").isalpha():
            print("Please enter a valid name.")
            continue
        return name
    

def get_full_name() -> str:
    """Prompt for and return a full name, combining validated first and last names."""
    first_name = get_valid_name("Enter traveller's first/middle name (max 25 characters): ")
    last_name = get_valid_name("Enter traveller's last name (max 25 characters): ")
    return f"{first_name} {last_name}"


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
        if seat_input.isdigit() and int(seat_input) > 0 and int(seat_input) < 171:
            return int(seat_input)
        else:
            print("Please re-enter the number of remaining seats.")


def apply_discount(flight: data.Flight, date_str: str, age: int) -> (float, str): # type: ignore
    """Return the reduction quantity from the final price with age, date, and seat considerations."""
    try:
        discount_status = False
        flight_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        days_until_flight = (flight_date - today).days
        discount_percentage_decimal = 0
        child = False
        senior = False
        urgent = False
        urgent_seat_scarcity = False
        discount_status = False
        discount_text = ""

        if age <= 16:
            discount_percentage_decimal = discount_percentage_decimal + 0.20
            child = True
            discount_status = True
        elif age >= 65:
            discount_percentage_decimal = discount_percentage_decimal + 0.25
            senior = True
            discount_status = True
        if days_until_flight < 20 or flight.seats_available < 50:
            discount_percentage_decimal = discount_percentage_decimal + 0.20
            urgent_seat_scarcity = True
            discount_status = True
        elif days_until_flight < 50:
            discount_percentage_decimal = discount_percentage_decimal + 0.10
            urgent = True
            discount_status = True

        if not discount_status:
            return 0.0, ""

        if child and urgent_seat_scarcity:
            discount_text = "Child + Urgency/Seat Scarcity Discount"
        elif child and urgent:
            discount_text = "Child + Urgency Discount"
        elif senior and urgent_seat_scarcity:
            discount_text = "Senior + Urgency/Seat Scarcity Discount"
        elif senior and urgent:
            discount_text = "Senior + Urgency Discount"
        elif urgent_seat_scarcity:
            discount_text = "Urgency/Seat Scarcity Discount"
        elif urgent:
            discount_text = "Urgency Discount"
        elif child:
            discount_text = "Child Discount"
        elif senior:
            discount_text = "Senior Discount"

        return flight.base_fare * discount_percentage_decimal, discount_text
    except ValueError:
        print("Please use YYYY-MM-DD.")
        return 0.0, ""


def save_bookings_to_csv(filename: str, booking_data: List[Dict]):
    """Place the booking records in a CSV file."""
    try:
        file_exists = False
        try:
            with open(filename, mode="r"):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(filename, mode="a", newline="") as csvfile:
            fieldnames = [
                "name", "age", "date", "departure", "destination",
                "flight_number", "base_fare", "discount",
                "discount_type", "final_fare"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for booking in booking_data:
                writer.writerow(booking)
        print(f"\nBooking appended to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving bookings: {e}")


def load_booking_by_name(filename: str):
    """Load booking info from the CSV file by individual."""
    try:
        with open(filename, mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            names = [row["name"] for row in reader]
            
            if not names:
                print("No bookings available.")
                return

            # List existing names
            print("Existing traveller names:")
            for name in sorted(set(names)):
                print(f" - {name}")

        name = input("Please enter the traveller's full name to search: ").strip().title()

        with open(filename, mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            found = False
            for row in reader:
                if row["name"] == name:
                    found = True
                    discount = ast.literal_eval(row['discount'])
                    print(f"\n- Booking for {row['name']} -")
                    print(f"Age: {row['age']}")
                    print(f"Date of Flight: {row['date']}")
                    print(f"Route: {row['departure']} → {row['destination']}")
                    print(f"Flight Number: {row['flight_number']}")
                    print(f"Original Fare: ${float(row['base_fare']):.2f}")
                    if float(tuple(row['discount'])[1]) > 0:
                        print(f"Discount: ${discount[0]:.2f} ({discount[1]})")
                    print(f"Final Fare: ${float(row['final_fare']):.2f}")

                    # Reconstruct objects for email generation
                    traveller = data.Traveller(row["name"], int(row["age"]), row["date"])
                    flight = data.Flight(
                        row["departure"], row["destination"],
                        float(row["base_fare"]), 0  # seats_available not needed here
                    )
                    booking = data.Booking(traveller, flight, discount)
                    email, subject = EmailGenerator.generate_email(booking)

                    print("\n--- Email Preview ---")
                    print(subject)
                    print(email)
                    send_email(subject, email)
                    
            if not found:
                print(f"No bookings found for {name}.")
    except FileNotFoundError:
        print("No bookings file found.")
    except IOError as e:
        print(f"An error occurred while reading the bookings: {e}")


def send_email(subject, body):
    """Create and open a 'mailto:' link to immediately send the email."""
    while True:
        email_now = input("Would you like to email the client now? (yes/no): ")
        if email_now.lower() == "yes":
            subject_encoded = urllib.parse.quote(subject)
            body_encoded = urllib.parse.quote(body)
            mailto_link = f"mailto:?subject={subject_encoded}&body={body_encoded}"
            webbrowser.open(mailto_link)
            break
        elif email_now.lower() == "no":
            print("\nAlrighty!")
            break
        else:
            print("\nPlease enter 'yes' or 'no'.")


def main():
    """Retrieve client info and compile previous definitions."""
    name = get_full_name()

    age = get_valid_age("Enter traveller's age (max 160): ")
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
    seats_available = get_valid_seat_count("How many seats are left on this flight? (max 171): ")

    traveller = data.Traveller(name, age, date_of_flight)
    flight = data.Flight(departure, destination, base_fare, seats_available)
    discount = apply_discount(flight, date_of_flight, traveller.age)

    booking = data.Booking(traveller, flight, discount)
    email, email_subject = EmailGenerator.generate_email(booking)

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
    print(email_subject)
    print(email, "\n")
    save_bookings_to_csv("waikato_air_bookings.csv", bookings)

    send_email(email_subject, email)


ROUTES = {
    ("Hamilton", "Auckland"): 120.0,
    ("Hamilton", "Rotorua"): 100.0,
    ("Auckland", "Rotorua"): 140.0,
    ("Rotorua", "Hamilton"): 100.0,
    ("Auckland", "Hamilton"): 120.0,
    ("Rotorua", "Auckland"): 140.0
}

bookings: List[Dict] = []
