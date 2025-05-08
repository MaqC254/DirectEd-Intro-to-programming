#Creates a variable called cars and assigns it a value of 100
cars = 100
#Creates a variable called space_in_a_car and assigns it a value of 4.0
space_in_a_car = 4.0
#Creates a variable called drivers and assigns it a value of 30
drivers = 30
#Creates a variable called passengers and assigns it a value of 90
passengers = 90
#Creates a variable called cars_not_driven and assigns it to the evaluation of cars - drivers
cars_not_driven = cars - drivers
#Creates a variable called cars_driven and assigns it to the value of drivers
cars_driven = drivers
#Creates a variable called carpool_capacity and assigns it to the evaluation of cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#Creates a variable called average_passengers_per_car and assigns it to the evaluation of passengers / cars_driven
average_passengers_per_car = passengers / cars_driven
Name = "Maxwell"
age = 22

#This code has 8 variables
#Single '=' sign is used to assign a value to a variable

#The statement prints "There are 100 cars available."
print("There are", cars, "cars available.")
#The statement prints "There are only 30 drivers available."
print("There are only", drivers, "drivers available.")
#The statement prints "There will be 70 empty cars today."
print("There will be", cars_not_driven, "empty cars today.")
#The statement prints "We can transport 120.0 people today."
print("We can transport", carpool_capacity, "people today.")
#The statement prints "We have 90 to carpool today."
print("We have", passengers, "to carpool today.")
#The statement prints "We need to put about 3.0 in each car."
print("We need to put about", average_passengers_per_car,
      "in each car.")