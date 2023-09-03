
class Restaurant:

    def __init__(self, resto_name, cuisine_type):
        self.resto_name = resto_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def open_restaurant(self):
        print(f"Welcome to {self.resto_name} we are now open! ")
    
    def describe_restaurant(self):
        print(f"We are a {self.cuisine_type} type and we mostly have juice bar!")

restaurant_01 = Restaurant('Namayan Village', 'Sea foods')
restaurant_02 = Restaurant('Manila Recto', 'Samgyup')
restaurant_03 = Restaurant('Italy Bar', 'Meat and bread')

restaurant_01.open_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()
restaurant_01.number_served


class User:

    def __init__(self, first_name, last_name, account_type, isActive):
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self.isActive = isActive
        self.ticket = 0

    
    def describe_user(self):
        name = f"Full Name: {self.first_name} {self.last_name}"
        account_status = f"Account type: {self.account_type} \nactive? {self.isActive}"
        print(f"{name}\n{account_status}")
    
    def update_ticket(self, total_tickets):
        return f"{self.first_name} has a {total_tickets} number of tickets! "


user_101 = User('Kenny', 'Membrano', 'Admin', 'True')
user_102 = User('Mystic', 'Cat', 'Guess', 'False')
user_103 = User('Fluffy', 'Bear', 'Co-admin', 'True')

user_101.describe_user()
print("----------------------")
user_102.describe_user()
print("----------------------")
user_103.describe_user()
print("----------------------")
display_ticket = user_103.update_ticket(20)
print(display_ticket)