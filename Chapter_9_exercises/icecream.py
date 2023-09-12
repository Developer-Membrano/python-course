from dessert import Dessert

class IceCream(Dessert):
    def __init__(self, kind_of_icecream, flavours):
        super().__init__(kind_of_icecream+" ice cream", flavours)

    

def main():
    vanilla = IceCream("American", "Chocolate")
    result = vanilla.response()
    print(result)

if __name__ == "__main__":
    main()