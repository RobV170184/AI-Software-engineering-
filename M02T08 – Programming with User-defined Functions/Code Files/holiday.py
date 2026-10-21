# M02T08: User-defined Functions - Holiday cost calculator
# This program calculates the total cost of a holiday

def hotel_cost(num_nights):
    """
    Calculate the total cost for hotel stay.

    Parameters:
        num_nights (int): Number of nights staying at the hotel.

    Returns:
        float: Total cost for the hotel stay.
    """
    price_per_night = 100
    return num_nights * price_per_night


def plane_cost(city_flight):
    """
    Calculate the cost of the flight based on destination city.

    Parameters:
        city_flight (str): The city flying to.

    Returns:
        float: Cost of the flight.
    """
    if city_flight == "New York":
        return 500
    elif city_flight == "London":
        return 600
    elif city_flight == "Tokyo":
        return 800
    elif city_flight == "Paris":
        return 550
    else:
        return 400


def car_rental(rental_days):
    """
    Calculate the total cost for car rental.

    Parameters:
        rental_days (int): Number of days renting a car.

    Returns:
        float: Total cost for the car rental.
    """
    daily_rental_cost = 50
    return rental_days * daily_rental_cost


def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculate the total cost of the holiday.

    Parameters:
        num_nights (int): Number of nights at hotel.
        city_flight (str): Destination city.
        rental_days (int): Number of days renting a car.

    Returns:
        float: Total holiday cost.
    """
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)

    return hotel_total + plane_total + car_total


# Get user inputs
print("Welcome to the Holiday Cost Calculator!")
print("\nAvailable cities: New York, London, Tokyo, Paris, Other")
city_flight = input("Enter the city you will be flying to: ")
num_nights = int(input("Enter the number of nights you will stay at a hotel: "))
rental_days = int(input("Enter the number of days you will hire a car: "))

# Calculate costs
hotel_total = hotel_cost(num_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days)
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print out all details
print("\n" + "="*50)
print("HOLIDAY COST BREAKDOWN")
print("="*50)
print(f"Destination: {city_flight}")
print(f"Flight cost: ${plane_total:.2f}")
print(f"Hotel cost ({num_nights} nights): ${hotel_total:.2f}")
print(f"Car rental ({rental_days} days): ${car_total:.2f}")
print("-"*50)
print(f"TOTAL HOLIDAY COST: ${total_cost:.2f}")
print("="*50)
