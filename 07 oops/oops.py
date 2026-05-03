# Welcome to your polished guide to Object-Oriented Programming (OOP) in Python!
# This file will walk you through the core concepts of OOP, from the basics to more advanced topics.
# Each section includes clear explanations and commented code examples to help you understand.

# =================================================================================================
# 1. Basic Class and Object
# =================================================================================================
# A 'class' is a blueprint for creating objects. It defines a set of attributes (variables) and methods (functions) that the created objects will have.
# An 'object' is an instance of a class. It's a concrete entity created from the class blueprint.

print("1. Basic Class and Object")

class Car:
    # These are class attributes. They are shared by all instances of the class.
    brand = None
    model = None

# Creating an object (or instance) of the Car class
my_first_car = Car()
my_first_car.brand = "Toyota"
my_first_car.model = "Camry"

print(f"My first car is a {my_first_car.brand} {my_first_car.model}.\n")


# =================================================================================================
# 2. The __init__() Method (Constructor) and Instance Attributes
# =================================================================================================
# The __init__() method is a special method that Python calls automatically when you create a new instance of a class.
# It's often referred to as a "constructor."
# We use it to initialize the object's attributes (instance attributes).

print("2. The __init__() Method")

class CarWithInit:
    # The __init__ method initializes the object with the provided values.
    def __init__(self, brand, model):
        # 'self' refers to the instance of the class being created.
        # These are 'instance attributes' because they are specific to each instance.
        self.brand = brand
        self.model = model

# When we create an object, we pass the arguments for the __init__ method.
my_second_car = CarWithInit("Honda", "Civic")
print(f"My second car is a {my_second_car.brand} {my_second_car.model}.\n")


# =================================================================================================
# 3. Instance Methods
# =================================================================================================
# Methods are functions defined inside a class. They operate on the instance's attributes.
# The first parameter of an instance method is always 'self'.

print("3. Instance Methods")

class CarWithMethods:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # This is an instance method. It uses the 'self' parameter to access instance attributes.
    def full_name(self):
        return f"{self.brand} {self.model}"

my_third_car = CarWithMethods("Ford", "Mustang")
# Calling the instance method
print(f"My third car's full name is: {my_third_car.full_name()}.\n")


# =================================================================================================
# 4. Encapsulation (Private Attributes)
# =================================================================================================
# Encapsulation is the concept of bundling data (attributes) and methods that work on the data within one unit (a class).
# In Python, we can suggest that an attribute should be "private" (not accessed directly from outside the class)
# by prefixing its name with a double underscore (__).
# This is called "name mangling".

print("4. Encapsulation (Private Attributes)")

class CarWithPrivate:
    def __init__(self, brand, model):
        self.__brand = brand  # This is now a "private" attribute.
        self.__model = model

    def get_brand(self):
        # We provide "getter" methods to allow controlled access to private attributes.
        return self.__brand

    def get_model(self):
        return self.__model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

my_private_car = CarWithPrivate("Tesla", "Model 3")
# print(my_private_car.__brand)  # This would cause an AttributeError.
# We access the private data through the getter method.
print(f"The brand of my private car is: {my_private_car.get_brand()}.\n")


# =================================================================================================
# 5. Class Methods and Class Attributes
# =================================================================================================
# A 'class attribute' is shared by all instances of the class.
# A 'class method' is a method that is bound to the class and not the object. It can modify a class state that would apply across all instances of the class.
# We use the '@classmethod' decorator to define a class method. The first parameter is 'cls', which refers to the class itself.

print("5. Class Methods and Class Attributes")

class CarWithClassAttrs:
    total_cars = 0  # This is a class attribute.

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        CarWithClassAttrs.total_cars += 1  # Increment the class attribute each time a new car is created.

    @classmethod
    def get_total_cars(cls):
        # This class method can access class attributes.
        return f"Total cars created: {cls.total_cars}"

car1 = CarWithClassAttrs("Tata", "Nexon")
car2 = CarWithClassAttrs("Mahindra", "Thar")
print(CarWithClassAttrs.get_total_cars())
print(f"Total cars from an instance: {car1.get_total_cars()}.\n") # Can be called from an instance too


# =================================================================================================
# 6. Static Methods
# =================================================================================================
# A 'static method' is a method that is related to a class but doesn't need access to the class ('cls') or instance ('self').
# It's like a regular function that lives inside the class's namespace.
# We use the '@staticmethod' decorator.

print("6. Static Methods")

