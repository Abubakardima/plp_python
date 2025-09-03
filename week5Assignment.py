"""
 Assignment 1: Design Your Own Class
 
We will design a Smartphone class that inherits from a Device class.
It will have constructors, attributes, methods, and show inheritance + polymorphism.
"""

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
        self.apps = []  # list to hold installed apps

    # Method to install apps
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed successfully on {self.model}!")

    # Method to check battery
    def check_battery(self):
        return f"Battery level: {self.battery}%"

    # Overriding parent method (Polymorphism example)
    def device_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Test Assignment 1
print("=== Assignment 1: Smartphone Class ===")
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 80)
phone2 = Smartphone("Apple", "iPhone 14", 128, 95)

print(phone1.device_info())
phone1.install_app("WhatsApp")
print(phone1.check_battery())

print(phone2.device_info())
phone2.install_app("Instagram")



"""

 Activity 2: Polymorphism Challenge

We will create different classes (Car, Plane, Boat, Animal) 
with the same move() method, but each behaves differently.
"""

class Car:
    def move(self):
        print("Driving ")

class Plane:
    def move(self):
        print("Flying ")

class Boat:
    def move(self):
        print("Sailing ")

class Animal:
    def move(self):
        print("Walking ")

# Test Activity 2
print("\n=== Activity 2: Polymorphism Challenge ===")
objects = [Car(), Plane(), Boat(), Animal()]

for obj in objects:
    obj.move()
