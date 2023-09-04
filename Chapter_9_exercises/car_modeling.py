class Battery:
    def __init__(self, battery=150):
        self.battery = battery
    
    def describe_battery(self):
        return f"The battery size is {self.battery}"

    def get_range(self):
        if self.battery > 40 and self.battery < 60:
             range = "Equivalent to 150 CC"
        elif self.battery > 60 and self.battery < 100:
            range = "Equivalent to 500 CC"
        else:
            range = "Equivalent to 1000 CC"
        return range

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.sit_seater = 4
        self.battery = Battery()
        
        self.dict_model = {"Brand Name" :self.make, 
                      "Model" :self.model, 
                      "Date release" :self.year, 
                      "Number of sits" :self.sit_seater}
        

    def describe_model(self):
        for key_model, value_model in self.dict_model.items():
            print(f"{key_model} : {value_model}")

    def fill_gas_tank(self):
        print(f"{self.model} filling a gas tank... ")
    
    def moving_forward(self):
        return f"{self.make} currently moving forward"

    def moving_backward(self):
        return f"{self.make} currently moving backward"

    def automatic_parking(self):
        return True
    
    def is_traffic_jam(self, isTraffic):
        return f"It's {isTraffic} {self.make} is in the traffic jam"


""" Child Class """
class ElectricCar(Car):

    def __init__(self, make, model, year, isCharging, flag_traffic):
        super().__init__(make, model, year)

        self.isCharging = isCharging
        self.flag_traffic = flag_traffic

    def fill_gas_tank(self): #sample of overriding a method from a parent class
       return f"{self.model} currently charging... " 

    def is_traffic(self): #sample of passing the attribute of a child class to parent class to it's method
        return super().is_traffic_jam(self.flag_traffic)


customer_101 = Car("suzuki", "black fortuner", 2021) #Parent class
customer_102 = ElectricCar("Honda", "Yellow cab", 2022, False, "Traffic sa Edsa") #Child class



print_battery = customer_101.battery.describe_battery()
print_range = customer_101.battery.get_range()
print(print_battery)
print(print_range)