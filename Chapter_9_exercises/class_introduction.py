class Dog:
    """
    this is a comment called Doc String
    """
    def __init__(self, name, age):
        """The variable here inside the __init__ method are called attributes"""
        self.name = name
        self.age = age
    
    def dog_info(self):
        print(f'Name: {self.name}\nAge: {self.age}')

    def sit(self):
        print(f'{self.name} is sitting...')
    
    def roll_over(self):
        print(f'{self.name} is rolling over...')

"""
this is an example of instance
german_sheppard = Dog('Change', 10)
"""    
german_sheppard = Dog('Change', 10)

"""
another instance of a class
labrador = Dog('Fluffy', 2)
"""
labrador = Dog('Fluffy', 2)

german_sheppard.dog_info()
german_sheppard.roll_over()

labrador.dog_info()
