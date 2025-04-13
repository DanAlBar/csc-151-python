def make_car(manufacturer, model_name, **car_info):
    """Store information about a car in a dictionary."""
    car = {'manufacturer': manufacturer, 'model': model_name}
    car.update(car_info)
    return car

# Call the function with required and additional arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to verify the information
print(car)

car2 = make_car('toyota', 'corolla', color='red', sunroof=True, year=2022)
print(car2)

