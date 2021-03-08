class Vehicle:
    def __init__(self, type, model, price):
        self.owner = None
        self.price = price
        self.type = type
        self.model = model

    def buy(self, money, name):

        if money < self.price:
            return "Sorry, not enough money"
        elif self.owner:
            return "Car already sold"
        else:
            self.owner = name
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"



'''•	buy(money, owner) - if the person has enough money and the vehicle has no owner, returns:  and sets the owner to the given one. If the money is not enough, return: "Sorry, not enough money". If the car already has an owner, return: "Car already sold"
•	sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
•	__repr__() - returns  if the vehicle has an owner. Otherwise, return: "{model} {type} is on sale: {price}"
'''
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
