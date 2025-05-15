"""This is a program for travel agents to compile a client's flight information into one email automatically for rapid sending."""
"""It also stores the flight data in a CSV file for future reference."""

import actions

if __name__ == "__main__":
    print("\nWelcome to the Waikato Air Email Generator!")
    while True:
        choice = input("\nPlease type 'book' to make a new booking, 'view' to see past bookings, or 'exit' to quit: ").strip().lower()
        if choice == "book":
            actions.main()
        elif choice == "view":
            actions.load_booking_by_name("waikato_air_bookings.csv")
        elif choice == "exit":
            break
        else:
            print("Please type 'book', 'view', or 'exit'.")
