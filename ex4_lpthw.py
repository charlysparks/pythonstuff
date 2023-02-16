# Exercise 4 from Learn Python the Hard Way 
# by Zed Shaw [https://learncodethehardway.org/python/]

# Total available cars
cars = 100
# Capacity of each car
space_in_a_car = 4.0
# Number of available drivers
drivers = 30
# Number of passengers
passengers = 90
# Calculation for cars not being driven
cars_not_driven = cars - drivers
# Cars driven is equal to the number of drivers available
cars_driven = drivers
# Total number of spots available in the carpool
carpool_capacity = cars_driven * space_in_a_car
# Average total of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cards today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