class CarWithStatic:
    @staticmethod
    def general_description():
        # This method doesn't know about the class or any instance.
        return "Cars are a popular means of transport."

# We can call a static method on the class itself or on an instance.
print(f"Static method on class: {CarWithStatic.general_description()}")
my_static_car = CarWithStatic()
print(f"Static method on instance: {my_static_car.general_description()}.\n")


# =================================================================================================
# 7. Inheritance
# =================================================================================================
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# The new class is called the 'child class' or 'subclass', and the one it inherits from is called the 'parent class' or 'superclass'.

print("7. Inheritance")

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "is moving."

# Child class inheriting from Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_size):
        # 'super()' gives us access to methods in the parent class.
        # Here, we are calling the parent's __init__ method.
        super().__init__(brand, model)
        self.battery_size = battery_size

    # We can also add new methods specific to the child class.
    def charge(self):
        return f"The {self.model} is charging its {self.battery_size} battery."

my_electric_car = ElectricCar("Tesla", "Model S", "100kWh")
print(f"My electric car is a {my_electric_car.brand} {my_electric_car.model}.")
print(f"The car {my_electric_car.move()}") # Accessing parent's method
print(my_electric_car.charge()) # Accessing child's method
print("")


# =================================================================================================
# 8. Polymorphism (Method Overriding)
# =================================================================================================
# Polymorphism means "many forms". In OOP, it refers to the ability of different classes to be treated as objects of a common superclass.
# A common use of polymorphism is 'method overriding', where a child class provides a specific implementation of a method that is already defined in its parent class.

print("8. Polymorphism (Method Overriding)")

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    # Here, we override the speak method from the Animal class.
    def speak(self):
        return "Woof!"

class Cat(Animal):
    # We override it again for the Cat class.
    def speak(self):
        return "Meow!"

# A function that can work with any Animal object
def animal_sound(animal):
    print(f"The animal says: {animal.speak()}")

my_dog = Dog()
my_cat = Cat()

animal_sound(my_dog)  # Calls Dog's speak method
animal_sound(my_cat)  # Calls Cat's speak method
print("")


# =================================================================================================
# 9. Multiple Inheritance
# =================================================================================================
# A class can inherit from more than one parent class. This is called multiple inheritance.

print("9. Multiple Inheritance")

class Battery:
    def battery_info(self):
        return "This is a battery."

class Engine:
    def engine_info(self):
        return "This is an engine."

# This class inherits from both Battery and Engine
class HybridCar(Vehicle, Battery, Engine):
    def __init__(self, brand, model):
        super().__init__(brand, model)

my_hybrid = HybridCar("Toyota", "Prius")
print(f"My hybrid car is a {my_hybrid.brand} {my_hybrid.model}.")
print(my_hybrid.battery_info()) # Method from Battery class
print(my_hybrid.engine_info())  # Method from Engine class
print("")


# =================================================================================================
# 10. The isinstance() Function
# =================================================================================================
# The isinstance() function is used to check if an object is an instance of a particular class or a subclass of it.

print("10. The isinstance() Function")

my_tesla = ElectricCar("Tesla", "Model Y", "75kWh")

# Check if my_tesla is an instance of ElectricCar
print(f"Is my_tesla an instance of ElectricCar? {isinstance(my_tesla, ElectricCar)}")

# Check if my_tesla is an instance of Vehicle (the parent class)
print(f"Is my_tesla an instance of Vehicle? {isinstance(my_tesla, Vehicle)}")

# Check if my_tesla is an instance of CarWithInit
print(f"Is my_tesla an instance of CarWithInit? {isinstance(my_tesla, CarWithInit)}")
print("")


# =================================================================================================
# 11. Properties
# =================================================================================================
# Properties allow you to define "getter", "setter", and "deleter" methods for an attribute,
# but access it like a regular attribute. This is useful for validation or computed properties.

print("11. Properties")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private age

    @property
    def age(self):
        # This is the "getter" method for age. It's called when you access person.age
        print("Getting age...")
        return self.__age

    @age.setter
    def age(self, value):
        # This is the "setter" method. It's called when you set person.age = value
        print("Setting age...")
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = value

person = Person("Alice", 30)
print(f"{person.name}'s age is {person.age}") # Calls the getter

person.age = 31 # Calls the setter
print(f"Now {person.name}'s age is {person.age}")

try:
    person.age = -5
except ValueError as e:
    print(f"Error: {e}")

print("\nOOP concepts covered! Keep practicing.")

