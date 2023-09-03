
def create_model(number_of_seats, *attributes):
    car_attribute = [attribute for attribute in attributes]
    match(number_of_seats):
        case 4:
            print("Creating a simple car! ")
        case 6:
            print("Creating a van for family size ")
        case _:
            print("Creating a Truck for delivery")

    return car_attribute
