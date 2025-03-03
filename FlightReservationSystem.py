import numpy as np
import pandas as pd


flights_data = {
    "Flight Number": ["AI101", "BA202", "DL303"],
    "Airline": ["Air India", "British Airways", "Delta Airlines"],
    "Total Seats": [150, 180, 200],
    "Booked Seats": [120, 160, 190],
    "Ticket Price": [8000, 12000, 10000]  # Price per ticket in ₹
}

# Creating a DataFrame from the static data
flights_df = pd.DataFrame(flights_data)


# Function 1: List All Flights
def list_all_flights():
    """
    List all available flights with details.
    TODO: Implement logic to return flight details using Pandas.
    """
    pass


# Function 2: Check Available Seats for a Flight
def available_seats_for_flight(flight_number):
    """
    Returns the number of available seats for a given flight.
    TODO: Implement logic using NumPy to calculate available seats.
    """
    pass


# Function 3: Calculate Total Revenue for All Flights
def total_revenue_for_all_flights():
    """
    Calculates total revenue generated from all booked seats.
    TODO: Implement logic using Pandas operations.
    """
    pass


# Main Function to Execute and Display Results
def main():
    """
    Main execution function.
    TODO: Call each function and print the results.
    """
    pass


if __name__ == "__main__":
    main()
