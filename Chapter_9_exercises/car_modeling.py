class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.sit_seater = 4
        
        self.dict_model = {"Brand Name" :self.make, 
                      "Model" :self.model, 
                      "Date release" :self.year, 
                      "Number of sits" :self.sit_seater}

    def describe_model(self):
        for key_model, value_model in self.dict_model.items():
            print(f"{key_model} : {value_model}")

    def fill_gas_tank(self):
        print(f"{self.model} filling a gas tank... ")
    
customer_101 = Car("suzuki", "black fortuner", 2021)
customer_101.describe_model()
print(customer_101.dict_model.get("Model"))